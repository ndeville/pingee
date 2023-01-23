from datetime import datetime
import os
import time
import speedtest
import csv

from dotenv import load_dotenv
load_dotenv()
USER = os.getenv("USER")
LOG_PATH = os.getenv("LOG_PATH")

date = f"{datetime.now().strftime('%y%m%d')}"

test = True
v = True # verbose mode

tests_to_run = 3
threads = 1 # 1 simulates a typical file transfer, else None
log_file = LOG_PATH

count = 0

def test_speed(count, threads=None, servers=[]):
    global date
    start_test_time = time.time()
    s = speedtest.Speedtest()
    # s.get_servers(servers)
    try:
        s.get_best_server()
        download = s.download(threads=threads)
        download_mbps = f"{round(download / 1000000, 2)} Mb/s"
        run_time = round((time.time() - start_test_time), 1)
        timestamp = datetime.now().strftime('%H:%M:%S')
        print(f"#{count} [{timestamp}] {download_mbps} ({run_time}s test time)")

        with open(log_file, 'a', newline='', encoding='utf-8') as i:
            writer = csv.writer(i, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            if threads == None:
                threads = 'multi'
            writer.writerow([date, timestamp, int(download), download_mbps, threads, run_time, "OK"])

        return download

    except Exception as e:
        timestamp = datetime.now().strftime('%H:%M:%S')
        run_time = round((time.time() - start_test_time), 1)
        error_message = f"ERROR: {e}"
        with open(f"log.csv", 'a', newline='', encoding='utf-8') as i:
            writer = csv.writer(i, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            if threads == None:
                threads = 'multi'
            writer.writerow([date, timestamp, "ERROR", "ERROR", threads, run_time, error_message])

        print(error_message)

        return "ERROR"

print(f"\nStarting speed test with {tests_to_run} runs (threads={threads})...\n")

for x in range(0, tests_to_run):
    count += 1
    test_speed(count, threads=threads)
print()