import time
import multiprocessing
from websites import WEBSITE_LIST
from utils import check_website

NUM_WORKERS = 4

start_time = time.time()

pool = multiprocessing.Pool(processes=NUM_WORKERS)
results = pool.map_async(check_website, WEBSITE_LIST)
results.wait()

end_time = time.time()

print ('Time for multiprocessing app is {}'.format(end_time-start_time))
