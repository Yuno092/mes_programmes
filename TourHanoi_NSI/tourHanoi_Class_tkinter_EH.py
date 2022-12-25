from tkinter import _cnfmerge
from tkinter import *
import tkMessageBox
from PIL import Image, ImageTk


class Dialog(Widget):

    def __init__(self, master=None, cnf={'title': 'Erreur de chargement',
                                         'text': """Le fichier contenant l'image de fond (fond.bmp) n'est pas dans le même répertoire que votre script
    Vous pouvez ne pas mettre d'image en fond ou bien quitter le programme""",
                                         'bitmap': 'warning',
                                         'default': 0,
                                         'strings': ('Charger sans fond',
                                                     'Quitter')}, **kw):

    cnf = _cnfmerge((cnf, kw))
    self.widgetName = '__dialog__'
    Widget._setup(self, master, cnf)
    self.num = self.tk.getint(
        self.tk.call(
            'tk_dialog', self._w,
            cnf['title'], cnf['text'],
            cnf['bitmap'], cnf['default'],
            *cnf['strings']))


try:
    Widget.destroy(self)
except TclError:
    pass


def destroy(self): pass


class Hanoi(Frame):
def __init__(self):


Frame.__init__(self, bg='ivory')
self.master.resizable(0, 0)
self.master.wm_geometry(newGeometry='530x560+220+0')
self.master.title("Tours de Hanoï")
self.can = Canvas(self, width=520, height=400, bg='ivory',
                  relief="raised", borderwidth=3)
# --- Image de fond ----#
self.err_chargement = 0
try:
image = Image.open("fond.bmp")
self.fond = ImageTk.PhotoImage(image)
except:
dia = Dialog()
if dia.num == 1:
self.err_chargement = 1
return
else:
self.err_chargement = 0
self.fond = ""


## ------------------------------ L'interface --------------------------------------##
# --- le cadre principal --- #
cadre_interface = Frame(self, relief="ridge", borderwidth=3, bg='light green')

# --- les sous-cadres ---#
cadre_nbDisc = Frame(cadre_interface, bg='light blue',
                     relief="ridge", borderwidth=3)
cadre_vitesse = Frame(cadre_interface, bg='light green',
                      relief="ridge", borderwidth=3)
cadre_bouttons = Frame(cadre_interface, bg='light green',
                       relief="ridge", borderwidth=3)

# --- la règle nb disques ---#
Label(cadre_nbDisc, text="Nombre de disques :", bg='light blue',
      font="Arial 11 bold").grid(row=1, column=1)
self.nb_disques = IntVar()
disques = Scale(cadre_nbDisc, from_=1, to=8, length=420, orient=HORIZONTAL,
                tickinterval=1, variable=self.nb_disques, command=self.initialisation,
                bg='light blue',
                activebackground='blue',
                troughcolor='ivory')
disques.grid(row=2, column=1)

# --- le choix de la vitesse ---#
Label(cadre_vitesse, text="Vitesse de déplacement :",
      font="Arial 11 bold", bg='light green').grid(row=1, column=2)
self.deux_vitesses = [('Lente', 5), ('Rapide', 10)]
self.vitesse = IntVar()
self.vitesse.set(5)
i = 1
for texte, vit in self.deux_vitesses:
rad_bout = Radiobutton(cadre_vitesse, text=texte, variable=self.vitesse,
                       bg='dark green', fg='ivory', selectcolor='maroon',
                       activebackground='ivory', activeforeground='maroon',
                       value=vit, indicatoron=0, font="Arial 13 bold")
rad_bout.grid(row=2, column=i)
i += 2

# --- les 3 boutons de droite ---#
Button(cadre_bouttons, text="Initialiser",
       command=self.initialisation, font="Arial 11 bold", bg='blue', fg='ivory',
       activebackground='ivory', activeforeground='blue').grid(row=1, column=1, padx=2, pady=2, sticky="nsew")
self.etat_but_sol = IntVar()
self.sol_but = Checkbutton(cadre_bouttons, text='Solution', bg='red', fg='ivory',
                           activebackground='ivory', activeforeground='red',
                           selectcolor='red',
                           variable=self.etat_but_sol, command=self.solution,
                           indicatoron=0, font='Arial 11 bold')
