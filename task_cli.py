# task_cli.py
import argparse


parser = argparse.ArgumentParser(description="Manage tasks")
subparsers = parser.add_subparsers(dest="command", required=True)

# args = add, delete, update, mark-in-progress, mark-done, list

add_parser = subparsers.add_parser("add", help="Add a item to the task list")
add_parser.add_argument("name", type=str, choices=["task_name"], help="the name of the task")

delete_parser = subparsers.add_parser("delete", help="delete a item to the task list")

update_parser = subparsers.add_parser("update", help="update a item to the task list")

mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="mark-in-progress a item to the task list")

mark_done_parser = subparsers.add_parser("mark-done", help="mark-done a item to the task list")

args = parser.parse_args()
