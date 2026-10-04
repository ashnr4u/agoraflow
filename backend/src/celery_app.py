from celery import Celery

celery_app = Celery(
    "agoraflow",
    broker="redis://redis_database:6379/0",
    include=["src.tasks"]
)