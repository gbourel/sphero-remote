# remote

Page de connexion à distance pour TP avec Sphero.

## Description

Un élève connecté à l'ENT peut envoyer son programme vers le robot Sphero.

### Commandes

 * **connect** : connection bluetooth au robot e
 t renvoi un objet robot Sphero
 *  **Sphero.set_rgb_led(int : r, int : g, int : b)** : allume les LEDs principales avec la couleur choisie. Chaque composante est codée sur un octet \[0-255\].
 * **Sphero.move(int : direction)** : déplacement à vitesse constante (50) dans la direction donnée \[0-359\].
 * **Sphero.roll(int : direction, int : speed)** : déplacement à vitesse choisie \[0-255\] dans la direction donnée \[0-359\].
 * **Sphero.wait(int : duree)** : attente en secondes

### Version

* v0.1.0 initialisation.

## Développement

Page HTML basique, pour tester

`npm start`


## TODO

 * static check python program on send (client side)
 * feedback for python running error
 * sensors values as CSV
 * sensors values as graph
 * handle bluetooth connection error in bluetooth server

