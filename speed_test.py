from datetime import datetime
import os
print("----------")
ts_file = f"{datetime.now().strftime('%y%m%d-%H%M')}"
ts_db = f"{datetime.now().strftime('%Y-%m-%d %H:%M')}"
ts_time = f"{datetime.now().strftime('%H:%M:%S')}"
print(f"{ts_time} starting {os.path.basename(__file__)}")
import time
start_time = time.time()

from dotenv import load_dotenv
load_dotenv()
USER = os.getenv("USER")

import sys
sys.path.append(f"/Users/{USER}/Python/indeXee")

# import my_utils
# import grist_BB
# import grist_PE
# import dbee

from inspect import currentframe
def get_linenumber():
    """
    print line numbers with f"{get_linenumber()}"
    """
    cf = currentframe()
    return cf.f_back.f_lineno

import pprint
pp = pprint.PrettyPrinter(indent=4)

count = 0
count_row = 0

test = True
v = True # verbose mode

print(f"{os.path.basename(__file__)} boilerplate loaded -----------\n")
####################
# testing speedtest-cli

import speedtest

servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1
# or
# threads = None

# s = speedtest.Speedtest()

# get_servers = s.get_servers(servers)
# print(f"\n#{get_linenumber()} {get_servers=}")
# get_best_server = s.get_best_server()
# print(f"\n#{get_linenumber()} {get_best_server=}")
# download = s.download(threads=threads)
# print(f"\n#{get_linenumber()} {download=}")
# s.upload(threads=threads)

# share = s.results.share()
# print(f"\n#{get_linenumber()} {share=}")
# results_dict = s.results.dict()
# print(f"\n#{get_linenumber()} {results_dict=}")

def test_speed(count, threads=None):
    start_test_time = time.time()
    s = speedtest.Speedtest()
    # s.get_servers(servers)
    s.get_best_server()
    download = s.download(threads=threads)
    download_mbps = f"{round(download / 1000000, 2)} Mbit/s"
    run_time = round((time.time() - start_test_time), 1)
    print(f"run#{count} [{datetime.now().strftime('%H:%M:%S')}] {download_mbps} ({run_time})")
    return download

for x in range(0,3):
    count += 1
    print(count)
    test_speed()



########################################################################################################

if __name__ == '__main__':
    print()
    print()
    print('-------------------------------')
    print(f"{os.path.basename(__file__)}")
    print()
    print(f"{count=}")
    print()
    print('-------------------------------')
    run_time = round((time.time() - start_time), 1)
    if run_time > 60:
        print(f'{os.path.basename(__file__)} finished in {run_time/60} minutes.')
    else:
        print(f'{os.path.basename(__file__)} finished in {run_time}s.')
    print()