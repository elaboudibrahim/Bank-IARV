
def creerCompte():
    f=open("files/creerCompte.txt",'a')
    Name=input(    "\t\t\t\t* entrez votre nom       * \n")
    password=input("\t\t\t\t* entrez votre password  * \n")
    email=input(   "\t\t\t\t* entrez votre email     * \n")
    f.write(Name + '**' + password + '**' + email +"**USER"+ '\n')
    f2=open("files/users/"+Name+email+".txt",'w')
    f2.write("Solde :**" + '0.0')
    f2.close()
    f.close()
def connexion():
    f = open("files/creerCompte.txt", "r")
    email = input(   "\t\t\t\t* - entrez votre email    * \n")
    password = input("\t\t\t\t* - entrez votre password * \n")
    datas = f.readlines()
    for data in datas:
        res=data.strip().split('**')
        if email == res[2] and password==res[1]:
                return res[2]
    return "f"


# with open("zoo.txt", 'r') as filin:
#      lignes = filin.readlines()
#      for ligne in lignes:
#         print(ligne)


# f = open("files/creerCompte.txt", "r")
#     # password = input("entrez votre password \n")
#     # email = input("entrez votre email \n")
#     data = f.readlines()
#     print(data)