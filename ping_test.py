### Testing best approach for a continuous ping test to monitor connectivity

from datetime import datetime
print("----------")

print()

hostnames = {
            '208.67.222.222': 'OpenDNS', # OpenDNS
            '208.67.220.220': 'OpenDNS', # OpenDNS  
            '1.1.1.1': 'Cloudflare', # Cloudflare
            '1.0.0.1': 'Cloudflare', # Cloudflare
            '8.8.8.8': 'Google', # Google
            '8.8.4.4': 'Google', # Google
}

# import socket
# import time
# import datetime
# import os
# import sys
    
# LOG_FNAME = "network.log"

# FILE = os.path.join(os.getcwd(), LOG_FNAME)

# def send_ping_request(host="1.1.1.1", port=53, timeout=3):
#     try:
#         socket.setdefaulttimeout(timeout)
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.connect((host,port))
#     except OSError as error:
#         return False
#     else:
#         s.close()
#         return True

# def write_permission_check():
#     try:
#         with open(FILE, "a") as file:
#             pass
#     except OSError as error:
#         print("Log file creation failed")
#         sys.exit()
#     finally:
#         pass

# def calculate_time(start, stop):
#     time_difference = stop - start
#     seconds = float(str(time_difference.total_seconds()))
#     return str(datetime.timedelta(seconds=seconds)).split(".")[0]

# def mon_net_connection(ping_freq=2):
#     monitor_start_time = datetime.datetime.now()
#     motd = "Network connection monitoring started at: " + str(monitor_start_time).split(".")[0] + " Sending ping request in " + str(ping_freq) + " seconds"
#     print(motd)
    
#     with open(FILE, "a") as file:
#         file.write("\n")
#         file.write(motd + "\n")
#     while True:
#         if send_ping_request():
#             time.sleep(ping_freq)
#         else:
#             down_time = datetime.datetime.now()
#             fail_msg = "Network Connection Unavailable at: " + str(down_time).split(".")[0]
#             print(fail_msg)
#             with open(FILE, "a") as file:
#                 file.write(fail_msg + "\n")
#                 i = 0
#             while not send_ping_request():
#                 time.sleep(1)
#                 i += 1
#                 if i >= 3600:
#                     i = 0
#                     now = datetime.datetime.now()
#                     continous_message = "Network Unavailabilty Persistent at: " + str(now).split(".")[0]
#                     print(continous_message)
#                     with open(FILE, "a") as file:
#                         file.write(continous_message + "\n")
#             up_time = datetime.datetime.now()
#             uptime_message = "Network Connectivity Restored at: " + str(up_time).split(".")[0]
    
#             down_time = calculate_time(down_time, up_time)
#             _m = "Network Connection was Unavailable for " + down_time
    
#             print(uptime_message)
#             print(_m)
    
#             with open(FILE, "a") as file:
#                 file.write(uptime_message + "\n")
#                 file.write(_m + "\n")
                
# mon_net_connection()




# import socket

# socket.setdefaulttimeout(3)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("1.1.1.1",53))
# s.close()



# print("\n" * 3)

# import subprocess

# # Internal ping
# print(f"INTERNAL PING:\n")

# router = '192.168.1.1'

# router_command = ['ping', '-c', '1', router]

# router_ping = subprocess.call(router_command)

# print(f"\n{router_ping=}\n")

# # External ping
# print(f"EXTERNAL PING:\n")



# for hostname in hostnames:

#     hostname_command = ['ping', '-c', '1', hostname]

#     external_ping = subprocess.call(hostname_command)

#     print(f"\n{external_ping=}\n")

# print("\n" * 3)



### Test with pythonping

# import os
# print(os.getenv("USER"))
# print(os.getenv("SUDO_USER"))


# from pythonping import ping

# ping('1.1.1.1', verbose=True)

# needs to be run with sudo on CLI

### Test with ping3

from ping3 import ping, verbose_ping
import time

run_time = 24 # in hours, as integer
log_file = '/Users/nic/Python/pingee/log/log.txt'

def log_message(s):
    global log_file
    with open(log_file, 'a') as file:
        file.write(s)

loops = int((run_time * 60 * 60) / len(hostnames))
print(f"\nRunning {loops} loops...\n")

# with open(log_file, 'a') as file:
#     file.write(f"\n\n---------- STARTING {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
log_message(f"\n\n---------- STARTING {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

for i in range(0,loops): # 14400 seconds in 24h

    for host,hostname in hostnames.items():
        p = ping(host)
        # print(f"\n{p=}")
        if p != None:
            p_format = round(p*1000, 2)   

            if hostname == 'OpenDNS':
                print(f"{i}/{loops}\t{datetime.now().strftime('%H:%M:%S')}\t✅\t{host}/{hostname}\t{p_format}ms")
            if hostname == 'Cloudflare':
                print(f"{i}/{loops}\t{datetime.now().strftime('%H:%M:%S')}\t✅\t{host}/{hostname}\t{p_format}ms")
            if hostname == 'Google':
                print(f"{i}/{loops}\t{datetime.now().strftime('%H:%M:%S')}\t✅\t{host}/{hostname}\t\t{p_format}ms")

        else:
            p = '-'
            if hostname == 'OpenDNS':
                print(f"{i}/{loops} {datetime.now().strftime('%H:%M:%S')}\t❌\t{host}/{hostname}\t{p}")
            if hostname == 'Cloudflare':
                print(f"{i}/{loops} {datetime.now().strftime('%H:%M:%S')}\t❌\t{host}/{hostname}\t{p}")
            if hostname == 'Google':
                print(f"{i}/{loops} {datetime.now().strftime('%H:%M:%S')}\t❌\t{host}/{hostname}\t\t{p}")

            log_message(f"\n{datetime.now().strftime('%H:%M:%S')}\t❌\t{host}/{hostname}: {p}")

        time.sleep(1)

    print()

# with open(log_file, 'a') as file:
#     file.write(f"\n---------- STOPPED {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
log_message(f"\n\n---------- STOPPED {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

print()
print()