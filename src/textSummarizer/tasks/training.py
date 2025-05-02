import os
import asyncio
from typing import Dict


# simulate status of tasks (using Redis or DB in reality)
task_status: Dict[str, dict] = {}

async def run_training_task(task_id: str):
    """
    Run a training task asynchronously.

    Args:
        task_id (str): The ID of the training task.
    """
    task_status[task_id] = {"status": "running", "progress": 0}
    try:
        # process simulation
        for i in range(100):
            await asyncio.sleep(0.1)  # training time simulation
            task_status[task_id]["progress"] = i + 1
        # execution
        os.system("python main.py")
        task_status[task_id]["status"] = "completed"
    except Exception as e:
        task_status[task_id]["status"] = "failed"
        task_status[task_id]["message"] = str(e)

def get_task_status(task_id: str) -> dict:
    """
    Get the status of a training task.

    Args:
        task_id (str): The ID of the training task.

    Returns:
        dict: The task status information.
    """
    return task_status.get(task_id)