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

IP_ROUTER = os.getenv("IP_ROUTER")
IP_SWITCH = os.getenv("IP_SWITCH")
IP_OFFICE = os.getenv("IP_OFFICE")
IP_KELLER = os.getenv("IP_KELLER")
IP_EG = os.getenv("IP_EG")
IP_DACH_LR = os.getenv("IP_DACH-LR")

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
# SCRIPT_TITLE

### Script-specific imports



### Global Variables



### Functions

# ssh ubnt@192.168.237

# info


# ### Main


# import paramiko

# router_ip = "172.16.1.100"
# router_username = "admin"
# router_password = "admin"

# ssh = paramiko.SSHClient()

# # Load SSH host keys.
# ssh.load_system_host_keys()
# # Add SSH host key automatically if needed.
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # Connect to router using username/password authentication.
# ssh.connect(router_ip, 
#             username=router_username, 
#             password=router_password,
#             look_for_keys=False )

# # Run command.
# ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f"ssh ubnt@{IP_DACH_LR}")

# output = ssh_stdout.readlines()
# # Close connection.
# ssh.close()

# # Analyze show ip route output
# for line in output:
#     if "0.0.0.0/0" in line:
#         print("Found default route:")
#         print(line)


# import os
# from fabric import Connection, task

# def deploy(ctx):
#     with Connection(
#         os.environ["HOST"],
#         user="USERNAME",
#         connect_kwargs={"key_filename": os.environ["DEPLOY_KEY_FILE"]},
#     ) as c:
#         with c.cd("/home/project/path/"):
#             c.run("docker-compose down")
#             c.run("git pull origin master --recurse-submodules --rebase")
#             c.run("docker-compose up --build -d")



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