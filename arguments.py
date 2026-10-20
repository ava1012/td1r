#! /usr/bin/env python3

"""Programme affichant les arguments qui lui sont fournis ainsi que leur indice si la variable d'environnement `DEBUG` est définie sur le shell. 
- Ce programme doit afficher un message d'erreur et renvoyer le code d'erreur 1 si aucun argument n'est fourni.
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant."""
import os 
import sys
def arguments():
    """Fonction qui affiche les arguments de la ligne de commande."""
    arguments = sys.argv[1:]
    if not arguments:
        print(f"Erreur : aucun argument fourni. \nUsage : {sys.argv[0]} arg1 [arg2...]", file=sys.stderr)
        return 1 
    debug = "DEBUG" in os.environ
    for indice, argument in enumerate(arguments, start = 1):
        if debug:
            print(f"{indice}:{argument}")
        else:
            print(argument)
    return 0

if __name__ == "__main__":
    arguments()         
