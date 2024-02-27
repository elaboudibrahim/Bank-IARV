from . import Information_bancaire


def simulateur_credit():
    credit_souhaite = float(input("Entrez le credit souhaite\n"))
    nbrMois = int(input("Entrez nbr de mois\n"))

    montant_retourner = credit_souhaite + (credit_souhaite * Information_bancaire.taux_interer()) / 100
    print('montant retourner {}'.format(montant_retourner))


def demande_credit(ref):
    credit_souhaite = float(input("Entrez le credit souhaite\n"))
    nbrMois = int(input("Entrez nbr de mois\n"))

    montant_retourner = credit_souhaite + (credit_souhaite * Information_bancaire.taux_interer()) / 100
    print('montant retourner {}'.format(montant_retourner))

    verifaication = input("si vous etes d accord ecrit  oui sinon ecrit non\n")
    if verifaication == "oui":
        f = open("files/demandeCredit.txt", 'a')
        f.writelines(str(ref) + "**" + str(credit_souhaite) + "\n")
        f.close()
        print("votre demandeCredit est entrin de traiter")
    else:
        print("vous etes pauvre ../\..")
