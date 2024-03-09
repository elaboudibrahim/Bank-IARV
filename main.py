from packages import Gestion_de_connexion
from packages import Gestion_de_transaction
from packages import Assistant
from packages import Gestion_de_paiment
from packages import Gestion_de_compte
from packages import Gestion_de_compte_client
from packages import Simulateur_d_credit

print("\n\n\t\t\t Bienvenue dans BRAHIM-MOUATAZ BANK\n"
      "\t\t\t      --(its 7alal no taxe)-- \n")
choix=int(input("\t\t\t***********************************\n"
                "\t\t\t *\tpour cree compte choisi  1   *\n"
                "\t\t\t *\t\t\t\t\t\t\t\t *\n"
                "\t\t\t *\tpour connecter chosi     2   *\n"
                "\t\t\t***********************************\n"))



if choix==1:
    Gestion_de_connexion.creerCompte()
elif choix==2:
    t = 0
    while (t < 3):
        ref=Gestion_de_connexion.connexion()
        #res[0] + res[2]
        connexion_etablie=Assistant.trouverCompte(ref)
        if ref == "f":
            print("--------------Vérifier le mot de pass ou l'email---------------")
        t += 1
        try:
            role = Assistant.retournerRole(ref)
        except:
            role = "USER"
        if ref != "f":
            test=True
            while(test):
                if role == str("ADMIN"):
                    choix = int(input("\t\t\t\t----------------------------------------------\n"
                                      "\t\t\t\t1  gestion de transaction         \t\t\t--\n"
                                      "\t\t\t\t2  gestion de paiment             \t\t\t--\n"
                                      "\t\t\t\t3  gestion de compte              \t\t\t--\n"
                                      "\t\t\t\t4  demander credit                \t\t\t--\n"
                                      "\t\t\t\t5  gestion des comptes de client  \t\t\t--\n"
                                      "\t\t\t\t99 pour deconnecter               \t\t\t--\n"
                                      "\t\t\t\t----------------------------------------------\n"
                                      ))
                else:
                    choix = int(input("\t\t\t\t------------------------------------------\n"
                                      "\t\t\t\t1--- gestion de transaction \t\t\t--\n"
                                      "\t\t\t\t2--- gestion de paiment     \t\t\t--\n"
                                      "\t\t\t\t3--- gestion de compte      \t\t\t--\n"
                                      "\t\t\t\t4--- demander credit        \t\t\t--\n"
                                      "\t\t\t\t99-- pour deconnecter       \t\t\t--\n"
                                      "\t\t\t\t------------------------------------------\n"))

                if choix == 1:
                    choix = int(input("\t\t\t\t------------------------------------------\n"
                                      "\t\t\t\t 1 - pour afficher solde          \n"
                                      "\t\t\t\t 2 - pour transferer l'argent     \n"
                                      "\t\t\t\t 3 - pour afficher les historiques \n"
                                      "\t\t\t\t------------------------------------------\n"))
                    if choix == 1:
                        Gestion_de_transaction.afficherSolde(connexion_etablie)
                    elif choix == 2 :
                        Gestion_de_transaction.transfereArgent(ref)
                    elif choix == 3 :
                        Gestion_de_transaction.afficher_historique(connexion_etablie)
                if choix == 2:
                    choix=int(input("\t\t\t\t** 1 pour afficher  *\n"
                                    "\t\t\t\t** 2 pour paiment   *\n"))
                    if choix == 1:
                        Gestion_de_paiment.afficher_facture(ref)
                    elif choix == 2:
                        num=int(input("\t\t\t\t** entrez num de facture \n"))
                        Gestion_de_paiment.paiment_facture(ref,num)
                if choix == 3:
                    choix = int(input("\t\t\t\t**---------------------------------**\n"
                                      "\t\t\t\t *1 pour afficher les informations * \n"
                                      "\t\t\t\t *                                 * \n"
                                      "\t\t\t\t *2 pour modifier les informations * \n"
                                      "\t\t\t\t**---------------------------------**\n"))
                    if choix == 1:
                        Gestion_de_compte.afficher_les_informations(ref)
                    elif choix == 2:
                        Gestion_de_compte.modifier_les_informations(ref)
                if choix == 4:
                    choix = int(input("\t\t\t\t**------------------**\n"
                                      "\t\t\t\t * 1 simulez credit  * \n"
                                      "\t\t\t\t *                   * \n"
                                      "\t\t\t\t * 2 demander credit * \n"
                                      "\t\t\t\t**------------------**\n"))
                    if choix == 1:
                        Simulateur_d_credit.simulateur_credit()
                    elif choix == 2:
                        Simulateur_d_credit.demande_credit(ref)
                if choix == 5 and role == "ADMIN":
                    choix = int(input("\t\t\t\t**-------------------------------**\n"
                                      "\t\t\t\t* 1 afficher tous les client      *\n"
                                      "\t\t\t\t* 2 ajouter client                *\n"
                                      "\t\t\t\t* 3 suprimmer client              *\n"
                                      "\t\t\t\t* 4 ajouter facture à un client   *\n"
                                      "\t\t\t\t* 5 approuver credit              *\n"
                                      "\t\t\t\t**-------------------------------**\n"))
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
                if choix == 99:
                    test=False