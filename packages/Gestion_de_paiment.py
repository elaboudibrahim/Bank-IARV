from . import Assistant

def afficher_facture(ref):

    compte=Assistant.trouverCompte(ref)
    file = open("files/users/facture/" + str(compte) + ".txt", 'r')
    data = file.readlines()
    print("debut----------------------------------------------------------")
    print("vous avez ", len(data), " facture à regler\n")
    print("----------------------------------------------------------")

    try:
        for i,j in zip(data, range(len(data))):
            facture=i.split("**")
            print(str(j+1) + ")-- type de facture :  " + facture[0] + " montant "  + facture[1] + "\n")
    except:
            print("fin----------------------------------------------------------")



def paiment_facture(ref,num):
    compte=Assistant.trouverCompte(ref)
    file = open("files/users/facture/" + str(compte) + ".txt", 'r')
    data = file.readlines()
    for i in range(len(data)):
        if i+1 == num:
            facture=data[i].split("**")
            try:
                Assistant.reduitSolde(compte, float(facture[1]))
                data.pop(i)
                file2 = open("files/users/facture/" + str(compte) + ".txt", 'w')
                file2.writelines(data)
                print("paiment succes  de la facture : ", facture[0] ," \n")
            except:
                print("vérifier votre solde \n")
