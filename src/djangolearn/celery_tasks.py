from djangolearn.celery_app import app


@app.task
def send_report(x, y):
    return x+y
