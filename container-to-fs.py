
import subprocess
import time
import uuid

while True:
    unique_filename = str(uuid.uuid4())
    command = "docker cp e8b8adc61dd4:/C:/NaosRestServer/logs/naos.log C:/naos_logs/naos.log_" + \
        str(time.time()).split('.')[1]+".txt"
    subprocess.call(command, shell=True)
    time.sleep(10)
