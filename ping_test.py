### Working code for pinging a list of hosts every x second

from ping3 import ping
import time
from datetime import datetime
print("----------\n")

run_time = 24 # in hours, as integer

ping_wait = 1 # in seconds, as integer

log_file = '/Users/nic/Python/pingee/log/log.txt'

ts_db = f"{datetime.now().strftime('%Y-%m-%d %H:%M')}"

hostnames = {
            '208.67.222.222': 'OpenDNS', # OpenDNS
            '208.67.220.220': 'OpenDNS', # OpenDNS  
            '1.1.1.1': 'Cloudflare', # Cloudflare
            '1.0.0.1': 'Cloudflare', # Cloudflare
            '8.8.8.8': 'Google', # Google
            '8.8.4.4': 'Google', # Google
}

def log_message(s):
    global log_file
    with open(log_file, 'a') as file:
        file.write(s)

loops = int((run_time * 60 * 60) / len(hostnames))
print(f"\nRunning {loops} loops...\n")

log_message(f"\n\n---------- STARTING {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

for i in range(0,loops): # 14400 seconds in 24h

    for host,hostname in hostnames.items():
        p = ping(host)
        # print(f"\n{p=}")
        if p != None:
            p_format = round(p*1000, 2)   

            if hostname == 'OpenDNS':
                print(f"{i}/{loops}\t{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\t✅\t{host}/{hostname}\t{p_format}ms")
            if hostname == 'Cloudflare':
                print(f"{i}/{loops}\t{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\t✅\t{host}/{hostname}\t{p_format}ms")
            if hostname == 'Google':
                print(f"{i}/{loops}\t{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\t✅\t{host}/{hostname}\t\t{p_format}ms")

        else:
            p = '-'
            if hostname == 'OpenDNS':
                print(f"{i}/{loops}\t{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\t❌\t{host}/{hostname}\t{p}")
            if hostname == 'Cloudflare':
                print(f"{i}/{loops}\t{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\t❌\t{host}/{hostname}\t{p}")
            if hostname == 'Google':
                print(f"{i}/{loops}\t{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\t❌\t{host}/{hostname}\t\t{p}")

            log_message(f"\n{datetime.now().strftime('%H:%M:%S')}\t❌\t{host}/{hostname}: {p}")

        time.sleep(ping_wait)

    print()

log_message(f"\n\n---------- STOPPED {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
