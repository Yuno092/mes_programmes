"""
Eléa Heijligers
Objectif : Tour de hanoi 
Programme récursif 
Animation Tkinter 
"""

# importation du module tkinter
import tkinter as tk

# creation d'une fenetre principale
fenetre = tk.Tk()
fenetre.title("Tour de Hanoï")
fenetre.geometry("800x600")

# creer trois rectangles pour les 3 piles
canvas = tk.Canvas(fenetre, width=600, height=400, bg='white')
pile1 = canvas.create_rectangle(100, 100, 120, 300, fill='brown')
pile2 = canvas.create_rectangle(250, 100, 270, 300, fill='brown')
pile3 = canvas.create_rectangle(400, 100, 420, 300, fill='brown')
#socle = canvas.create_rectangle(600/10,9*600/10,20)
canvas.pack()

# creer cinqs disques
disk5 = canvas.create_oval(85, 200, 135, 220, fill='blue')
disk4 = canvas.create_oval(70, 220, 150, 240, fill='green')
disk3 = canvas.create_oval(55, 240, 165, 260, fill='yellow')
disk2 = canvas.create_oval(40, 260, 180, 280, fill='orange')
disk1 = canvas.create_oval(25, 280, 195, 300, fill='red')

'''
 disk5 = canvas.create_oval(25, 200, 195, 220, fill='blue')
disk4 = canvas.create_oval(40, 220, 180, 240, fill='green')
disk3 = canvas.create_oval(55, 240, 165, 260, fill='yellow')
disk2 = canvas.create_oval(70, 260, 150, 280, fill='orange')
disk1 = canvas.create_oval(85, 280, 135, 300, fill='red') 
'''


# fonction de deplacement des disques a différents piles
def move_disk(disk, from_pile, to_pile):
    canvas.move(disk, to_pile - from_pile, 0)


def move_disk_to_pile1(disk):
    move_disk(disk, 250, 100)


def move_disk_to_pile2(disk):
    move_disk(disk, 100, 250)


def move_disk_to_pile3(disk):
    move_disk(disk, 250, 400)


# creation de boutons pour commencer l'animation
bouton1 = tk.Button(fenetre, text="Déplacer le disque 1 vers le pôle 2",
                    command=lambda: move_disk_to_pile2(disk5))
bouton1.pack()
bouton2 = tk.Button(fenetre, text="Déplacer le disque")
bouton2.pack()

def


def TourHanoi(cpt, n, depart, arrivee, transition):
    i = 0
    if (n == 1):
        print(cpt, ": deplacer le disque 1 de la tige",
              depart, "vers la tige", arrivee)
        move_disk_to_pile2(disk5)
        for i < 1000
        i = i+1
        cpt += 1
        return cpt
    cpt = TourHanoi(cpt, n-1, depart, transition, arrivee)
    print(cpt, ": deplacer le disque", n, "de la tige",
          depart, "vers la tige", arrivee)
    cpt += 1
    cpt = TourHanoi(cpt, n-1, transition, arrivee, depart)
    return cpt


cpt = 0
#TourHanoi(cpt, 5, 'centre', 'droite', 'gauche')


fenetre.mainloop()
