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


def afficher_historique(nf):
    file=open("files/users/"+nf+".txt",'r')
    data=file.readlines()
    print("les operations que vous effectueez :\n")
    print("idRecp :\ttype d'op\t montant\t  date\t")
    for i in range(len(data)-1):
        #pour ignorer le premier ligne
        ligne=data[i+1].split("**")
        print(ligne[0]+"\t"+ligne[1]+'\t'+ligne[2]+'\t'+ligne[3])