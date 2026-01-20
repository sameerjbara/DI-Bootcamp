# anagram_checker.py

from __future__ import annotations

from pathlib import Path
from typing import List, Set


class AnagramChecker:
    def __init__(self, word_list_path: str | Path = "words.txt") -> None:
        """
        Load the word list into a searchable structure.
        Expected format: one word per line.
        """
        path = Path(word_list_path)
        if not path.exists():
            raise FileNotFoundError(f"Word list file not found: {path.resolve()}")

        self.words: Set[str] = set()
        with path.open("r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                w = line.strip().lower()
                if w.isalpha():  # keep only clean words
                    self.words.add(w)

    def is_valid_word(self, word: str) -> bool:
        """
        Return True if 'word' is a valid English word found in the word list.
        """
        if not isinstance(word, str):
            return False
        w = word.strip().lower()
        return w in self.words

    def is_anagram(self, word1: str, word2: str) -> bool:
        """
        Return True if word1 and word2 are anagrams (same letters, different order),
        False otherwise.
        """
        w1 = word1.strip().lower()
        w2 = word2.strip().lower()

        if w1 == w2:
            return False
        if len(w1) != len(w2):
            return False
        return sorted(w1) == sorted(w2)

    def get_anagrams(self, word: str) -> List[str]:
        """
        Return a list of all anagrams of 'word' found in the word list.
        Does not print anything.
        """
        w = word.strip().lower()
        if not w.isalpha():
            return []

        target_sorted = sorted(w)
        results = []

        # Only check words of same length to be efficient
        for candidate in self.words:
            if len(candidate) != len(w):
                continue
            if candidate == w:
                continue
            if sorted(candidate) == target_sorted:
                results.append(candidate)

        return sorted(results)
