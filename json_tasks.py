# json_tasks.py
from pathlib import Path
import json
from datetime import datetime
import logging

# Configure logging to be more flexible and genre-agnostic
logging.basicConfig(
    level=logging.INFO,  # Set the default log level to INFO
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",  # Include timestamp, log level, and logger name
    datefmt="%Y-%m-%d %H:%M:%S",  # Use a standard date format
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set the logger level to DEBUG for this module

TASK_FILE = Path("tasks.json")


def load_tasks() -> list[dict]:
    try:
        if not TASK_FILE.exists():
            return []
        with TASK_FILE.open() as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"Task file '{TASK_FILE}' does not exist. Starting with an empty task list.")
        return []
    except json.JSONDecodeError:
        logger.error("Invalid JSON data in the task file. Starting with an empty task list.")
        return []


def save_tasks(tasks: list[dict]) -> None:
    try:
        with TASK_FILE.open("w") as file:
            json.dump(tasks, file)
    except OSError as e:
        logger.error(f"Failed to write tasks to '{TASK_FILE}': {e}")


def add_task(task_name: str) -> None:
    tasks = load_tasks()
    task_id = max([task["id"] for task in tasks], default=0) + 1
    task = {
        "id": task_id,
        "task_name": task_name,
        "status": "todo",
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }
    if not task_name.strip():
        print("Task name cannot be empty.")
        return
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")
    return


def delete_task(task_id: int) -> None:
    tasks = load_tasks()
    task_exists = any(task["id"] == task_id for task in tasks)
    if not task_exists:
        print(f"Task with ID {task_id} does not exist.")
        return
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task with ID {task_id} deleted successfully.")


def display_tasks() -> None:
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\nTask List:")
    print("===========")
    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Task Name: {task['task_name']}")
        print(f"Status: {task['status']}")
        print(f"Created At: {task['created_at']}")
        print(f"Updated At: {task['updated_at']}")
        print("-" * 30)
    print("\n")


def mark_in_progress(task_id: int) -> None:
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updated_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as in-progress.")
            return
    print(f"Task with ID {task_id} not found.")


if __name__ == "__main__":
    add_task("Test Task")
    # Test the load_tasks function
    tasks = load_tasks()
    print("Loaded tasks:", tasks)
    # Test the delete_task function
    delete_task(1)
    tasks = load_tasks()
    print("Tasks after deletion:", tasks)
