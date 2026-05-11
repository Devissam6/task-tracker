# print("Hello world")
import argparse

parser = argparse.ArgumentParser(
    prog="task-tracker",
    description="CLI app to track your tasks and manage your to-do list."
)

parser.add_argument('action', help="Action to take")
parser.add_argument('id', help="ID number of existing task")
parser.add_argument('context', help="Title or status of task")

args = parser.parse_args()
print(args)
