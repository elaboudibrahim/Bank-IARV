from . import Assistant


def afficherSolde(nf):
    file=open("files/users/"+nf+".txt",'r')
    info=file.readline()
    solde=info.split("**")
    print("vote solde  : "+ str(solde[1]))
    file.close()

def transfereArgent(ref):
    ref2=input("entrez le reference du compte que vous voulez transferer l'argent \n")
    montant = float(input("entrez le montant que vous voulez transferer \n"))
    nf=Assistant.trouverCompte(ref)
    Assistant.reduitSolde(nf, montant)
    refCompte=Assistant.trouverCompte(ref2)
    Assistant.augmenterSolde(refCompte, montant)
    Assistant.enregistrer_operation(ref,ref2,montant,"virement")
    Assistant.enregistrer_operation(ref2,ref,montant,"reception")

