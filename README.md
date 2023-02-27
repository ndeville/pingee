# pingee - Internet Connection Monitoring Script


## ping_test

Working (basic) script for monitoring internet connection.  

Can be run for a specified amount of time, looping hosts to ping every x seconds.  
Logs ping errors to a `txt` file.  

I use it mainly as needed for quick checks, launching the script via a keyboard shortcut.   

Variables:   

``` python
run_time = 24 # in hours, as integer

ping_wait = 1 # in seconds, as integer

log_file = '/path/to/log/file.txt'

hostnames = {
            '208.67.222.222': 'OpenDNS', # OpenDNS
            '208.67.220.220': 'OpenDNS', # OpenDNS  
            '1.1.1.1': 'Cloudflare', # Cloudflare
            '1.0.0.1': 'Cloudflare', # Cloudflare
            '8.8.8.8': 'Google', # Google
            '8.8.4.4': 'Google', # Google
}
```

prints as:   

``` shell
Running 14400 loops...

0/14400 17:46:42        ✅      208.67.222.222/OpenDNS  22.01ms
0/14400 17:46:43        ✅      208.67.220.220/OpenDNS  23.97ms
0/14400 17:46:44        ✅      1.1.1.1/Cloudflare      20.11ms
0/14400 17:46:45        ✅      1.0.0.1/Cloudflare      23.05ms
0/14400 17:46:46        ✅      8.8.8.8/Google          13.31ms
0/14400 17:46:47        ✅      8.8.4.4/Google          15.93ms

1/14400 17:46:48        ✅      208.67.222.222/OpenDNS  21.93ms
1/14400 17:46:49        ✅      208.67.220.220/OpenDNS  19.6ms
1/14400 17:46:50        ✅      1.1.1.1/Cloudflare      25.94ms
1/14400 17:46:51        ✅      1.0.0.1/Cloudflare      19.57ms
1/14400 17:46:52        ✅      8.8.8.8/Google          16.17ms
1/14400 17:46:53        ✅      8.8.4.4/Google          17.55ms
```


## speedtest

Using the `speedtest-cli` Python library, looping download tests.   

Variables:   

``` python
tests_to_run = 3
threads = 1 # 1 simulates a typical file transfer, else None
log_file = '/path/to/log.csv'
```

prints as:   

``` shell
Starting speed test with 3 runs (threads=1)...

#1 [10:19:44] 60.85 Mbit/s (11.3s test time)
#2 [10:19:55] 72.8 Mbit/s (11.3s test time)
#3 [10:20:06] 25.89 Mbit/s (11.4s test time)
```

and logs to CSV file.    