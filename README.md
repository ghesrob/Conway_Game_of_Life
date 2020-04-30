# Conway_Game_of_Life
 Une implémentation python du jeu de la vie de Conway.

Le jeu de la vie de Conway est un automate cellulaire se déroulant au tour par tour sur une grille où chaque case représente une cellule.
Une cellule a deux états possible : elle peut être vivante ou morte. A chaque tour, l'état de chacune des cellules est mis à jour selon les règles suivantes :
- une cellule morte possédant exactement trois voisines vivantes devient vivante (elle naît),
- une cellule vivante possédant deux ou trois voisines le reste, sinon elle meurt. 

Par exemple, la configuration ![exemple_1](example_1.png) devient au tour suivant ![exemple_2](example_2.png).