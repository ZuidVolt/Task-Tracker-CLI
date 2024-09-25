# task_cli.py
import argparse
import logging

# Configure logging to be more flexible and genre-agnostic
logging.basicConfig(
    level=logging.INFO,  # Set the default log level to INFO
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",  # Include timestamp, log level, and logger name
    datefmt="%Y-%m-%d %H:%M:%S",  # Use a standard date format
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set the logger level to DEBUG for this module

parser = argparse.ArgumentParser(description="Manage tasks")
subparsers = parser.add_subparsers(dest="command", required=True)

# args = add, delete, update, mark-in-progress, mark-done, list

add_parser = subparsers.add_parser("add", help="Add a item to the task list")
add_parser.add_argument("task_name", type=str, help="The name of the task")


delete_parser = subparsers.add_parser("delete", help="delete a item to the task list")
delete_parser.add_argument("task_id", type=int, help="ID of the task to delete")

update_parser = subparsers.add_parser("update", help="update a item to the task list")
update_parser.add_argument("task_id", type=int, help="ID of the task to Update")

mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="mark-in-progress a item to the task list")
mark_in_progress_parser.add_argument("task_id", type=int, help="ID of the task to mark as in progress")

mark_done_parser = subparsers.add_parser("mark-done", help="mark-done a item to the task list")
mark_done_parser.add_argument("task_id", type=int, help="ID of the task to mark as done")


list_parser = subparsers.add_parser("list", help="List all tasks")

args = parser.parse_args()


def main():
    if args.command == "add":
        pass
    if args.command == "delete":
        pass
    if args.command == "update":
        pass
    if args.command == "mark-in-progress":
        pass
    if args.command == "mark-done":
        pass
    if args.command == "list":
        pass
    else:
        raise NotImplementedError(f"Command {args.command} not implemented")


if __name__ == "__main__":
    main()
