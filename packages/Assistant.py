

def afficher_All():
    f = open("files/creerCompte.txt", "r")
    datas = f.readlines()
    for data,i in zip(datas,range(len(datas))):
        res = data.rstrip().split('**')
        try:
            print("{})- Nom: {}  Role: {}  Email: {}".format(i, res[0], res[3], res[2]))
        except IndexError:
            print("{})- Nom: {}  Email: {}".format(i, res[0], res[2]))




#augmenter le solde d'un client
def augmenterSolde(nf,montant):
    file = open("files/users/" + str(nf) + ".txt", 'r')
    data = file.readlines()
    solde = float(data[0].strip().split("**")[1])

    solde = solde + montant

    data[0] = "Solde :**" + str(solde) + "\n"
    file.close()
    file = open("files/users/" + str(nf) + ".txt", 'w')
    file.writelines(data)

    file.close()

#réduit le solde d'un client
def reduitSolde(nf,montant):
    file = open("files/users/" + str(nf) + ".txt", 'r')
    data = file.readlines()
    solde=float(data[0].strip().split("**")[1])
    if solde > montant:
        solde -= montant
    else:
        print("solde insufissant")
        return
    data[0] = str("Solde :**" + str(solde)+"\n")
    file.close()

    file = open("files/users/" + str(nf) + ".txt", 'w')
    file.writelines(data)

    file.close()