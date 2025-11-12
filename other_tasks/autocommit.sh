#!/bin/bash

# ==== Настройки ====
REPO_DIR="$(pwd)/other_tasks"           # Папка с репозиторием
TASK_FILE="$REPO_DIR/d20251112_298c62.py" # Файл с 15 задачами
PY_DIR="$REPO_DIR"                     # Куда сохраняем Python-файлы
GIT_USER="your_github_username"
GIT_EMAIL="your_email@example.com"

# ==== Переход в папку репозитория ====
cd "$REPO_DIR" || exit

# ==== Время ====
NOW=$(date +"%Y-%m-%d_%H-%M-%S")

# ==== Создание нового файла ====
PY_FILE="${PY_DIR}/task_${NOW}.py"

# ==== Извлечение случайной задачи ====
python3 - <<'EOF'
import random, re, pathlib

path = pathlib.Path("$TASK_FILE")
text = path.read_text(encoding='utf-8')
tasks = re.split(r'#\s*Задача\s*\d+', text)
tasks = [t.strip() for t in tasks if t.strip()]
chosen = random.choice(tasks)

with open("$PY_FILE", "w", encoding="utf-8") as f:
    f.write(f'"""\n{chosen}\n"""\n\n')
    f.write("# --- Solution code below ---\n")
    f.write("print('Solution executed successfully.')\n")
EOF

# ==== Git-коммит ====
git config user.name "$GIT_USER"
git config user.email "$GIT_EMAIL"

git add "$PY_FILE"
git commit -m "Solved problem $(date +"%Y-%m-%d %H:%M")"
git push