self.sol_but.grid(row=2, column=1, padx=2, pady=2, sticky="nsew")

Button(cadre_bouttons, text="Quitter", bg='black', fg='ivory',
       activebackground='ivory', activeforeground='black',
       command=self.quitter, font="Arial 11 bold").grid(row=3, column=1, padx=2, pady=2,
                                                        sticky="nsew")
Button(cadre_bouttons, text="Règles", bg='dark violet', fg='ivory',
       activebackground='ivory', activeforeground='dark violet',
       command=self.regle, font="Arial 11 bold").grid(row=4, column=1, padx=2, pady=2,
                                                      sticky="nsew")
cadre_nbDisc.grid(row=1, column=1)
cadre_vitesse.grid(row=2, column=1)
cadre_bouttons.grid(row=1, column=2, rowspan=2)

cadre_interface.pack()
self.can.pack()

# --- Création du canevas et des item 'texte'(coups mini, coups effectués)
self.can.create_image(264, 204, image=self.fond)
mess = "Nombre minimum de mouvements : "
self.coups_mini = self.can.create_text(
    250, 340, text=mess, font="Arial 13 bold ", fill='white')
self.coups = self.can.create_text(250, 360, text="Nombre de déplacements effectué : "
                                  + str(0), font="Arial 13 bold ", fill='white')

# --- Tableau des 3 tours ---#
self.tours = [[], [], []]  # chacune d'elle est un tab à 4 dim :
t1 = [[], [], [], []]  # 1ere -> l'id de la tour
t2 = [[], [], [], []]  # 2eme -> tab d'id des disques
t3 = [[], [], [], []]  # 3eme -> id de la tige
# 4eme -> tab des coord de la base
# tn = [id tn,[idD1,idD2,...],id tige,[coord_tn_xmin,coord_tn_ymin,coord_tn_xmax,...]]
self.tours[0] = t1
self.tours[1] = t2
self.tours[2] = t3

# --- Les bases ---#
long_base = 120
t1[0] = self.can.create_rectangle(40, 300, 40+long_base, 310, fill='gold')
t2[0] = self.can.create_rectangle(200, 300, 200+long_base, 310, fill='gold')
t3[0] = self.can.create_rectangle(360, 300, 360+long_base, 310, fill='gold')
# --- Les tiges ---#
t1[2] = self.can.create_rectangle(95, 300, 105, 100, fill='gold')
t2[2] = self.can.create_rectangle(255, 300, 265, 100, fill='gold')
t3[2] = self.can.create_rectangle(415, 300, 425, 100, fill='gold')
# --- Toutes les coordonnées relatives à chaque base ---#
self.coord_t1 = self.can.coords(self.tours[0][0])
self.coord_t1_xmin = self.coord_t1[0]
self.coord_t1_ymin = self.coord_t1[1]
self.coord_t1_xmax = self.coord_t1[2]
self.coord_t1_ymax = self.coord_t1[3]
self.coord_t1_mil = self.coord_t1_xmin + \
    (self.coord_t1_xmax-self.coord_t1_xmin)/2
self.tours[0][3] = [self.coord_t1_xmin, self.coord_t1_ymin,
                    self.coord_t1_xmax, self.coord_t1_ymax, self.coord_t1_mil]

self.coord_t2 = self.can.coords(self.tours[1][0])
self.coord_t2_xmin = self.coord_t2[0]
self.coord_t2_ymin = self.coord_t2[1]
self.coord_t2_xmax = self.coord_t2[2]
self.coord_t2_ymax = self.coord_t2[3]
self.coord_t2_mil = self.coord_t2_xmin + \
    (self.coord_t2_xmax-self.coord_t2_xmin)/2
self.tours[1][3] = [self.coord_t2_xmin, self.coord_t2_ymin,
                    self.coord_t2_xmax, self.coord_t2_ymax, self.coord_t2_mil]

self.coord_t3 = self.can.coords(self.tours[2][0])
self.coord_t3_xmin = self.coord_t3[0]
self.coord_t3_ymin = self.coord_t3[1]
self.coord_t3_xmax = self.coord_t3[2]
self.coord_t3_ymax = self.coord_t3[3]
self.coord_t3_mil = self.coord_t3_xmin + \
    (self.coord_t3_xmax-self.coord_t3_xmin)/2
