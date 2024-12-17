import time
import random

porte = r'''          ---   .    ____        -----      ______   -----        .
  ___     / \             .....................      ____   / \
        .`   `.  --  ..:::::`````````````````:::::..      .`   `.
  ---   | ^ ^ |    .::::````          (_     ````::::. -- | ^ ^ `
        | ^ ^ |  .::``                       _)    ``::.  | ^ ^ | --
____     `...`  .::`              .-.      (_        `::.  `...`
        .-.!_  .::`       _)     /   \                `::.   ! ____
       / / `-`.:`                `-.-`            _)    `:..```.
 --    ` |  `.|:`      _)         .`.       (_          `:/` |  \
       | |   |`.               _/^---^\_                  |     . --
 ___    \ .  `|               \-------../         (_      \   `.`
        ` :   `        _)      `.\:::/.`       (_   )_    |`   || ___
        | |  .|      _(         | | |`|                   / ` . |
    --  | `. | \                `.\ /.`                   `.  | |--
        |`.   `|                 |[ ]|           (_       | .`  |____
__    .`\ |  .`\                 `.^.`                    \ |.  .
     .`-.\`. | |        _)        (:)                     | ||| |
   .`    \`..` .             _..--```--.._      (_       /`-._.-`| ---
   |       `-..`.         .-`             `-.           |      .-`.
    \            `-.    .`  ..            .. `.        .`-._.-`    `.
--   )              `-./    `::.        .::`   \   _.-`             /
     `._/-..          /       `::.    .::`      \-`              .-`
         ::.`-.      ``        `::   ::`        ``       _..-\_.`
         :::   `._   | \         `   `         / |    .-`   .:: _____
____     :::      `-.|  `  .----..___..----.  `  | .-`      :::
         :::          \ |  _..--.     .--.._  | /-`         ::: ---
         :::   _)     | ` /     |     |     \ ` |  (        :::
   --    :::          )   |   _.`     `._   |   (   )_      :::____
    ____ :::          /`. \_.`   )\ /(   `._/ .`\     (_    :::
         :::       .-`|  `  -->-@ /     \ @->--`  |-.         :::
         :::    .-`   \         | / \ |         /  `-.      :::  ---
 ----    `` _.-`       |        )/   \(        |      `-.   :::  _____
  _.-=--..-`          . \ /\               /\ /          `-. ``
 /.._    `.        .-`   .\ `-.\.\\.//./.-` /.`-.           `---.._
|    `.    \    .-`      | `.             .` |   `-.                \ 
 \    _\.   `.-`         |   `-././.\.\.-`   |      `.               |
  `.-`  |   /::::::::::: \                   /::::::::`.      ,-.    /
 - |   /   /        ----  `-.             .-`     ----  `.    |  \_.`
__ \   | .`     _____        `-._._._._.-`     ____      |    |   |
    `--`                                                 `-.  `._ / --
                                                            `...-`'''
coffres = r"""
                 .--------------------------------...          .--------------------------------...
               ,'-------------------------------,'   |       ,'-------------------------------,'   |
              /                                /     |      /                                /     |
             /________________________________/    ,'|     /________________________________/    ,'|
             |               ..               |  ,'  |     |               ..               |  ,'  |
             |___________-==/88\==-___________|,' /) |     |___________-==/88\==-___________|,' /) |.
             |  \    \     ((  ))     /    /  |  (/  |-. . |  \    \     ((  ))     /    /  |  (/  |-. .
             |   \    \     \{}/     /    /   |    .' .  . |   \    \     \{}/     /    /   |    .' .  .
          . '|    \    \     )(     / _  /    |    ,   .  .|    \    \     )(     / _  /    |    ,   .  .
         . . |\    \    \    \/    _.( ~-.   /|\ ,' .   . .|    \    \    \/    _.( ~-.    /|\ ,' .   . .
       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   . .  |_-.--.______..._____( ,/  ` \~-.|,' .   .
        .  `    .     .       .  ,'\. ~-  . , .  .  .   .   .  `    .     .       .  ,'\. ~-  . , .  .  .   .
           .  `   .     ,   .      , ~~-.' .  .    .         .  `   .     ,   .      , ~~-.' .  .    .     """
