# VERIFICATION FR (FRANCAIS)
def verificationFR(tab):
    for i in range(len(tab)):
        print(str(i)+" - " + tab[i] + " sera supprimé.")
    
    if(len(tab)>0):
        print("Indiquez l'ensemble des fichiers à NE PAS supprimer (Format : 0,3,7,9)  (Ne rien indiquer pour ignorer) : ")
        reponse = input()

        if reponse != "":
            reponse = reponse.split(",")
            try:
                reponse = [int(i) for i in reponse]
            except:
                print("ERREUR : Veuillez indiquer des chiffres séparés par une virgule.")
                print("")
                print("")
                return verificationFR(tab)
            reponse.sort(reverse=True)
            for i in reponse:
                tab.pop(i)
        return tab

# SUPPRIMER FR (FRANCAIS)
def supprimerFR(tab):
    try:
        for cheminFichier in tab:
            try:
                os.unlink(cheminFichier)
            except Exception as e:
                print("Erreur lors de la suppression du fichier " + cheminFichier + ": " + str(e))
            print(f"Le fichier {cheminFichier} a été supprimé avec succès.")
    except Exception as e:
        print("AUCUN FICHIER A SUPPRIMER")

# VERIFICATION EN (ENGLISH)
def verificationEN(tab):
    for i in range(len(tab)):
        print(str(i)+" - " + tab[i] + " will be deleted.")
    
    if(len(tab)>0):
        print("Indicate all the files NOT to delete (Format : 0,3,7,9)  (Leave blank to ignore) : ")
        reponse = input()

        if reponse != "":
            reponse = reponse.split(",")
            try:
                reponse = [int(i) for i in reponse]
            except:
                print("ERROR : Please indicate numbers separated by a comma.")
                print("")
                print("")
                return verificationEN(tab)
            reponse.sort(reverse=True)
            for i in reponse:
                tab.pop(i)
        return tab
    
# SUPPRIMER EN (ENGLISH)
def supprimerEN(tab):
    try:
        for cheminFichier in tab:
            try:
                os.unlink(cheminFichier)
            except Exception as e:
                print("Error while deleting the file " + cheminFichier + ": " + str(e))
            print(f"The file {cheminFichier} has been deleted successfully.")
    except Exception as e:
        print("NO FILE TO DELETE")  


####################################################################################################



lang = ""

while(lang != "fr" and lang != "en"):
    lang = input("Enter the language (fr/en) : ")



####################################################################################################


if(lang == "fr"):
    print("""
    #########################################
    #                                       #
    #   Supprimer des fichiers par filtre   #
    #                                       #
    #########################################
        """)

    extension = -1
    termine_par = -1
    contient = -1

    while ((extension == -1 or "." not in extension) and extension != ""):
        extension = str(input("Entrez l'extension du fichier à supprimer (Ne rien indiquer pour ignorer) : "))

    while (termine_par == -1):
        termine_par = str(input("Entrez le terme qui termine le nom du fichier à supprimer (Ne rien indiquer pour ignorer) : "))

    while (contient == -1):
        contient = str(input("Entrez le terme qui doit être contenu dans le nom du fichier à supprimer (Ne rien indiquer pour ignorer) : "))

    if extension == "":
        extension = None
    if termine_par == "":
        termine_par = None
    if contient == "":
        contient = None



    import os
    import sys
    import time

    # Obtenir le chemin du répertoire du fichier
    path = os.path.dirname(os.path.realpath(sys.argv[0]))
    tab = []

    # Parcourir tous les fichiers du répertoire
    for fichier in os.listdir(path):
        cheminFichier = os.path.join(path, fichier)
        try:
            nomFichier = os.path.basename(cheminFichier)

            split = nomFichier.split(".")
            if len(split) > 1:
                for i in range(len(split) - 1):
                    if i == 0:
                        nomFichier = split[i]
                    else:
                        nomFichier = nomFichier + "." + split[i]
            else:
                nomFichier = split[0]


            if ((os.path.isfile(cheminFichier)) and (extension is None or fichier.endswith(extension)) and (termine_par is None or nomFichier.endswith(termine_par)) and (contient is None or contient in fichier)) and (nomFichier != "remover"):
                tab.append(cheminFichier) 
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier {cheminFichier}: UNKOWN ERROR")

    print("""
        #########################################
        #                                       #
        #   CHARGEMENT EN COURS DES FICHIERS    #
        #                                       #
        #########################################
            """)

    print("...")
    time.sleep(1)
    print("Par Lucien")
    time.sleep(1)
    print("...")
    time.sleep(1)

    tab = verificationFR(tab)
    supprimerFR(tab)
    time.sleep(1)
    input("Appuyez sur une touche pour quitter le programme...")







####################################################################################################


if(lang == "en"):
    print("""
    #########################################
    #                                       #
    #   Remove files by filter              #
    #                                       #
    #########################################
        """)

    extension = -1
    termine_par = -1
    contient = -1

    while ((extension == -1 or "." not in extension) and extension != ""):
        extension = str(input("Enter the file extension to delete (Leave blank to ignore) : "))

    while (termine_par == -1):
        termine_par = str(input("Enter the term that ends the name of the file to delete (Leave blank to ignore) : "))

    while (contient == -1):
        contient = str(input("Enter the term that must be contained in the name of the file to delete (Leave blank to ignore) : "))

    if extension == "":
        extension = None
    if termine_par == "":
        termine_par = None
    if contient == "":
        contient = None



    import os
    import sys
    import time

    # Get the path of the file directory
    path = os.path.dirname(os.path.realpath(sys.argv[0]))
    tab = []

    # Browse all files in the directory
    for fichier in os.listdir(path):
        cheminFichier = os.path.join(path, fichier)
        try:
            nomFichier = os.path.basename(cheminFichier)

            split = nomFichier.split(".")
            if len(split) > 1:
                for i in range(len(split) - 1):
                    if i == 0:
                        nomFichier = split[i]
                    else:
                        nomFichier = nomFichier + "." + split[i]
            else:
                nomFichier = split[0]


            if ((os.path.isfile(cheminFichier)) and (extension is None or fichier.endswith(extension)) and (termine_par is None or nomFichier.endswith(termine_par)) and (contient is None or contient in fichier)) and (nomFichier != "remover"):
                tab.append(cheminFichier) 
        except Exception as e:
            print(f"Error reading file {cheminFichier}: UNKOWN ERROR")

    print("""
        #########################################
        #                                       #
        #   LOADING FILES IN PROGRESS           #
        #                                       #
        #########################################
            """)

    print("...")
    time.sleep(1)
    print("By Lucien")
    time.sleep(1)
    print("...")
    time.sleep(1)
    tab = verificationEN(tab)
    supprimerEN(tab)
    time.sleep(1)
    input("Press any key to exit the program...")