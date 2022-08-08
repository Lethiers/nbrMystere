from random import random

essaie = 5
okNbr = 'false'
nbMystere = round(random()*100)
reponse = ""

i = 0
while i < essaie:
    print(f'tu as {essaie} essaie')
    while okNbr =='false':
        reponse = input('essaie de trouver le nombre mystère entre 1 et 100:')
        if reponse.isdigit() == False:
            print('merci de saisir un nombre')
        elif reponse.isdigit() == True:
            okNbr = 'true'
    if int(reponse) == int(nbMystere):
        print(f'tu as trouvé le nombre mystère !!')
        break
    else:
        if int(reponse) < int(nbMystere):
            print('trop bas')
        elif int(reponse) > int(nbMystere):
            print('trop haut')
        essaie = essaie - 1
        okNbr = 'false'
        print(f'tu viens de perdre un essaie')
i = i + 1
print(f'le chiffre mystère était {nbMystere}')