sphinx = r"""
                              .sSSSSSSSs
                              sSS=""^^^"s
                  /\       , /  \_\_\|_/_)
                 /';;     /| \\\/.-. .-./
                / \;|    /. \,S'  -   - |
               / -.;|    | '.SS     _|  ;
              ; '-.;\,   |'-.SS\   __  /S
              | _  ';\\.  \' SSS\_____/SS
              |  '- ';\\.  \_SSS[_____]SS
              \ '--.-';;-. __SSS/\    SSS
               \  .--' ';;'.=SSS`\\_\_SSS
                `._ .-'` _';;..=.=.=.\.=\
                   ;-._-'  _.;\.=.=.=.|.=|
         ,     _.-'    `"=._  ;\=.=__/__/
         )\ .'`   __        ".;|.=.=.=./
         (_\   .-`  '.   |    \/=.=.=/`
          /\\         \-,|     |.--'|
         /  \`,       //  \    | |  |
        ( (__) )  _.-'--,  \   | |  '--,
         ;----' -'--,__}}}  \  '--, __}}}
         \_________}}}       \___}}}
  """

gargouille = r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡀⠀⠙⢶⣦⣤⠀⠀⡀⢀⠀⠀⣤⣴⡶⠋⠀⢀⣄⠀⠀⠀⠀⠀
⠀⠀⢀⣠⡾⠋⠙⠷⣤⡀⠛⠋⣠⣿⣇⣸⣿⣄⠙⠛⢀⣤⠾⠋⠙⢷⣄⡀⠀⠀
⠀⠀⣾⢋⣠⣶⠀⣦⣄⠙⠃⣸⣿⣿⣿⣿⣿⣿⣇⠘⠋⣠⣴⠀⣶⣄⡙⣷⠀⠀
⠀⢸⣿⣿⣿⡟⢀⣿⣿⣿⠀⢿⣤⣈⡉⢉⣁⣤⡿⠀⣿⣿⣿⡀⢻⣿⣿⣿⡇⠀
⠀⢸⣿⣿⣿⣷⡾⠿⠿⠿⠓⠀⠛⠋⣁⣈⠙⠛⠀⠚⠿⠿⠿⢷⣾⣿⣿⣿⡇⠀
⠀⠘⣿⡟⠛⠟⠀⠀⠀⣴⣾⣿⣦⣈⣉⣉⣁⣴⣿⣷⣦⠀⠀⠀⠻⠛⢻⣿⠃⠀
⠀⠀⠹⠀⠀⠀⠀⠀⠀⢹⣿⣿⠛⣿⣿⣿⣿⠛⣿⣿⡏⠀⠀⠀⠀⠀⠀⠏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣴⡀⢻⣿⡆⢸⣿⣿⡇⢰⣿⡟⢀⣦⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⠈⣿⡇⠀⣭⣭⠀⢸⣿⠁⣾⣿⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⡇⢸⣿⠀⢻⡟⠀⣿⡇⢸⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⠘⣿⣇⠘⠃⣸⣿⠃⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣿⡄⢻⣿⡀⢀⣿⡟⢠⣿⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠐⠋⠛⠁⠼⢿⡇⢸⡿⠧⠈⠛⠙⠂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

sorcier = r"""
                    ____ 
                  .'* *.'
               __/_*_*(_
              / _______ \
             _\_)/___\(_/_ 
            / _((\- -/))_ \
            \ \())(-)(()/ /
             ' \(((()))/ '
            / ' \)).))/ ' \
           / _ \ - | - /_  \
          (   ( .;''';. .'  )
          _\"__ /    )\ __"/_
            \/  \   ' /  \/
             .'  '...' ' )
              / /  |  \ \
             / .   .   . \
            /   .     .   \
           /   /   |   \   \
         .'   /    b    '.  '.
     _.-'    /     Bb     '-. '-._ 
 _.-'       |      BBb       '-.  '-. 
(___________\____.dBBBb.________)____)"""



