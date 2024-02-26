from . import Assistant
import os

def afficher_les_informations(ref):
    f=open("files/creerCompte.txt",'r')
    data=f.readlines()

    for i in range(len(data)):
        d_compte=data[i].strip().split("**")

        if d_compte[2] == ref :
            print("votre nom :" + str(d_compte[0]))
            print("votre email : " + str(d_compte[2]))


def modifier_les_informations(ref):
    f=open("files/creerCompte.txt",'r')
    data = f.readlines()

    for i in range(len(data)):
        d_compte = data[i].strip().split("**")
        if (d_compte[2] == ref):
            print("email : " + str(d_compte[2])+"\n")
            choix = int(input(" 1 - pour chenger l'email \n 2- pour chenger password "))
            if choix == 1 :
                email= input("entrez un nouveau email \n")
                d_compte[2]=email

            if choix == 2:
                password = input("entrez un nouveau mot de passe \n")
                password2= input("repetez le mot de passe \n")
                if password == password2 :
                    d_compte[1] = password
            data[i]=str(d_compte[0])+ "**" +str(d_compte[1])+ "**" + str(d_compte[2])+ "\n"
            f2 = open("files/creerCompte.txt", 'w')
            f2.writelines(data)
            f2.close()



            try:
                 compte=str(str(d_compte[0])+str(ref))
                 chemin="files/users/"+str(compte)+".txt"

                 data2=""
                 try:
                     fille=open(chemin,'r')
                     data2=fille.readlines()
                     fille.close()
                     os.remove(chemin)
                 except:
                     print("le fichier user : " + chemin + " invalide")
                 new_fille = open("files/users/" + str(d_compte[0])+str(d_compte[2]) + ".txt", "w")
                 new_fille.writelines(data2)
                 new_fille.close()
            except:
                print("le fichier user"+str(d_compte[0])+str(d_compte[2])+" invalide")

             #effectuer des modifications sur  et facture

            try:
                compte = str(str(d_compte[0]) + str(ref))
                data_facture=""
                try:
                    chemin = "files/users/facture/" + str(compte) + ".txt"
                    fille = open(chemin, 'r')
                    data_facture = fille.readlines()
                    fille.close()
                    os.remove(chemin)
                except:
                    print("le fichier facture : " + chemin + " invalide")

                new_fille = open("files/users/facture/" + str(d_compte[0])+str(d_compte[2]) + ".txt", "w")
                new_fille.writelines(data_facture)
            except:
                print("le fichier facture dans le nom : "+ str(d_compte[0])+str(d_compte[2]) +" invalide")

            break
