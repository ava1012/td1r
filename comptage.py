#! /usr/bin/env python3

"""Programme permettant de lire un fichier et d'afficher ses caractéristiques principales.
- Le chemin du fichier à lire devra être fourni comme argument en ligne de commandes. 
- En absence d'argument, le programme lira les caractères fournis sur l'entrée standard. 
- Le programme doit afficher le nombre de caractères, de lignes et de mots du texte lu. Pour cela, vous devez utiliser la structure de contrôle match/case afin de discrimer la nature des caractères au fur et à mesure de leur lecture. 
- De façon à ne pas trop compliquer les traitements, on considérera qu'un mot est une séquence de caractères encadrée de séparateurs et dans un premier temps, seuls trois séparateurs seront pris en compte : le saut de ligne, l'espace et le caractère de tabulation ('\t')
- Votre programme devra proposer un mode de débogage affichant les numéros des mots détectés. 
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant."""
import os
import sys

def lire(argumentd):
    if len(arguments) > 1:
        chemin = arguments[1]
        try:
            with open(chemin, "r", encoding="utf-8") as flux:
                return flux.read()
        except OSError as erreur:
            print(f"Erreur : impossible de lire '{chemin}' ({erreur.sterror})", file=sys.stderr)
            return None 
    if sys.stdin.isatty():
        print("Saisissez votre texte (Ctrl + D pour terminer) :", file=sys.stderr)
    return sys.stdin.read()
def compter(texte, debug = False): 
    nb_caracteres = 0 
    nb_lignes = 0
    nb_mots = 0
    mot_courant = " "

    for caractere in texte : 
        nb_caracteres += 1 
        match caractere :
            case "\n"|" "| "\t":
                if caractere == "\n":
                    nb_lignes += 1
                if mot_courant:
                    if debug:
                        print(f"[debug] mot {nb_mots} : {mot_courant!r}", file = sys.stderr)
                        mot courant = " "
            case _:
                if not mot_courant: 
                    nb_mots += 1 
                    mot_courant += caractere 
    if mot_courant and debug:
        print(f"[debug] mot {nb_mots} : {mot_courant!r}", file=sys.stderr)
    return nb_caracteres, nb_lignes, nb_mots 

def main():
    texte = lire_texte(sys.argv)
    if texte is None:
        return 1
    caracteres, lignes, mots = compter(texte, debug = "DEBUG" in os.environ)
    print(f"Caracteres : {caracteres}")
    print(f"Lignes : {lignes}")
    print(f"Mots : {mots}")
    return 0

if __name__ == "__main__":
    lire()
