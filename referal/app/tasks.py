from time import sleep

from celery import shared_task


@shared_task
def simple_task():
    for _ in range(5):
        sleep(2)
        print(10+20)
    return True