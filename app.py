import time
import sys
import os
import itertools
from collections import deque

with open('Leboncoin_6_9.log.txt') as file:

    # Récupérer dans une variable, dans le nom du fichier, le 6_9

    filename = file.name
    FindExecutionHour = filename.find('6_9')  # renvoi 10
    FileExecutionHour = filename[10:13]

    # Rechercher dans les 5 premieres lignes la ligne "INITIALISATION : leboncoin 95 at : 04:09:42.806197" , on récupère le 95, qui correspond au numéro de département concerné
    # Toujours dans la même ligne : récupérer l'heure d'execution
    for line in itertools.islice(file, 0, 5):
        if line.startswith('INITIALISATION'):
            line.find('95')  # 27
            line.find('04')  # 35
            departmentNumber = line[27:29]
            executionHour = line[35:50]

# On recherche dans les 15 dernières lignes du fichier une heure, si dispo on le stock dans une variable

    fichier = deque(file, maxlen=15)
    for ligne in fichier:
        if ligne.startswith('END'):
            date = ligne[6:21]
            print(date)
