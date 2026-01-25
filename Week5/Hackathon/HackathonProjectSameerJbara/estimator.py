import re
import json
import ast
from dataclasses import dataclass
from typing import Optional, Dict
import requests

@dataclass(frozen=True)
class EstimateResult:
    calories: int
    method: str
    note: str


# -------------------------
# Ollama config
# -------------------------
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2:1b"


def _extract_json(text: str) -> str:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("No JSON object found in LLM output.")
    return text[start:end + 1]


def _parse_llm_json(text: str) -> dict:
    t = (text or "").strip()

    # strict JSON first
    try:
        return json.loads(t)
    except Exception:
        pass

    # then try extracting {...}
    block = _extract_json(t)

    try:
        return json.loads(block)
    except Exception:
        # handles cases like single quotes/trailing commas
        return ast.literal_eval(block)


def _ollama_calories_only(food_text: str, timeout_sec: float = 60.0) -> int:
    # IMPORTANT: escape braces {{ }}
    prompt = """Return ONLY JSON. No extra text.
Schema:
{{
  "calories": <int>
}}
Food: {food}
""".format(food=food_text.strip())

    r = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "format": "json",
            "options": {
                "num_predict": 30,
                "temperature": 0.0
            }
        },
        timeout=timeout_sec
    )
    r.raise_for_status()

    raw = r.json().get("response", "")
    data = _parse_llm_json(raw)

    cals = data.get("calories", None)
    if cals is None:
        # fallback: first number in response
        m = re.search(r"(\d{1,6})", raw)
        if not m:
            raise ValueError("LLM response did not include calories.")
        return int(m.group(1))

    return int(cals)


def estimate_calories(food_text: str, prefer_api: bool = True) -> EstimateResult:
    """
    Used by flows.py for: "Text (estimate calories)" :contentReference[oaicite:2]{index=2}

    Now: just send the text to the local Ollama LLM and return the number.
    """
    food_text = (food_text or "").strip()
    if not food_text:
        return EstimateResult(calories=0, method="text_estimate", note="Empty input.")

    calories = _ollama_calories_only(food_text)

    # method must be one of: manual/text_estimate/api_guess :contentReference[oaicite:3]{index=3}
    return EstimateResult(
        calories=max(calories, 0),
        method="text_estimate",
        note=f"LLM (Ollama: {OLLAMA_MODEL})"
    )
