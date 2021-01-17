# BelSD PiFan Control
## Pour 2 ventilateurs sur un Pi 400

![image1](https://github.com/BelSD/Pifan/blob/master/images/1.jpg)
![image2](https://github.com/BelSD/Pifan/blob/master/images/2.jpg)
![image4](https://github.com/BelSD/Pifan/blob/master/images/4.jpg)

1. Fichiers pour l'impression 3D

Les fichiers sont sur [Cults3D](https://cults3d.com/fr/mod%C3%A8le-3d/divers/pi-400-cooling)

2. Plan de branchement

* Composants :

- 1x Transistor PNP BD140
- 1x Transistor NPN S8050
- 1x Résistance 47 Ohm
- 2x Résistance 220 Ohm

![Plan](https://github.com/BelSD/Pifan/blob/master/images/PI400-Fan.png)

3. Installation


Le moyen le plus simple d'installer le script du contrôleur de ventilateurs est d'utiliser le script d'installation. 
Pour ce faire, connectez-vous en SSH à votre Pi et clonez le référentiel: 

```
git clone https://github.com/BelSD/Pifan.git
```
Si vous n'avez pas encore installé git, vous devrez d'abord installer git en utilisant

```
sudo apt-get install git
```

Allez dans le répertoire Pifan

```
cd Pifan
```

Exécutez le fichier d'installation

```
bash install.sh
```

Ce script installe BelSD_PiFan.py ce qui surveille la température centrale et contrôle le ventilateur. 
En outre, il ajoute un script appelé BelSD_PiFan.sh à /etc/init.d et configure le script à exécuter lorsque le système démarre.

il vous suffit plus qu'à redémarrer votre RPI pour que le programme démarre.
```
sudo reboot
```

4. Personnalisation

Le script est conçu de telle façon que les ventilateurs tournent toujours en vitesse réduite
et dès que la température de 65°C du CPU est atteinte, ceux-ci se mettent à tourner à pleine puissance
jusqu'à ce que la température du CPU sois redescendue à 55°C.

Si vous souhaitez modifier ces paramètres, alors éditez le fichier source :

```
sudo nano /usr/local/bin/BelSD_PiFan.py
```

Et modifier les valeurs de FAN_ON et FAN_OFF
* ATTENTION
FAN_OFF doit être inférieur à FAN_ON

Le code est conçus de telle façon que dès que vous avez sauvegarder les paramètres,
ceux-ci sont pris en considération en un laps de temps de maximum 5 secondes.
