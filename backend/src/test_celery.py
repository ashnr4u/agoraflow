from celery import Celery

test_app = Celery(
    "test",
    broker="redis://localhost:6379/0"
)

result = test_app.send_task("src.tasks.test_task")

print(result.id)