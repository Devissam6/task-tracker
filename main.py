# ==================== IMPORTS ====================

import argparse
from datetime import datetime
import json
from pathlib import Path

# ==================== DEFINED FUNCTIONS ====================

def find_task_by_id(task_list, task_id):
    for task in task_list:
        if task['id'] == task_id:
            return task
    return None

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
update_parser.add_argument("id", type=int, help="ID of the task")
update_parser.add_argument("description", help="Description of the task")

delete_parser = subparsers.add_parser('delete', help="Delete a task")
delete_parser.add_argument("id", type=int, help="ID of the task")

mark_done_parser = subparsers.add_parser('mark-done', help="Mark a task as done")
mark_done_parser.add_argument("id", type=int, help="ID of the task")

mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help="Mark a task as in progress")
mark_in_progress_parser.add_argument("id", type=int, help="ID of the task")

list_parser = subparsers.add_parser('list', help="List all tasks")
list_parser.add_argument("status", nargs='?', choices=('done', 'prog', 'todo'), help="Filter by done, in progress, incomplete tasks")


args = parser.parse_args()
# print(f"args: {args}") #DEBUG

# ==================== HANDLING FILE IO ====================

json_path = Path("tasks.json")
if not json_path.exists():
    json_path.write_text("[]")
    # print(f"{json_path} created.") #DEBUG
else:
    # print(f"{json_path} already exists.") #DEBUG
    pass

# ==================== DECODING JSON OBJECT ====================

tasks = json.loads(json_path.read_text())
# print(f"Tasks: {tasks}; len: {len(tasks)}; type: {type(tasks)}") #DEBUG

# ==================== PROCESS ACTIONS ====================

if args.action == "add":
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = 1 + max(task['id'] for task in tasks)
    tasks.append({'id': new_id, 'description': args.description, 'status': 'todo', 'createdAt': datetime.now().isoformat(), 'updatedAt': datetime.now().isoformat()})
    print(f'Added task: {args.description}')

elif args.action == "update":
    task_dict = find_task_by_id(tasks, args.id)
    print(f'Updated task: [{args.id}] [{task_dict['description']}] -> [{args.description}]')
    task_dict['description'] = args.description
    task_dict['updatedAt'] = datetime.now().isoformat()

elif args.action == "delete":
    task_dict = find_task_by_id(tasks, args.id)
    print(f'Deleted task: [{args.id}] [{task_dict['description']}]')
    tasks.pop(tasks.index(task_dict))

elif args.action == "mark-done":
    task_dict = find_task_by_id(tasks, args.id)
    task_dict['status'] = 'done'
    task_dict['updatedAt'] = datetime.now().isoformat()
    print(f'Marked done: [{args.id}] [{task_dict['description']}]')

elif args.action == "mark-in-progress":
    task_dict = find_task_by_id(tasks, args.id)
    task_dict['status'] = 'prog'
    task_dict['updatedAt'] = datetime.now().isoformat()
    print(f'Marked in progress: [{args.id}] [{task_dict['description']}]')

elif args.action == "list":
    if args.status:
        [print(task) for task in tasks if task['status'] == args.status]
    else:
        [print(task) for task in tasks]
# ==================== WRITE TO FILE ====================

# print(tasks) #DEBUG
json_path.write_text(json.dumps(tasks))