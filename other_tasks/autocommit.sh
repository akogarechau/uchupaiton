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
    f.write(f'"""\n{chosen}\n"""\n\n')
    f.write("# --- Solution code below ---\n")
    # Добавляем импорты если они есть в исходном файле
    if "import random" in text:
        f.write("import random\\n")
    if "import string" in text:
        f.write("import string\\n")
    f.write("\\n")
    f.write("# Your solution implementation here\\n")
    f.write("print('Task file created successfully.')\\n")

print(f"Created: {path}")
EOF

# ==== Git-коммит ====
git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"

git add "$PY_FILE"
git commit -m "Auto-commit: random task $(date +"%Y-%m-%d %H:%M")"
git push

# ==== Очистка состояния ====
git restore . || true
