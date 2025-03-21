""" 
Téléchargement & Installation  de la bibliothèque regex sur la console par la commande : pip install regex
qui permet de  prendre en compte les caractères Unicode, 
y compris les caractères accentués et les caractères spéciaux de différentes langues
"""
#NB: Les modules re et regex fonctionnent différemment 

from regex import * #Importation du Module regex dans le code
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showerror, showinfo, showwarning
from PIL import Image , ImageTk  # Importation de la Bibliothèque pillow pour insérer les images dans la fenêtre
import time


# Variable globale pour suivre les tentatives
tentatives = 0
verrouille_jusqua = 0
verrouillage_duree = 5 * 60  #05 minutes en secondes

# Fonction qui valide les noms saisis
def validerNom(nom):
    # Autorise les tirets, les lettres et les espaces
    pattern = r"^[\p{L}][\p{L}\s\-]*$"  # pareil avec pattern = r"^[\p{L}\s\-]+$"
    return bool(search(pattern, nom))

# Création de la fonction de vérification
def verification():
    global tentatives, verrouille_jusqua  # les VARIABLEs tentative et verrouille_jusqua sont des variables globales
    nomUtilisateur = zoneSaisieDuNom.get()
    prenomUtilisateur = zoneSaisieDuPrenom.get()
    motDePasseUtilisateur = zoneDeSaisieMotDePasse.get()
    listeDeMotsDePasseValide = ["admin123", "user456", "guest789"]

    if not validerNom(nomUtilisateur) or not validerNom(prenomUtilisateur):  # Si les champs de saisie du nom & prenoms sont vides
        showwarning("AVERTISSEMENT", "Veuillez remplir le champ de saisie!")
        return

    if not motDePasseUtilisateur:  #Si le champ de sasie du mot de passe  est vide
        showwarning("Avertissement", f"{nomUtilisateur},\nVeuillez saisir votre mot de passe.")
        return

    if motDePasseUtilisateur in listeDeMotsDePasseValide:  #Si le mot de passe saisi se trouve dans la liste des mots de passe valides 
        showinfo("Succès", "Accès autorisé.")
        reset_tentatives()
    else:
        tentatives += 1
        if tentatives >= 3:
            showerror("Erreur", "Nombre de tentatives dépassé, Accès verrouillé")
            verrouille_jusqua = time.time() + verrouillage_duree
            bouton_valider.config(state=DISABLED)   #Désactivation du bouton Valider 
            bouton_annuler.config(state=DISABLED)   #Desactivation du bouton Annuler
            fenetre.after(1000, verifier_verrouillage)
            zoneDeSaisieMotDePasse.delete(0, END)      #Effacement de la zone de saisie du mot de passe 
        else:
            showwarning("Erreur", f"Mot de passe incorrect.\n{nomUtilisateur} il vous reste {3 - tentatives} Tentatives")
            zoneDeSaisieMotDePasse.delete(0, END)

def validerNom(nom):
    # Autorise les tirets, les lettres et les espaces
    pattern = r"^[\p{L}][\p{L}\s\-]*$"  # pareil avec pattern = r"^[\p{L}\s\-]+$"
    return bool(search(pattern, nom))

# Création de la fonction de vérification
def alter_verification(event):
    verification()


# Fonction pour réinitialiser le compteur de tentatives
def reset_tentatives():
    global tentatives
    tentatives = 0
    zoneSaisieDuNom.delete(0, END)  # Pour supprimer d'un coup tout le contenu de la zone de nom (Du début à la fin)
    zoneSaisieDuPrenom.delete(0, END)  # Pour supprimer d'un coup tout le contenu de la zone de prenom (Du début à la fin)
    zoneDeSaisieMotDePasse.delete(0, END)  # Pour supprimer d'un coup tout le contenu de la zone de mot de passe (Du début à la fin)

# Fonction pour vérifier si le verrouillage est terminé
def verifier_verrouillage():
    if time.time() >= verrouille_jusqua:
        bouton_valider.config(state=NORMAL)  
        bouton_annuler.config(state=NORMAL)
        reset_tentatives()
    else:
        fenetre.after(1000, verifier_verrouillage)

# Création de la fonction qui supprime les zones de saisie
def suppression():
    reset_tentatives()

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Password Validator")
fenetre.geometry("750x500")
fenetre.resizable(width=False, height=False)
fenetre.config(background="navy")  # couleur de la fenêtre d'arrière plan

# Charger l'image pour l'icône de la fenêtre
icon_path = "C:/Users/lenovo/Desktop/MyApps/projet_passwordValidator/connexion_small.png" 
icon_image = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_image)
fenetre.iconphoto(False, icon_photo)

# Ajout des Widgets
Label(fenetre, text="Nom* :", font="Arial").place(x=100, y=50)
zoneSaisieDuNom = Entry(fenetre, font="Arial", width=35)
zoneSaisieDuNom.place(x=280, y=46, height=30)
zoneSaisieDuNom.bind('<Return>' , alter_verification)  #Permettre à ce que le code s'execute suite à l'appui sur la touche Enter du  clavier

Label(fenetre, text="Prénoms* :", font="Arial").place(x=100, y=150)
zoneSaisieDuPrenom = Entry(fenetre, font="Arial", width=35)
zoneSaisieDuPrenom.place(x=280, y=147, height=30)
zoneSaisieDuPrenom.bind('<Return>' , alter_verification)  #Permettre à ce que le code s'execute suite à l'appui sur la touche Enter du  clavier

Label(fenetre, text="Mot de Passe* :", font="Arial").place(x=100, y=250)
zoneDeSaisieMotDePasse = Entry(fenetre, font="Arial", width=35, show="*")
zoneDeSaisieMotDePasse.place(x=280, y=248, height=30)
zoneDeSaisieMotDePasse.bind('<Return>' , alter_verification)   #Permettre à ce que le code s'execute suite à l'appui sur la touche Enter du  clavier

Label(fenetre, text="*Champs de saisie Obligatoires", foreground="red").place(x=280, y=300)

# Ajout des Boutons
bouton_valider = Button(fenetre, text="Valider", command=verification)
bouton_valider.place(x=280, y=350)


bouton_annuler = Button(fenetre, text="Annuler", command=suppression)
bouton_annuler.place(x=450, y=350)

# Affichage de la fenêtre principale
fenetre.mainloop()
