import psutil
import time

while True:
    cpu_percent = psutil.cpu_percent()
    print("CPU usage: {}%".format(cpu_percent))
    time.sleep(10)