self.tours[2][3] = [self.coord_t3_xmin, self.coord_t3_ymin,
                    self.coord_t3_xmax, self.coord_t3_ymax, self.coord_t3_mil]

## -----------------------------------------------------------------------------------##
# --- Démarage ---#
self.initialisation()

## ---------------------- Init de toutes les variables ---------------------------------------##


def initialisation(self, x=1):


self.init 1  # var qui permet de sortir de la boucle de mouvement si1

for t in self.tours:
for disque in t[1]:
self.can.delete(disque)  # effacement des disques du canevas
t[1] = []  # et du tableau des tours

self.nb_disc = self.nb_disques.get()  # récupération du nombre de disques
self.creer_disques(self.nb_disc)  # création des disques

# récupération de la vitesse de déplacement(5 ou 10 pix)
self.vit = self.vitesse.get()
self.dx, self.dy = 0, -self.vit  # direction du déplacement


self.tour_dep = []  # tableau qui contiendra la tour de depart selectionnée
self.tour_arr = []  # pareil pour la tour d'arrivée

# tableau qui contiendra les couples (tour dep,tour arr) pour la solution
self.tab = []
self.index = 0  # var pour se deplacer dans le ce tableau après chaque mouvement
self.sol = 0  # var qui indique que l'on est(=1) ou pas(=0) en mode solution

self.mouv = 0  # var qui contient le nombre de mouvements effectués

self.can.bind('', self.selection_tour)

self.mini_mouv = (2**self.nb_disc)-1  # nombre de mouvements minimum
mess = "Nombre minimum de mouvements : %s" % (str(self.mini_mouv))
self.can.itemconfigure(self.coups_mini, text=mess)  # modif du Label
self.can.itemconfigure(self.coups, text="Nombre de déplacements effectué : "
                       + str(0))

self.can.itemconfigure(self.tours[0][0], fill='gold')
self.can.itemconfigure(self.tours[0][2], fill='gold')
self.can.itemconfigure(self.tours[1][0], fill='gold')
self.can.itemconfigure(self.tours[1][2], fill='gold')
self.can.itemconfigure(self.tours[2][0], fill='gold')
self.can.itemconfigure(self.tours[2][2], fill='gold')


def creer_disques(self, nb):


    # Création de nb disques choisi par l'utilisateur
for i in range(nb):  # i compris entre 0 et nb-1
    # i étant croissant les pos en xmin et
coord_d_xmin = self.coord_t1_mil - (nb-i)*10
# xmax diminuent et sont multiple de 10
coord_d_xmax = self.coord_t1_mil + (nb-i)*10
# pos en y i fois l'épaisseur d'un disque
coord_d_y self.coord_t1_ymin - (i*20)
self.tours[0][1].append(self.can.create_rectangle(
    coord_d_xmin, coord_d_y, coord_d_xmax, coord_d_y-20, fill='maroon'))

# ---------- Départ de l'algorithme de solution ----------#
# --- Phase 1 : Initialisation ---#


def solution(self):


self.initialisation()  # Appel à l'initialisation générale
self.init = 0
self.sol = 1  # mode solution : après chaque pose de disque on reviendra sur la phase 3
# 0,1,2 -> les indexs des tours dans self.tours
self.recursivite(self.nb_disc, 0, 1, 2)
self.deplace_auto()

# --- Phase 2 : Remplissage du tableau de couple (t_dep,t_arr) par récursivité ---#


def recursivite(self, n, td, tt, ta):


if n > 0:
self.recursivite(n-1, td, ta, tt)
self.tab.append((td, ta))
self.recursivite(n-1, tt, td, ta)

# --- # Phase 3 : Appel successif de la fonction mouvement avec chaque couple(t_dep,t_arr) ---#


def deplace_auto(self):


self.can.unbind('')

couple = self.tab[self.index]

self.tour_dep = self.tours[couple[0]]
self.tour_arr = self.tours[couple[1]]

self.deplacement()
self.index += 1
# -----------------------------------------------------#

