import threading
import time

def task(name):
    print(f"Thread {name} started")
    time.sleep(2)
    print(f"Thread {name} finished")

threads = []

for i in range(3):
    t = threading.Thread(target=task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads finished")