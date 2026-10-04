from src.celery_app import celery_app


@celery_app.task
def test_task():
    print("AgoraFlow Celery task executed successfully!")