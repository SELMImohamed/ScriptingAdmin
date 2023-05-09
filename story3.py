import psutil
import time

# Ouverture du fichier de journal en mode ajout (append)
with open('system_log.txt', 'a') as file:
    # Boucle infinie pour collecter les données à intervalles différents
    while True:
        # Collecte des données du CPU toutes les 5 secondes
        cpu_usage = psutil.cpu_percent(interval=5)

        # Collecte des données de la mémoire toutes les 30 secondes
        memory_usage = psutil.virtual_memory().percent
        if time.time() % 30 == 0:
            # Obtention de l'heure actuelle
            timestamp = int(time.time())
            # Création de la chaîne de caractères à enregistrer dans le fichier journal
            log_string = f'{timestamp},"Usage mémoire " {memory_usage}\n'
            # Enregistrement de la chaîne de caractères dans le fichier journal
            file.write(log_string)

        # Collecte des données du disque toutes les 15 secondes
        disk_usage = psutil.disk_usage('/').percent
        if time.time() % 15 == 0:
            # Obtention de l'heure actuelle
            timestamp = int(time.time())
            # Création de la chaîne de caractères à enregistrer dans le fichier journal
            log_string = f'{timestamp}, "Utilisation du disque "{disk_usage}\n'
            # Enregistrement de la chaîne de caractères dans le fichier journal
            file.write(log_string)

        # Obtention de l'heure actuelle
        timestamp = int(time.time())
        # Création de la chaîne de caractères à enregistrer dans le fichier journal
        log_string = f'{timestamp},"Usage du Cpu" {cpu_usage}\n'
        # Enregistrement de la chaîne de caractères dans le fichier journal
        file.write(log_string)
        time.sleep(5)