from packages import Gestion_de_compte_client
from packages import Assistant
import os
from packages import Simulateur_d_credit

#Simulateur_d_credit.demande_credit("e")


#Gestion_de_compte_client.approuver_credit()


# try:
#     print("1")
#     compte = Assistant.trouverCompte(ref)
#     print("2")
#     chemin = "files/users/" + str(compte) + ".txt"
#     print("3")
#
#     data2 = ""
#     try:
#         fille = open(chemin, 'r')
#         data2 = fille.readlines()
#         fille.close()
#         os.remove(chemin)
#     except:
#         print("le fichier user" + chemin + " invalide")
#     print("3")
#     new_fille = open("files/users/" + str(d_compte[0]) + str(d_compte[2]) + ".txt", "w")
#     print("4")
#     new_fille.writelines(data2)
#     print("5")
#     new_fille.close()
# except:
#     print("le fichier user" + str(d_compte[0]) + str(d_compte[2]) + " invalide")
#
# # effectuer des modifications sur  et facture
#
# try:
#     compte = Assistant.trouverCompte(ref)
#     data_facture = ""
#     try:
#         chemin = "files/users/facture/" + str(compte) + ".txt"
#         fille = open(chemin, 'r')
#         data_facture = fille.readlines()
#         fille.close()
#         os.remove(chemin)
#     except:
#         print("le fichier facture" + chemin + " invalide")
#
#     new_fille = open("files/users/facture/" + str(d_compte[0]) + str(d_compte[2]) + ".txt", "w")
#     new_fille.writelines(data_facture)
# except:
#     print("le fichier facture" + str(d_compte[0]) + str(d_compte[2]) + " invalide")
#
# break
