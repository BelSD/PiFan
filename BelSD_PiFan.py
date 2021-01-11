#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2005-2021 BelSD - Jean-Pierre Waldorf
#
# Raspberry Temperature PiFan Control
# 
# Version : 0.2.0
#

from time import sleep
from gpiozero import OutputDevice
from termcolor import colored, cprint

STARTING = True
FAN_ON = 65   # Température d'activation du/des ventilateur(s) (en degrés Celcius).
FAN_OFF = 55  # Température de déactivation du/des ventilateur(s) (en degrés Celcius).
WAIT = 5      # Fréquence de mesure de la température (en secondes).
GPIO_PIN = 14 # GPIO où est branché le contrôleur du/des ventilateur(s)

def read_temp():
    # 
    # Lecture de la température du processeur en millièmes de degrés Celcius
    #
    with open('/sys/class/thermal/thermal_zone0/temp') as READ_CPU_TEMP:
        CPU_TEMP = READ_CPU_TEMP.read()

    try:
        return int(CPU_TEMP) / 1000
    except (IndexError, ValueError,) as ERROR_STR:
        raise RuntimeError('Impossible d\'analyser la sortie de température.') from ERROR_STR

if __name__ == '__main__':
    if STARTING == True:
        print ('[', colored('  OK  ', 'green'),']', ' Started', colored(' BelSD PiFan Control.', 'white'))
    # Valider les seuils d'activation et de désactivation
    if FAN_OFF >= FAN_ON:
        raise RuntimeError('FAN_OFF doit-être inférieur à FAN_ON')

    fan = OutputDevice(GPIO_PIN)

    while True:
        CPU_TEMPERATURE = read_temp()
        # Active le(s) ventilateur(s) si le seuil de température est atteint
        # et qu'il(s) n'est/ne sont pas déjà activé(s)
        # NOTE: `fan.value` retourne 1 pour "on" et 0 pour "off"
        if CPU_TEMPERATURE > FAN_ON and not fan.value:
            fan.on()
        # Arrête le(s) ventilateur(s) si la température est en dessous su seuil de température
        elif fan.value and CPU_TEMPERATURE < FAN_OFF:
            fan.off()

        sleep(WAIT)