# --- Selection à la souris des tours de départ et d'arrivée ---#


def selection_tour(self, event):


x, y = event.x, event.y
tour_selec = []

if ((x > self.coord_t1_xmin and x < self.coord_t1_xmax) and
   (y > 100 and y < self.coord_t1_ymax)):
tour_selec = self.tours[0]

elif ((x > self.coord_t2_xmin and x < self.coord_t2_xmax) and
      (y > 100 and y < self.coord_t2_ymax)):
tour_selec = self.tours[1]

elif ((x > self.coord_t3_xmin and x < self.coord_t3_xmax) and
      (y > 100 and y < self.coord_t3_ymax)):
tour_selec = self.tours[2]
else:
return

if self.tour_dep == []:
self.tour_dep = tour_selec
self.can.itemconfigure(self.tour_dep[0], fill='red')
self.can.itemconfigure(self.tour_dep[2], fill='red')
if self.tour_dep[1] == []:  # tour de départ vide : violation d'une règle
tkMessageBox.showerror(title="Tour de départ invalide",
                       message="Cette tour de départ ne contient aucun disque")
self.can.itemconfigure(self.tour_dep[0], fill='gold')
self.can.itemconfigure(self.tour_dep[2], fill='gold')
self.tour_dep = []
elif self.tour_dep != []:
self.tour_arr = tour_selec
self.can.itemconfigure(self.tour_arr[0], fill='green')
self.can.itemconfigure(self.tour_arr[2], fill='green')
if self.tour_arr == self.tour_dep:
self.can.itemconfigure(self.tour_dep[0], fill='gold')
self.can.itemconfigure(self.tour_dep[2], fill='gold')
self.tour_dep = []
self.tour_arr = []
if self.tour_dep != [] and self.tour_arr != []:
self.verif()

# --- Vérification du respect de la règle pas de disque sur un plus petit ---#


def verif(self):


self.init = 0

if self.tour_arr[1] != []:
coord_d_dep = self.can.coords(self.tour_dep[1][-1])
diam_d_dep = coord_d_dep[2] - coord_d_dep[0]

coord_d_arr = self.can.coords(self.tour_arr[1][-1])
diam_d_arr = coord_d_arr[2] - coord_d_arr[0]

if diam_d_arr < diam_d_dep:
self.can.itemconfigure(self.tour_dep[0], fill='gold')
self.can.itemconfigure(self.tour_dep[2], fill='gold')
self.can.itemconfigure(self.tour_arr[0], fill='gold')
self.can.itemconfigure(self.tour_arr[2], fill='gold')
self.tour_dep = []
self.tour_arr = []
tkMessageBox.showerror(title="Déplacement non autorisé",
                       message="Attention pas de disque sur un plus petit que lui !")
return

self.deplacement()

# --- Mouvement d'un disque d'une tour à une autre ---#


def deplacement(self):


    # Si appui sur 'initialisation' ou désélection du bonton 'solution'
if self.init == 1 or (self.etat_but_sol.get() == 0 and self.sol == 1):
self.sol_but.deselect()
self.initialisation()
return
self.can.unbind('')

# Présence ou non d'un disque sur la tour d'arrivée par defaut : non
disc_present = 0

# Coord du disque qui se deplace et de son milieu
coord_d = self.can.coords(self.tour_dep[1][-1])
coord_d_xmin = coord_d[0]
coord_d_xmax = coord_d[2]
coord_d_ymin = coord_d[1]
coord_mil_d = coord_d_xmin+(coord_d_xmax-coord_d_xmin)/2

# Coord du dernier disque de la tour d'arrivé si il existe
if self.tour_arr[1] != []:
disc_present = 1
coord_d_arr = self.can.coords(self.tour_arr[1][-1])
coord_d_arr_ymin = coord_d_arr[1]

# Si le disque est en haut
if coord_d_ymin == 60:
self.dy = 0
# le signe de la différence des coord en xmin des tours donne le sens de déplacement
# Déplacement sur la droite
if self.tour_arr[3][0] - self.tour_dep[3][0] > 0:
self.dx = self.vit
# Ou déplacement sur la gauche
else:
self.dx = -self.vit

