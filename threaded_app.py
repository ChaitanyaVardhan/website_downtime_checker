# threaded_app
import time
import Queue
from threading import Thread
from websites import WEBSITE_LIST
from utils import check_website

NUM_WORKERS = 4
task_queue = Queue.Queue()

def worker():
    # Constantly check the queue for addresses
    while True:
        address = task_queue.get()
        check_website(address)
        
        task_queue.task_done()

start_time = time.time()

#Create the worker threads
threads = [Thread(target=worker) for _ in range(NUM_WORKERS)]

#Add the websites to queue
[task_queue.put(item) for item in WEBSITE_LIST]

#start all the workers
[thread.start() for thread in threads]

#wait for all tasks in the queue to be processed
task_queue.join()

end_time = time.time()

print 'Time for threaded app is {}'.format(end_time-start_time)

