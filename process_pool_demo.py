from concurrent.futures import ProcessPoolExecutor
import time

def task(n):
    time.sleep(2)
    return f"Process {n} done"

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = executor.map(task, [1, 2, 3])

        for r in results:
            print(r)