# Si les milieux du disque et de la tour d'arrivée correspondent
if coord_mil_d == self.tour_arr[3][4]:
self.dx = 0
self.dy = self.vit
# Descente du disque
# jusq'au dernier de la tour d'arrivée
if disc_present == 0:
if coord_d_ymin+20 == self.tour_arr[3][1]:
self.disque_pose()  # Que faire quand le disque est posé
return
# sinon jusqu'à la base
elif disc_present == 1:
if coord_d_ymin+20 == coord_d_arr_ymin:
self.disque_pose()  # Que faire quand le disque est posé
return

self.can.move(self.tour_dep[1][-1], self.dx, self.dy)
self.master.after(self.vit, self.deplacement)

# --- Actions à réaliser quand un disque est posé ---#


def disque_pose(self):


self.dy = 0

self.can.itemconfigure(self.tour_dep[0], fill='gold')
self.can.itemconfigure(self.tour_dep[2], fill='gold')
self.can.itemconfigure(self.tour_arr[0], fill='gold')
self.can.itemconfigure(self.tour_arr[2], fill='gold')

# Le disque déplacé est ajouté au tableau des disques de la tour d'arrivée
self.tour_arr[1].append(self.tour_dep[1][-1])
# Et supprimé du tableau de la tour de départ
del (self.tour_dep[1][-1])

# Quelques réinitialisations
self.tour_dep = []
self.tour_arr = []
self.dx, self.dy = 0, -self.vit
self.can.bind('', self.selection_tour)
self.vit = self.vitesse.get()

# Mise à jour du label 'déplacements effectués'
self.mouv += 1
self.can.itemconfigure(
    self.coups, text="Nombre de déplacements effectués : " + str(self.mouv))


# Si la tour doite est complète en mode 'souris'
if len(self.tours[2][1]) == self.nb_disc and self.sol == 0:
    # si il y a trop de déplacements
if self.mouv > self.mini_mouv:
diff = self.mouv - self.mini_mouv
message = "Bien mais il y a %s coups de trop\nVoulez-vous rejouer ?" % (
    str(diff))
# si le minimum de déplacement est respecté
elif self.mouv == self.mini_mouv:
message = "Gagné ! en %s coups\nVoulez-vous rejouer ?" % (str(self.mouv))

if tkMessageBox.askyesno(title=" !! BRAVO !!", message=message):
self.initialisation()
else:
self.master.destroy()
return

# Si la tour doite est complète en mode 'solution'
elif len(self.tours[2][1]) == self.nb_disc and self.sol == 1:
if tkMessageBox.askyesno(title=" Terminé",
                         message="Solution terminée\n%s coups minimum respectés\nVoulez-vous rejouer ?"
                         % (str(self.mouv))):
self.sol_but.deselect()
self.initialisation()
else:
self.master.destroy()
return

# Si la tour doite n'est pas complète en mode 'solution'
if self.sol == 1:
    # Retour en phase 3
self.deplace_auto()

# Si la tour doite n'est pas complète en mode 'souris'
# retour dans l'attente d'une sélection
return

# --- Arret de l'aplication ---#


def quitter(self):


self.master.destroy()

# --- Règle du jeux ---#


def regle(self):


regle = Toplevel(self, bg='pink', width=200, height=200)
regle.resizable(0, 0)
# Pour n'avoir qu'une icone dans la barre des tâches
regle.transient(self.master)
regle.grab_set()  # Pour que l'utilisateur n'a plus accès à la fenetre parente
regle.wm_geometry(newGeometry='700x200+120+180')
mess = "Règle du jeux\n\n Le but est de déplacer tous les disques\
de la tour gauche vers la tour droite\n\
et ce sans violer les règles suivantes :\n\n\
1°/ On ne peut déplacer qu'un disque à la fois\n\
2°/ Un disque ne peut se poser sur un disque plus petit que lui\n"
Label(regle, text=mess, font='Century 13 bold',
      bg='light blue', relief='ridge', borderwidth=5).pack()
Button(regle, text='OK', command=regle.destroy).pack()


if __name__ == '__main__':

app = Hanoi()
if app.err_chargement == 1:
app.master.destroy()
elif app.err_chargement == 0:
app.pack()
app.mainloop()
