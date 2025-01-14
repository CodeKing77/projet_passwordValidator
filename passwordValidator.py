""" 
Téléchargement & Installation la bibliothèque regex sur la console par la commande : pip install regex
qui permet de  prendre en compte les caractères Unicode, 
y compris les caractères accentués et les caractères spéciaux de différentes langues
"""
from regex import *  #Puis Importation du Module regex dans le code
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showerror, showinfo, showwarning

# Variable globale pour suivre les tentatives
tentatives = 0


#Fonction  qui valide les noms saisis
def validerNom(nom):
    #Autorise les tirets, les lettres et les espaces
    pattern = r"^[\p{L}][\p{L}\s\-]*$" #  pareil avec pattern = r"^[\p{L}\s\-]+$"
    return bool(search(pattern, nom))



# Création de la fonction de vérification
def verification():
    global tentatives
    nomUtilisateur = zoneSaisieDuNom.get()
    prenomUtilisateur = zoneSaisieDuPrenom.get()
    motDePasseUtilisateur = zoneDeSaisieMotDePasse.get()
    listeDeMotsDePasseValide = ["admin123", "user456", "guest789"]

    if not validerNom(nomUtilisateur) or not validerNom(prenomUtilisateur):
        showerror("Erreur", "Valeur du Nom ou Prénom d'utilisateur incorrecte!")
        return

    if motDePasseUtilisateur == "":
        showwarning("Avertissement", f"{nomUtilisateur},\nVeuillez saisir votre mot de passe.")
        return

    if motDePasseUtilisateur in listeDeMotsDePasseValide:
        showinfo("Succès", "Accès autorisé.")
        reset_tentatives()
    else:
        #global tentatives
        tentatives += 1
        if tentatives >= 3:
            showerror("Erreur", "Nombre de tentative dépassé, Accès verrouillé")
            reset_tentatives()
        else:
            showwarning("Erreur", f"Mot de passe incorrect.\n{nomUtilisateur} il vous reste {3 - tentatives} Tentatives  ")
            zoneDeSaisieMotDePasse.delete(0, END)

# Fonction pour réinitialiser le compteur de tentatives
def reset_tentatives():
    global tentatives
    tentatives = 0
    zoneSaisieDuNom.delete(0, END)  #Pour supprimer d'un coup tout le contenu de la zone de nom (Du début à la fin)
    zoneSaisieDuPrenom.delete(0, END)  #Pour supprimer d'un coup tout le contenu de la zone de prenom (Du début à la fin)
    zoneDeSaisieMotDePasse.delete(0, END)  #Pour supprimer d'un coup  tout le contenu de la zone de mot de passe (Du début à la fin)

# Création de la fonction qui supprime les zones de saisie
def supression():
    reset_tentatives()

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Password Validator")
fenetre.geometry("650x500")
fenetre.resizable(width=False, height=False)
fenetre.config(background="navy")  #couleur de la fenêtre d'arrière plan 

# Ajout des Widgets
Label(fenetre, text="Nom* :", font="Arial").place(x=100, y=50)
zoneSaisieDuNom = Entry(fenetre, font="Arial", width=35)
zoneSaisieDuNom.place(x=220, y=46, height=30)

Label(fenetre, text="Prénoms* :", font="Arial").place(x=100, y=150)
zoneSaisieDuPrenom = Entry(fenetre, font="Arial", width=35)
zoneSaisieDuPrenom.place(x=220, y=147, height=30)

Label(fenetre, text="Mot de Passe* :", font="Arial").place(x=100, y=250)
zoneDeSaisieMotDePasse = Entry(fenetre, font="Arial", width=35, show="*")
zoneDeSaisieMotDePasse.place(x=220, y=248, height=30)

Label(fenetre, text="*Champs de saisie Obligatoires", foreground="red").place(x=220 , y=300)

# Ajout des Boutons
Button(fenetre, text="Valider", command=verification).place(x=220, y=350)
Button(fenetre, text="Annuler", command=supression).place(x=400, y=350)

# Affichage de la fenêtre principale
fenetre.mainloop()
