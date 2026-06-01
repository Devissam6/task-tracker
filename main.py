import argparse
from datetime import datetime
import json
import os.path
from pathlib import Path

# ==================== HANDLING CLI ARGUMENTS ====================

parser = argparse.ArgumentParser(
    prog="task-tracker",
    description="CLI app to track your tasks and manage your to-do list."
)

subparsers = parser.add_subparsers(
    dest="action",
    help="Action to take",
)

add_parser = subparsers.add_parser('add', help="Add a task")
add_parser.add_argument("description", help="Description of the task")

update_parser = subparsers.add_parser('update', help="Update a task")
update_parser.add_argument("id", help="ID of the task")
update_parser.add_argument("description", help="Description of the task")

delete_parser = subparsers.add_parser('delete', help="Delete a task")
delete_parser.add_argument("id", help="ID of the task")

mark_done_parser = subparsers.add_parser('mark-done', help="Mark a task as done")
mark_done_parser.add_argument("id", help="ID of the task")

mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help="Mark a task as in progress")
mark_in_progress_parser.add_argument("id", help="ID of the task")

list_parser = subparsers.add_parser('list', help="List all tasks")
list_parser.add_argument("filter", nargs='?', choices=('done', 'prog', 'todo'), help="Filter by done, in progress, incomplete tasks")


# parser.add_argument('action', help="Action to take", choices=["add", "update", "delete", "mark-done", "mark-in-progress", "list"])
# parser.add_argument('id', help="ID number of existing task (not required for add, list)", nargs='?', default=0, type=int)
# parser.add_argument('context', help="Title or status of task (not required for delete, mark-done, mark-in-progress, list)", nargs='?', default="", type=str)

args = parser.parse_args()
print(f"args: {args}") #DEBUG

# ==================== HANDLING FILE IO ====================

# if not os.path.exists('./tasks.json'):
json_path = Path("tasks.json")
if not json_path.exists():
    json_path.write_text("[]")
    print(f"{json_path} created.") #DEBUG
else:
    print(f"{json_path} already exists.") #DEBUG

# ==================== DECODING JSON OBJECT ====================

tasks = json.loads(json_path.read_text())
print(f"Tasks: {tasks}; len: {len(tasks)}; type: {type(tasks)}") #DEBUG

# ==================== PROCESS ARGS ====================


if args.action == "add":
    tasks.append({'id': len(tasks) + 1, 'description': args.description, 'status': 'todo', 'createdAt': datetime.now().isoformat(), 'updatedAt': datetime.now().isoformat()})
    print(f'Added task: {args.description}')

elif args.action == "update":
    # Action
    print(f'Updated task: [{args.id}] {args.description}')

elif args.action == "delete":
    # Action
    print(f'Deleted task: [{args.id}] {args.description}')

elif args.action == "mark-done":
    # Action
    print(f'Marked done: [{args.id}] {args.description}')

elif args.action == "mark-in-progress":
    # Action
    print(f'Marked in progress: [{args.id}] {args.description}')

elif args.action == "list":
    # Action
    print(f'List')

# ==================== WRITE TO FILE ====================

print(tasks) #DEBUG
json_path.write_text(json.dumps(tasks))