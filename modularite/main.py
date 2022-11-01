#deux façons d'importer
# la première : on importe fonction après fonction séparés par les virgules
# ca permet d'appeler directement la fonction
from monmodule import tauxvar, pgf
print(tauxvar(100,10))

help(monmodule)
#sinon on importe tout le module d'un coup mais il faut préfixer les appels aux fonctions par monmodule
# import monmodule
# print(monmodule.tauxvar(100,10))