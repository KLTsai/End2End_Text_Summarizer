from fastapi import APIRouter, HTTPException, BackgroundTasks
from textSummarizer.models.api_models import TextInput, PredictResponse, TrainingResponse
from textSummarizer.tasks.training import run_training_task, get_task_status
from textSummarizer.pipeline.prediction_pipeline import PredictionPipeline
import uuid


router = APIRouter(prefix="/api/v1")

# Predict endpoint
@router.post("/predict", response_model=PredictResponse, tags=["Prediction"])
async def predict(text_input: TextInput):
    """
    Predict a summary for the given text.

    Args:
        text_input (TextInput): JSON body with a "text" field.

    Returns:
        PredictResponse: JSON response with the summary.
    """
    try:
        # input validation
        if not text_input.text.strip():
            raise HTTPException(status_code=400, detail="Text cannot be empty")

        obj = PredictionPipeline()
        summary = obj.predict(text_input.text)

        return PredictResponse(
            status="success",
            data={"summary": summary},
            message=None
        )
    except Exception as e:
        return PredictResponse(
            status="error",
            data=None,
            message=f"Prediction failed: {str(e)}"
        )

# start training endpoint
@router.post("/training/start", response_model=TrainingResponse, tags=["Training"])
async def start_training(background_tasks: BackgroundTasks):
    """
    Start a training task asynchronously.

    Returns:
        TrainingResponse: JSON response with the task ID.
    """
    try:
        task_id = str(uuid.uuid4())
        background_tasks.add_task(run_training_task, task_id)
        return TrainingResponse(
            status="success",
            data={"task_id": task_id},
            message="Training task started"
        )
    except Exception as e:
        return TrainingResponse(
            status="error",
            data=None,
            message=f"Failed to start training: {str(e)}"
        )

# checking training status
@router.get("/training/status", response_model=TrainingResponse, tags=["Training"])
async def get_training_status(task_id: str):
    """
    Get the status of a training task.

    Args:
        task_id (str): The ID of the training task (query parameter).

    Returns:
        TrainingResponse: JSON response with the task status.
    """
    task_info = get_task_status(task_id)
    if not task_info:
        return TrainingResponse(
            status="error",
            data=None,
            message="Task not found"
        )
    
    return TrainingResponse(
        status="success",
        data={
            "task_id": task_id,
            "status": task_info["status"],
            "progress": task_info.get("progress", 0),
            "message": task_info.get("message", None)
        },
        message=None
    )