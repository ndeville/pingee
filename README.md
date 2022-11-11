# pingee

Internet Connection Monitoring Script

Last update: 11th Nov '22

## Speed Test

: currently using the `speedtest-cli` Python library, looping download tests.

Variables:   

``` python
tests_to_run = 3
threads = 1 # 1 simulates a typical file transfer, else None
log_file = '/path/to/log.csv'
```

prints as:   

``` zsh
Starting speed test with 3 runs (threads=1)...

#1 [10:19:44] 60.85 Mbit/s (11.3s test time)
#2 [10:19:55] 72.8 Mbit/s (11.3s test time)
#3 [10:20:06] 25.89 Mbit/s (11.4s test time)
```

and logs to CSV file.  

## Ping Test

Next step:  

script for ping test, using `ping3` Python library - see `ping_test.py`.    