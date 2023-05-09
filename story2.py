import psutil
import time
import datetime
# Ouverture du fichier de journal en mode ajout (append)
with open('log.txt', 'a') as file:
    # Boucle infinie pour collecter les données toutes les 15 secondes
    while True:
        cpu_usage = psutil.cpu_percent()
        timestamp = int(time.time())
        date = datetime.datetime.fromtimestamp(timestamp)
        log_string = f'{timestamp},{date} {cpu_usage}\n'
        file.write(log_string)
        time.sleep(10)
