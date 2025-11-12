#!/bin/bash
# --- autocommit.sh ---
# Автогенерация и коммит простых Python-задач 4 раза в день

set -e

# Текущая дата и время
NOW=$(date '+%Y-%m-%d_%H-%M-%S')
FILENAME="task_${NOW}.py"

# Папка, где лежит скрипт
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Выбираем случайную задачу из файла deepseek_python_20251112_298c62.py
# и создаём новый Python-файл
python3 - <<'EOF'
import random, re, os, datetime

source = "d20251112_298c62.py"
if not os.path.exists(source):
    raise SystemExit(f"{source} not found")

with open(source, "r", encoding="utf-8") as f:
    text = f.read()

# Разделяем задачи по строкам вида "# --- Task ---" (если таких нет, берём функции)
blocks = re.split(r'\n\s*#\s*---\s*Task\s*---\s*\n', text)
task = random.choice([b for b in blocks if len(b.strip()) > 0])

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
filename = f"task_{now.replace(':', '-')}.py"

with open(filename, "w", encoding="utf-8") as f:
    f.write('"""\n')
    f.write(f"Task generated automatically at {now}\n\n")
    f.write("Solve the following problem:\n")
    f.write(task.split('\n')[0] + "\n")
    f.write('"""\n\n')
    f.write(task)
EOF

# Коммит и пуш
cd "$DIR"
git add .
git commit -m "Solved task: $(date '+%Y-%m-%d %H:%M:%S')"
git push
