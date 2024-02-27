from packages import Gestion_de_connexion
from packages import Gestion_de_transaction
from packages import Assistant
from packages import Gestion_de_paiment
from packages import Gestion_de_compte
from packages import Gestion_de_compte_client
from packages import Simulateur_d_credit


choix=int(input("pour cree compte choisi 1 \npour connecter chosi 2 \n"))



if choix==1:
    Gestion_de_connexion.creerCompte()
elif choix==2:
    ref=Gestion_de_connexion.connexion()
    #res[0] + res[2]
    connexion_etablie=Assistant.trouverCompte(ref)

    try:
        role = Assistant.retournerRole(ref)
    except:
        role = "USER"

    if connexion_etablie != "":
        if role == str("ADMIN"):
            choix = int(input("1 gestion de transaction\n2 gestion de paiment\n"
                              "3 gestion de compte\n4 demander credit\n"
                              "5 gestion des comptes de client\n"
                              ))
        else:
            choix = int(input("1 gestion de transaction\n2 gestion de paiment\n3 gestion de compte\n"
                              "4 demander credit\n"))

        if choix == 1:
            choix = int(input("1 pour afficher solde \n2 pour transferer l'argent\n3 pour afficher les historiques\n"))
            if choix == 1:
                Gestion_de_transaction.afficherSolde(connexion_etablie)
            elif choix == 2 :
                Gestion_de_transaction.transfereArgent(ref)
            elif choix == 3 :
                Gestion_de_transaction.afficher_historique(connexion_etablie)
        if choix == 2:
            choix=int(input("1 pour afficher\n2 pour paiment\n"))
            if choix == 1:
                Gestion_de_paiment.afficher_facture(ref)
            elif choix == 2:
                num=int(input("entrez num de facture \n"))
                Gestion_de_paiment.paiment_facture(ref,num)
        if choix == 3:
            choix = int(input("1 pour afficher les informations \n2 pour modifier les informations\n"))
            if choix == 1:
                Gestion_de_compte.afficher_les_informations(ref)
            elif choix == 2:
                Gestion_de_compte.modifier_les_informations(ref)
        if choix == 4:
            choix = int(input("1 simulez credit \n2 demander credit\n"))
            if choix == 1:
                Simulateur_d_credit.simulateur_credit()
            elif choix == 2:
                Simulateur_d_credit.demande_credit(ref)
        if choix == 5 and role == "ADMIN":
            choix = int(input("1 afficher tous les client\n2 ajouter client\n"
                              "3 suprimmer client\n4 ajouter facture à un client\n"
                              "5 approuver credit"))
            if choix == 1:
                Gestion_de_compte_client.afficher_All()
            if choix == 2:
                Gestion_de_compte_client.ajouter_clients()
            if choix == 3:
                Gestion_de_compte_client.supprimer_client()
            if choix == 4:
                Gestion_de_compte_client.ajouter_facture()
            if choix == 5:
                Gestion_de_compte_client.approuver_credit()