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
print(f"args: {args}")

# ==================== HANDLING FILE IO ====================

# if not os.path.exists('./tasks.json'):
json_path = Path("tasks.json")
if not json_path.exists():
    json_path.write_text("{}")
    print(f"{json_path} created.")
else:
    print(f"{json_path} already exists.")

# ==================== DECODING JSON OBJECT ====================

tasks = json.loads(json_path.read_text())
print(f"Tasks: {tasks}; len: {len(tasks)}")

# ==================== PROCESS ARGS ====================

print(f"Action: {args.action}; type: {type(args.action)}")

# test = input("what: ")
# print(f"test: {test}")