from functools import reduce

def longueur(liste):
    return list(map(len, liste))

print (longueur(["un","deux", "trois"]))