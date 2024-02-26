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
            print("fin-----------------------------------------------------------")
