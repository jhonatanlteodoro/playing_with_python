from flask import Flask
from celery import Celery
import requests, time

app = Flask(__name__)


def make_celery(app):
    celery = Celery(
        app.import_name, broker='redis://localhost:6379', backend='redis://localhost:6379'
    )
    # celery.conf.update(app.config["CELERY_CONFIG"])

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery = make_celery(app)


@celery.task()
def add_together(a, b):
    print(a+b)
    return a + b



@celery.task()
def send_request():
    print("from task")
    return requests.get("https://docs.python.org/3/").status_code

@celery.task()
def generate_requests_calls():
    return [i for i in range(1, 30)]


@app.route("/")
def hello_world():
    add_together.delay(10, 20)
    return "<p>Hello, World!</p>"


@app.route("/2")
def hello_world2():
    start_time = time.time()
    urls = generate_requests_calls.delay()
    urls = urls.get(timeout=1)

    results = []
    for _ in urls:
        result = send_request.delay()
        results.append(result)
    
    for res in results:
        print(res.get(timeout=1))

    print("--- %s seconds ---" % (time.time() - start_time))
    return "<p>Hello, World!</p>"



@app.route("/3")
def hello_world3():
    start_time = time.time()

    results = []
    for i in range(1, 30):
        results.append(requests.get("https://docs.python.org/3/").status_code)
        print("from normal requests")
    for res in results:
        print(res)

    print("--- %s seconds ---" % (time.time() - start_time))
    return "<p>Hello, World!</p>"



# how to run
#  celery -A background_task.celery worker
#  FLASK_APP=background_task.py flask run



"""
Notes: you can do this kind of thing like you see on hello_world2 and 3
I didn't see to much difference here, even the celery are using many different works.

I'll test more, maybe I'm missing something, implementation details or something like that


CELERY LOGS

[2023-01-23 11:55:53,948: WARNING/ForkPoolWorker-16] from task
[2023-01-23 11:55:53,948: WARNING/ForkPoolWorker-1] from task
[2023-01-23 11:55:53,963: WARNING/ForkPoolWorker-3] from task
[2023-01-23 11:55:53,962: WARNING/ForkPoolWorker-2] from task
[2023-01-23 11:55:53,979: WARNING/ForkPoolWorker-4] from task
[2023-01-23 11:55:53,979: WARNING/ForkPoolWorker-5] from task
[2023-01-23 11:55:53,996: WARNING/ForkPoolWorker-6] from task
[2023-01-23 11:55:53,996: WARNING/ForkPoolWorker-7] from task
[2023-01-23 11:55:54,013: WARNING/ForkPoolWorker-8] from task
[2023-01-23 11:55:54,014: WARNING/ForkPoolWorker-9] from task
[2023-01-23 11:55:54,032: WARNING/ForkPoolWorker-16] from task
[2023-01-23 11:55:54,033: WARNING/ForkPoolWorker-2] from task
[2023-01-23 11:55:54,050: WARNING/ForkPoolWorker-1] from task
[2023-01-23 11:55:54,051: WARNING/ForkPoolWorker-3] from task
[2023-01-23 11:55:54,067: WARNING/ForkPoolWorker-4] from task
[2023-01-23 11:55:54,067: WARNING/ForkPoolWorker-5] from task
[2023-01-23 11:55:54,085: WARNING/ForkPoolWorker-6] from task
[2023-01-23 11:55:54,085: WARNING/ForkPoolWorker-7] from task
[2023-01-23 11:55:54,103: WARNING/ForkPoolWorker-16] from task
[2023-01-23 11:55:54,104: WARNING/ForkPoolWorker-2] from task
[2023-01-23 11:55:54,119: WARNING/ForkPoolWorker-1] from task
[2023-01-23 11:55:54,120: WARNING/ForkPoolWorker-3] from task
[2023-01-23 11:55:54,135: WARNING/ForkPoolWorker-5] from task
[2023-01-23 11:55:54,135: WARNING/ForkPoolWorker-4] from task
[2023-01-23 11:55:54,152: WARNING/ForkPoolWorker-8] from task
[2023-01-23 11:55:54,152: WARNING/ForkPoolWorker-6] from task
[2023-01-23 11:55:54,167: WARNING/ForkPoolWorker-16] from task
[2023-01-23 11:55:54,167: WARNING/ForkPoolWorker-1] from task
[2023-01-23 11:55:54,180: WARNING/ForkPoolWorker-2] from task

"""