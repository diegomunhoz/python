import _thread
import time

num_thread = 0
max_loop = 5
thread_started = False


def task(task_name, delay):
    global num_thread, max_loop, thread_started
    thread_started = True
    num_thread += 1
    ct = 0
    while ct < max_loop:
        time.sleep(delay)
        print("Thread: % s" % (task_name))
        ct += 1
    num_thread -= 1


_thread.start_new_thread(task, ("Tarefa 1", 2))
_thread.start_new_thread(task, ("Tarefa 2", 4))

while not thread_started:
    pass
while num_thread > 0:
    pass