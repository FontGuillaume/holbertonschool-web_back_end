#!/usr/bin/env python3
import time
wait_n = __import__('1-concurrent_coroutines').wait_n
def measure_time(n: int, max_delay: int) -> float:
    wait_n(n, max_delay)
    return time.time() % n

    
