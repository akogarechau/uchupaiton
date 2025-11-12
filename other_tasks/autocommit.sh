#!/bin/bash
set -e

# ==== Настройки ====
REPO_DIR="$(pwd)/other_tasks"
TASK_FILE="$REPO_DIR/d20251112_298c62.py"
PY_DIR="$REPO_DIR"

cd "$REPO_DIR" || exit

# ==== Время ====
NOW=$(date +"%Y-%m-%d_%H-%M-%S")
PY_FILE="${PY_DIR}/task_${NOW}.py"

# ==== Извлечение случайной задачи ====
python3 - <<EOF
import random, re, pathlib

task_file = pathlib.Path("$TASK_FILE")
if not task_file.exists():
    raise FileNotFoundError(f"Task file not found: {task_file}")

text = task_file.read_text(encoding='utf-8')

# Ищем задачи по шаблону: # номер. описание
pattern = r'#\s*\d+\..*?(?=#\s*\d+\.|\Z)'
tasks = re.findall(pattern, text, re.DOTALL)

if not tasks:
    raise ValueError("No tasks found in file")

chosen = random.choice(tasks).strip()

path = pathlib.Path("$PY_FILE")
with open(path, "w", encoding="utf-8") as f:
    f.write(f'{chosen}\n')


print(f"Created: {path}")
EOF

# ==== Git-коммит ====
git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"

git add "$PY_FILE"
git commit -m "Auto-commit: Task done $(date +"%Y-%d-%m || %H:%M")"
git push

# ==== Очистка состояния ====
git restore . || true
