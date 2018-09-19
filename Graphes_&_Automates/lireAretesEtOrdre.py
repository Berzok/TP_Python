def lireAretesEtOrdre(nomdufichier):
    """lit le fichier et renvoie la liste des aretes qui s'y trouvent
    ainsi que l'ordre"""
    f = file(nomdufichier, 'r')
    lignes = f.readlines()
    #on extrait les lignes qui commencent par 'E' 
    #si c'est bon on cree une nouvelle arete
    aretes = []
    ordre = 0
    for l in lignes:
        mots = l.split()
        if len(mots) >= 3 and mots[0]=='E':
            aretes.append([int(mots[1]), int(mots[2])])  #ATTENTION ne pas oublier la conversion str en int
        if len(mots) > 0 and mots[0]=="ordre":
            ordre = int(mots[1])
    return aretes, ordre