biblio_ascii = r"""   ____________________________________________________
  |____________________________________________________|
  | __     __   ____   ___ ||  ____    ____     _  __  |
  ||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | |
  ||==|^^||--| |=||=| |=*=||| |  | |  |=|=|| | |~||==| |
  ||  |F ||  | | || | | G |||-|  | |==| | ||-|-|~||__| |
  ||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_|
  ||_______________________||__________________________|
  | _____________________  ||      __   __  _  __    _ |
  ||=|=|=|=|=|=|=|=|=|=|=| __..\/ |  |_|  ||#||==|  / /|
  || | | | | | | | | | | |/\ \  \\|++|=|  || ||==| / / |
  ||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|
  |____________________ /\~()/()~//\ __________________|
  | __   __    _  _     \_  (_ .  _/ _    ___     _____|
  ||~~|_|..|__| || |_ _   \ //\\ /  |=|__|~|~|___| | | |
  ||--|+|^^|==|A||B| | |__/\ __ /\__| |==|*|C|+|+|=|=|=|
  ||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_|
  |_________________ _/    \/\/\/    \_ _______________|
  | _____   _   __  |/      \../      \|  __   __   ___|
  ||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-|||
  ||______||=|H|--| |\   \   o    /   /| |  |~|  | | |||
  ||______||_|_|__|_|_\   \  o   /   /_|_|__|_|__|_|_|||
  |_________ __________\___\____/___/___________ ______|
  |__    _  /    ________     ______           /| _ _ _|
  |\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%|
  | \/\ |D/  .//____//.//   /__/__/ (_)      /  ||=|=|=|
__|  \/\|/   /(____|/ //                    /  /||E|~|~|__
  |___\_/   /________//   ________         /  / ||_|_|_|
  |___ /   (|________/   |\_______\       /  /| |______|
      /                  \|________)     /  / | |
"""
carte = r"""
         +---+          
         |S  |            
         |  1|          
         +---+          
          | |           
          | |            
  +---+  +---+  +---+    
  |S  |--|S  |--|S  |    
  | 3 |--| 2 |--| 5 |    
  +---+  +---+  +---+    
   | |    | |            
   | |    | |      N       
  +---+  +---+   * ║ *         
  |S  |  |S  |  O══*══E           
  |  4|  |  6|   * ║ *       
  +---+  +---+     S      
"""




l_mots = [
    "l'homme", "homme", "humain", "être humain", "l'Homme", "Homme",
    "les humains", "l homme", "l'humain", "les êtres humains", "l'Être humain", "un homme",
    "des hommes", "un humain", "les hommes", "l’Homme", "hommes", "gens", "mâle", "l'individu",
    "individu", "personne", "le genre humain", "la personne humaine", "le mâle", "les personnes",
    "l’humanité", "l’être", "le sapiens", "les individus", "la figure humaine", "le peuple humain"
]


def wait_petits_points(n):
    time.sleep(n)
    for i in range(2):
        print(".", end="")
        time.sleep(n/2)
    print('.')
    time.sleep(n)








def rappel_trajet(n, trajet):
    if n > len(trajet) :
        print(f"erreur : trop loin !({len(trajet)} maximum)")
    else :
        for i in range(len(trajet)-1, len(trajet)-n-1, -1):
            print(trajet[i], end="")
            if i != len(trajet)-n :
                print(', ')
            

