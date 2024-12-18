#Créer une application graphique qui permet de vérifier la validité d'un mot de passe entré par l'utilisatteur 
from tkinter import *
from tkinter.ttk import *  #importe les widgets améliorés
from tkinter.messagebox import *  #Importe les boîtes de dialogues

#Création de la fonction de vérification


def verification():
    nomUtilisateur = zoneSaisieDuNom.get()
    prenomUtilisateur = zoneSaisieDuPrenom.get()
    motDePasseUtilisateur = zoneDeSaisieMotDePasse.get()
    listeDeMotsDePasseValide = ["admin123", "user456" , "guest789"]
    global nombreDeTentative
    nombreDeTentative =0

    if not nomUtilisateur.isalpha or not prenomUtilisateur.isalpha :
        showerror("Erreur" , "Valeur du Nom ou Prénom d'utilisateur Incorrecte!")
        raise Exception("Mauvaise Saisie !")
    
    if motDePasseUtilisateur == "" and nomUtilisateur.isalpha and prenomUtilisateur.isalpha:
        showwarning("Avertissement", f"{nomUtilisateur},\nVeuillez Saisir votre mot de passe")
        raise Exception("Veuillez Saisir votre mot de passe")
    
    if nomUtilisateur.isalpha  and  prenomUtilisateur.isalpha  and  motDePasseUtilisateur!="":
        while motDePasseUtilisateur not in listeDeMotsDePasseValide:
            print(f"{nomUtilisateur} , votre accès est refusé.")
            askretrycancel("Avertissement" , f"{nomUtilisateur}\nVotre Accès est refusé\nIl vous reste 2 tentatives")
            nombreDeTentative=+1
            
            if nombreDeTentative ==3 :
                print("Trop de tentatives. Accès vérrouillé")
                showerror("Erreur" , f"{nomUtilisateur}\nVous avez eu 3 tentatives.\nVotre Accès est vérrouillé ")
                break
              
        else:
           print("Accès autorisé.")
           showinfo("Succès" , "Accès Autorisé")
            
    

#Création de la fonction qui supprime les zones de saisies
def supression():
    zoneSaisieDuNom.delete(first=0)
    zoneSaisieDuPrenom.delete(first=0)
    zoneDeSaisieMotDePasse.delete(first=0)

#Création de la fenêtre principale
fenetre = Tk()

#Configuration de la fenêtre principale
fenetre.title("Password Validator")  #Titre de la fenêtre principale
fenetre.geometry("650x500")  #Taille de la fenêtre principale
fenetre.resizable(width=True , height=True)  #Redimensionnage de la fenêtre principale

#Ajout des Widgets
labelNomUtilisateur = Label(fenetre , text="Nom* :" , font="Arial")
labelNomUtilisateur.place_configure(x=100 , y=50)
zoneSaisieDuNom = Entry(fenetre, font="Arial"  , width=35)
zoneSaisieDuNom.place(x=220 , y= 46 , height=30 )

labelPrenomUtilisateur = Label(fenetre , text="Prénoms* : " , font="Arial")
labelPrenomUtilisateur.place_configure( x=100 , y=150)
zoneSaisieDuPrenom = Entry(fenetre , font="Arial" , width=35)
zoneSaisieDuPrenom.place_configure(x=220 , y= 147, height=30)


labelMotDePasse = Label(fenetre , text="Mot de Passe*: " , font="Arial")
labelMotDePasse.place_configure(x=100 , y=250 )
zoneDeSaisieMotDePasse = Entry(fenetre, font="Arial" , width=35)
zoneDeSaisieMotDePasse.place_configure(x=220 , y=248, height=30 )




#Ajout des Boutons DE Validation et d'Annulation
boutonValider = Button(fenetre, text="Valider", command=verification)
boutonValider.place_configure(x=220 , y=350)

boutonAnnuler = Button(fenetre, text="Annuler", command=supression)
boutonAnnuler.place_configure(x=400, y=350)






#Affichage de la fenêtre principale
fenetre.mainloop()