import time
import matplotlib.pyplot as plt
from functools import lru_cache

timings = []


# Timer decorator
def timer(func):
    def wrapper(*args, **kwargs):
        global timings
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        execution_time = end - start  # Convert to seconds
        timings.append(execution_time)
        print(f"Finished in {execution_time:.10f} s: f({args[0]}) -> {result}")
        return result

    return wrapper


# Fibonacci function with memoization and the timer decorator
@lru_cache
@timer
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def graph():
    # Plotting the results
    plt.plot(timings)
    plt.title("Fibonacci Calculation Timings (in milliseconds)")
    plt.xlabel("n (Fibonacci sequence index)")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    fib(100)
    graph()