def jeu():
    #organisation des salles, 0 -> pas de chemin, nb -> destination salle n°nb
    #ordre -- > nsoe
    guide_dir = ["",  [0, 2, 0, 0], [1, 6, 3, 5], [0, 4, 0, 2 ], [3, 0, 0, 0], [0, 0, 2, 0], [2, 0, 0, 0]]
    trajet = []
    inventaire = []
    
    pv = 100
    salle = 1
    #s2         s4               s5          totem de bén.      coffres     s3bis
    has_fought, has_been_defied, has_solved, second_try_active, has_opened, has_found = False, False, False, False, False, None
    
    entree = input("Bienvenue au Jeu, veuillez séléctionner les options suivantes : \n\tJOUER (j) \n\tQUITTER (q)\n")
    
    if entree == "j" :
        print("Vous êtes un explorateur téméraire")
        time.sleep(1.5)
        print("Votre but ultime : acquérir le précieux artéfact légendaire")
        time.sleep(3)
        print("Lors d'une de vos explorations, vous tombez dans un trou")
        time.sleep(3)
        print("Vous voilà alors dans une chambre, éclairée par des crystaux magiques, offrant une atmosphère chaleureuse")
        time.sleep(3)
        print("Auriez-vous mis la main sur le trésor tant convoité ?")
        wait_petits_points(1.8)
        print('Vous êtes dans la salle n°1')
        Running = True
    elif entree == "q":
        Running = False
        print("A bientôt !")
    #pour skip le début
    elif entree == "skip":
        Running = True
    else :
        print('erreur : commande invalide, veuillez redémarrer le jeu')
        Running = False

    while Running :
        
        if pv <= 0 :
            print("Game Over!")
            Running = False
        
        print("Quelle action souhaitez-vous effectuer ? \nStatut (i), Rappel trajet (r), Se déplacer (d), Quitter (q)", end="")
        if 'Carte' in inventaire :
            print("ou encore consulter la Map (m).")
        entree = input()
        time.sleep(0.8)
        
        if entree == "i":
            print(f'Le contenu de votre inventaire est le suivant : {inventaire} et vous avez {pv} pv.')
            
        elif entree == 'm' and 'Carte' in inventaire :   
            print(carte, end="\n\n")
            print(f"Vous êtes actuellement dans la salle {salle}")
        
        elif entree == "r":
            rappel_trajet(int(input("De combien de trajets voulez_vous vous rappeller ?")), trajet)

        elif entree == "d":
            direction = input("Vers quelle direction souhaitez-vous vous diriger ? (n/s/o/e)")
            if direction not in 'nsoe':
                print("erreur : saisie erronée")
                continue
            direction = 'nsoe'.index(direction)            #pour obtenir un nombre -> guide_dir 
            if guide_dir[salle][direction] != 0 :
                destination = guide_dir[salle][direction]
                trajet.append(f"{salle} --> {destination}")
                salle = destination
                print(f'Vous entrez dans la salle n°{salle}')
                wait_petits_points(0.7)
            
            else : #si joueur met une direction invalide
                if "Totem de bénediction" not in inventaire :
                    print("Aïe, vous vous cognez contre un mur, -5 PV")
                    pv -= 5
                print("AIDE : les directions disponibles pour votre salle sont : ", end = '')
                for each in guide_dir[salle] :
                    if each != 0 :
                        print(' nsoe'[each], end='')
                print('\n')
                continue 
            
            
            if salle == 1 : #implique que joueur est parti et revenu de la salle
                print("Rien d'autre à voir que la trou par lequel vous êtes rentré, perçant le plafond..")
                
            elif salle == 2 :
                if not has_fought :
                    print(gargouille, end="\n\n")
                    print("Attention ! Un monstre vous attaque !\nPour le vaincre, vous devez réussir à le battre au Pierre-Feuille-Ciseau..")
                    
                    
                    


                    
                    time.sleep(1.5)
                    nb_monstre = random.randint(1,3)
                    display = ['pierre', 'feuille', 'ciseau'][nb_monstre - 1]
                    nb_perso = int(input("Pierre (1), Feuille (2) ou Ciseau (3) ?"))
                    if nb_perso not in [1,2,3] :
                        print("erreur : dernière chance, insérez un nombre entre 1 et 3")
                        nb_perso = int(input("Pierre (1), Feuille (2) ou Ciseau (3) ?"))
                    print(f'Le monstre a joué {display}, le gagnant est donc :', end=
                          "")
                    if nb_monstre == nb_perso :
                        print(" personne, puisque vous avez fait égalité\nIl vous laisse prendre la fuite..")
                        #has_fought reste False pour qu'il puisse se faire attaquer encore
                        
                    elif (nb_monstre == 1 and nb_perso == 3) or (nb_monstre == 2 and nb_perso == 1) or (nb_monstre ==3 and nb_perso == 2) :
                        print(" le monstre, vous perdez 50 pv, attention !")
                        if "Totem de bénediction" not in inventaire :
                            pv -= 50
                        else :
                            print('Mais le totem de bénediction réduit vos dégâts')
                            pv -= 25
                        has_fought = True
                    else :
                        print(" vous ! Vous récuperez une peau de gargouille !")
                        inventaire.append("Peau de gargouille")
                        has_fought = True
                        
                        
                else :
                    print("Des traces du combat antérieur sont présentes dans la salle")
                    
            elif salle == 3 :
                if not has_opened :
                    print(coffres, end="\n\n")
                    entree = input("En rentrant dans la salle, vous apercevez deux coffres en bois ancien\nL'un contient un totem de bénediction tandis que l'autre contient une malédiction ancienne, êtes-vous prêt à prendre ce risque ? (y/n)")
                    if entree == 'y':
                        wait_petits_points(1.2)
                        nb = random.randint(1,2)
                        if nb == 1 :
                            print("Hourrah, vous êtes tombés sur le totem de bénediction\nVous êtes désormais protégé de tout type de dégât à hauteur de 50 % et béneficiez d'un deuxième essai utilisable sur un des puzzles de ce donjon")
                            inventaire.append("Totem de bénediction")
                            second_try_active = True
                        else :
                            print("Oh non ! Vous êtes tombé sur la malédiction ancienne !\n Vous perdez 50% de vos pv actuels et ressuscitez la gargouille, si tuée")
                            has_fought = False
                            pv = pv // 2
                            inventaire.append("Malédiction ancienne")
                        
                    else :
                        print("Bon choix.. ou mauvais.. qui sait ?")
                    has_opened = True
                elif has_found == None :
                    print("Bizarre... Les deux coffres qui étaient présents dans la salle ont disparu,")
                    time.sleep(1.5)
                    print("Cependant, une impressionante mosaïque, jusqu'à présent cachée par le présentoir, brille de mille feux, attirant votre attention !")
                    time.sleep(1.5)
                    mot = "artefact"
                    guess = ""
                    guess_dis = ["_", "_", "_","_", "_", "_", "_", "_"]
                    print("Sur la mosaïque, un clavier de lettres de l'alphabet, de A à Z, surmonté d'une sorte d'afficheur antique..")
                    time.sleep(0.3)
                    print("On dirait que vous avez affaire à un jeu du pendu !")
                    comp = 1
                    while comp < 11 and not has_found:
                        print()
                        print("".join(guess_dis))
                        saisie = str(input("Saisir une lettre ou un mot\t"))
                        if len(saisie) == 1 and saisie.lower() in mot :
                            print("Super, elle est dans le mot")
                            guess += saisie
                        elif len(saisie)> 1 and saisie.lower() == mot :
                            guess = saisie
                        else :
                            print(f'Aïe, plus que {11-comp} essais !')
                            comp += 1
                        for u in range(len(mot)) :
                            for i in range(len(guess)):
                                if mot[u] == guess[i]:
                                    guess_dis[u] = mot[u]
                            has_found = "".join(guess_dis) == mot
                        
                        
                    if  has_found :
                        #récompense blabla
                        print("Bravo !! vous avez résolu l'énigme")
                        print("Vous remportez une carte du donjon !")
                        inventaire.append("Carte")
                    else :
                        #perdu blablaa
                        has_found = False
                        print("Dommage..")
                        if second_try_active :
                            print("Mais votre totem de bénédiction vous indique que vous avez une seconde chance, quand vous le souhaitez..")
                            has_found = None
                            second_try_active = False
                else :
                    print("Rien à voir ici !")
            elif salle == 4 :
                if not has_been_defied :
                    print(sorcier, end='\n\n')
                    print("En entrant dans la salle, vous tombez nez à nez avec un mage ennemi, qui vous défie à un jeu ancestral.")
                    
                    time.sleep(1.5)
                    print("Il suffit de deviner un nombre voulu en moins de 10 essais")
                    nb_mystere = random.randint(1, 99)
                    nb_test = int(input('Proposez un nombre entre 1 et 99 : '))
                    compteur = 1

                    while True:
                        
                        if nb_mystere > nb_test:
                            nb_test = int(input('Trop petit ! Testez encore : '))
                        elif nb_mystere < nb_test:
                            nb_test = int(input('Trop grand ! Testez encore : '))
                        elif nb_mystere == nb_test:
                            print('Bravo ! Le nombre était ', nb_mystere)
                            wait_petits_points(0.7)
                            print("Le mage s'incline respectueusement devant vous, puis reprend ses activités d'érudit\nIl vous offre le grimoire de glace, puissant livre magique")
                            inventaire.append("Grimoire de glace")
                            break
                        
                        if compteur > 10 :
                            print('Perdu ! Le nombre était ', nb_mystere)
                            
                            if second_try_active:
                                print("Mais grâce au totem de bénediction, tu as droit à une seconde chance !")
                                second_try_active = False
                                nb_mystere = random.randint(1, 99)
                                nb_test = int(input('Proposez un nombre entre 1 et 99 : '))
                                compteur = 1
                                continue
                            else:
                                print("Ce combat étant pacifique, il ne vous demande rien. Cependant, il arbore un sourire narquois, signe de sa supériorité intelectuelle")
                                break
                                
                        compteur = compteur + 1

                    time.sleep(1.5)
                    print("Juste avant que vous ne quittiez la salle, le mage enclenche un mécanisme grâce à un levier caché.\nVous entendez un bruit sourd provenant du sud de la salle 2")
                    has_been_defied = True
                else :
                    print("Le mage vous fait un signe de la tête en guise de salutations, et vaque à ses occupations habituelles")
                    time.sleep(1.5)
            
            elif salle == 5 :
                if not has_solved :
                    compteur = 0
                    print(biblio_ascii, end='\n\n')
                    print("Vous entrez dans la salle, accueilli par un bibliothécaire.\nIl vous annonce énigmatiquement quela bibliothèque derrière lui renferme un secret.")
                    while True : 
                        entree = input("entrez une séquence de 8 lettres comme cela : XXXXXXXX en majuscules, ou f pour abandonner l'énigme et continuer le reste du donjon")
                        if entree == "f" :
                            print("Vous pourrez toujours revenir plus tard..")
                            break
                        if entree == "FGABCHDE" :
                            time.sleep(0.5)
                            print("A l'annonce de votre réponse, le bibliothécaire sourit et active un bouton sous son bureau")
                            wait_petits_points(1.2)
                            print("! ! ! ! ! ! ! !")
                            print("Félicitations, vous remportez le légendaire artefact ! Vous pouvez vous estimer heureux ! ")
                            inventaire.append("Artefact")
                            has_solved = True
                            break
                        elif compteur == 2 :
                            print("Dans un élan d'immense génerosité, le libraire vous donne un bout de papier intitulé 'INDICE'")
                            if input('Souhaitez-vous le regarder ? (y/n)') == 'y':
                                print("FGAXXXXX")
                            else :
                                print("Le libraire vous hoche la tête en signe de respect.")
                        compteur += 1
                else :
                    print("A votre incompréhension totale, la salle est complétement vide.\nLà où vous aviez laissé le bibliothécaire, une note :\n'Prenez garde, le sphinx peut s'avérer carnivore au bout de 3 tentatives successives'")
            
            elif salle == 6 :
                
                if has_been_defied :
                    print(sphinx, end='\n\n')
                    print("Vous entrez dans la salle.\nDevant vous, un sphinx en roche, endormi")
                    wait_petits_points(0.7)
                    print("A cause du bruit de vos pas, il se réveille :\n'Oh vil explorateur, toi qui t'es aventuré dans les profondeurs mêmes de la Terre\n Sauras-tu résoudre ma charade ?'")
                    if input("oui (y), non (n)") == 'y':
                        compteur = 1
                        while True :
                            entree = input("Quel être, pourvu d'une seule voix, a d'abord quatre jambes le matin, puis deux jambes le midi, et trois jambes le soir ?")
                            wait_petits_points(0.5)
                            if entree in l_mots:
                                
                                if "Artefact" in inventaire :
                                    print("Bravo, vous avez gagné :\n\tVous êtes sorti du donjon avec l'artefact.")
                                    if len(inventaire) != 1 :
                                        print(f"Additionellement, vous avez obtenu {len(inventaire)-1} objets cachés !")
                                        for each in inventaire :
                                            print(each, end=" ")
                                else :
                                    print("Vous êtes sorti du donjon en laissant l'artefact derrière vous, quel dommage !")
                                    if len(inventaire) != 0 :
                                        print(f"Pour vous consoler, vous avez obtenu {len(inventaire)} autres objets..")
                                        for each in inventaire :
                                            print(each, end=" ")
                                            
                                Running = False
                                break
                                
                            elif compteur < 3 :
                                print('"MAUVAIS REPONSE", vous sentez l`aura meurtière de la créature s`intensifier')
                            else :
                                print("'Vous ne méritez pas de sortir de ce donjon', affirme le sphinx avant de sortir de son deux ses mains immenses et de vous étrangler à mort...")
                                if second_try_active :
                                    print("Mais le totem de bénedction vous sauve de la mort et vous donne une seconde chance, utilisez-la bien !\nPartez de la salle et revenez lorsque vous vous sentez prêt.")
                                    compteur = 0
                                    second_try_active = False
                                else :
                                    Running = False
                                break
                                
                            compteur += 1
                    else :
                        print("C'est bien.. les humains intelligents ont meilleur goût.")
                        
                if not has_been_defied  :
                    print(porte, end="\n\n")
                    print("Une lourde porte antique vous bloque le passage pour l'instant, faites demi-tour")
                    
                    
                    
        elif entree == "q" :
            Running = False
            print("A bientôt !")
        else :
            print("erreur : commande invalide")
        
        time.sleep(0.8)
        print('\n')
    
jeu()    
        
        
        
    
    

