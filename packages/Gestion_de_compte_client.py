from . import Assistant
from . import Gestion_de_connexion
import os
def ajouter_clients():
    Gestion_de_connexion.creerCompte()

def supprimer_client():
    try:
        f=open("files/creerCompte.txt",'r')
        data=f.readlines()
        email=input('Emial  de client que vous voulez suprimer\n')
        d_compte=""
        for i in range(len(data)):
            print(i)
            d_compte = data[i].strip().split("**")
            if (d_compte[2] == email):
                data.remove(data[i])
                break
        f2=open("files/creerCompte.txt",'w')
        f2.writelines(data)
        f2.close()


        try:
            compte = str(str(d_compte[0]) + str(d_compte[2]))
            chemin = "files/users/" + str(compte) + ".txt"
            os.remove(chemin)
        except:
            print("le fichier user" + str(d_compte[0]) + str(d_compte[2]) + " invalide")
        try:
            compte = str(str(d_compte[0]) + str(d_compte[2]))
            chemin = "files/users/facture/" + str(compte) + ".txt"
            os.remove(chemin)
        except:
            print("le fichier facture " + str(d_compte[0]) + str(d_compte[2]) + " invalide")
    except:
        print("quelque chose n'est pas correct. ")


def afficher_All():
    Assistant.afficher_All()

def ajouter_facture():
    try:
        email=input('Email  de client \n')
        compte=Assistant.trouverCompte(email)
        f=open("files/users/facture/"+str(compte)+".txt","a")
        type=input("entrez type de facture \n")
        montant=input("entrez le montatn \n")
        ligne=str(type)+"**"+str(montant)+"\n"
        f.writelines(ligne)
        f.close()
    except:
        print("email invalide \n")


def approuver_credit():
    try:
        f = open("files/demandeCredit.txt", 'r')
        data=f.readlines()
        print("les listes de credits \n-----------------------------------------" )
        for d in data:
            res=d.split("**")
            print("idClient  {}  montant  :{}".format(res[0],res[1]))

        c=input("a pour approuver  \ns pour supprimer\n")
        choix = input("entrez idClient \n")

        if c=='a':
            #approuver
            for d,i in zip(data,range(len(data))):
                res=d.rstrip().split("**")
                if choix==res[0]:
                    compte=Assistant.trouverCompte(res[0])
                    solde=Assistant.lire_solde(compte)
                    solde+=float(res[1])
                    f=open("files/users/"+str(compte)+".txt", 'r')
                    soldeClient=f.readlines()
                    soldeClient[0]=str("Solde :**")+str(solde)+"\n"
                    f.close()
                    f=open("files/users/"+str(compte)+".txt", 'w')
                    f.writelines(soldeClient)
                    #supprimer le ligne courant

                    data.pop(i)
                    f.close()
                    f = open("files/demandeCredit.txt", 'w')
                    f.writelines(data)
                    break

        if c=="s":
            #supprimer
            for d, i in zip(data, range(len(data))):
                res = d.rstrip().split("**")
                if choix == res[0]:
                    data.pop(i)
                    f.close()
                    f = open("files/demandeCredit.txt", 'w')
                    f.writelines(data)
                    break
    except:
        print("quelque chose n'est pas correct. ")
