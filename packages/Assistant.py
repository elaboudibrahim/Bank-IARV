

def afficher_All():
    f = open("files/creerCompte.txt", "r")
    datas = f.readlines()
    for data,i in zip(datas,range(len(datas))):
        res = data.rstrip().split('**')
        try:
            print("{})- Nom: {}  Role: {}  Email: {}".format(i, res[0], res[3], res[2]))
        except IndexError:
            print("{})- Nom: {}  Email: {}".format(i, res[0], res[2]))