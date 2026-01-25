# Daily Calorie Tracker (Terminal App)

A simple **terminal-based calorie tracker** 

You can log calories in 2 ways:
- **Manual**: type the calories yourself
- **Text (LLM estimate)**: type what you ate (ex: `2 eggs`) and the app estimates calories using **Ollama (local LLM)**

---

## Features

- Multi-user support (login / create user)
- Daily calorie goal per user
- Add / update / delete entries
- Daily summary + weekly summary (last 7 days)
- Export entries for a day to JSON
- Remembers last logged-in user

---


## Project Files

- `main.py` – runs the app + menus
- `flows.py` – app logic (login, add entry, summaries, export)
- `services.py` – database functions + config helpers
- `db.py` – SQLite connection + table creation
- `models.py` – `User` and `Entry` classes
- `estimator.py` – calorie estimator (Ollama LLM)
- `ui.py` – terminal printing helpers
- `prompts.py` – input helpers / validation
- `config.json` – stores last user id


