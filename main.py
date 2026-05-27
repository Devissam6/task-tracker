import argparse
import json
import os.path
from pathlib import Path

# ==================== HANDLING CLI ARGUMENTS ====================

parser = argparse.ArgumentParser(
    prog="task-tracker",
    description="CLI app to track your tasks and manage your to-do list."
)

parser.add_argument('action', help="Action to take")
parser.add_argument('id', help="ID number of existing task")
parser.add_argument('context', help="Title or status of task")

args = parser.parse_args()
print(args)

# ==================== HANDLING FILE IO ====================

# if not os.path.exists('./tasks.json'):
json_path = Path("tasks.json")
if not json_path.exists():
    json_path.touch()
    print(f"{json_path} created.")
else:
    print(f"{json_path} already exists.")