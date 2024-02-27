from datetime import datetime

#construire une date courant
def date():
    maintenant = datetime.now()
    annee = maintenant.year
    mois = maintenant.month
    jour = maintenant.day
    heure = maintenant.hour
    minute = maintenant.minute
    seconde = maintenant.second
    date=str(annee)+":"+str(mois)+":"+str(jour)+" "+str(heure)+":"+str(minute)+":"+str(seconde)
    return date

#retourne le nom du fichier à un client spécifier
def trouverCompte(email):
    f = open("files/creerCompte.txt", "r")
    datas=f.readlines()
    for data in datas:
        res=data.strip().split('**')
        if email == res[2]:
            return res[0]+res[2]

def retournerRole(email):
    f = open("files/creerCompte.txt", "r")
    datas = f.readlines()
    for data in datas:
        res = data.strip().split('**')
        if email == res[2]:
            try :
                return str(res[3])
            except:
                return "USER"

#retouner le dolde d'un client
def lire_solde(nf):
    file = open("files/users/" + nf + ".txt", 'r')
    ligne = file.readline()
    solde = float(ligne.strip().split("**")[1])
    return solde
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

def enregistrer_operation(ref,idRecepteru,montant,typeOp):
    nomFichier=trouverCompte(ref)
    dateCourant=date()
    file = open("files/users/" + nomFichier + ".txt","a")
    file.write(idRecepteru + '**' +str(typeOp)+ "**" +str(montant) + "**" + dateCourant + "\n")

def afficher_All():
    f = open("files/creerCompte.txt", "r")
    datas = f.readlines()
    for data,i in zip(datas,range(len(datas))):
        res = data.rstrip().split('**')
        try:
            print("{})- Nom: {}  Role: {}  Email: {}".format(i, res[0], res[3], res[2]))
        except IndexError:
            print("{})- Nom: {}  Email: {}".format(i, res[0], res[2]))