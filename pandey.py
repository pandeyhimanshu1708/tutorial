from operator import truediv
import random

def swg (comp, mine):
    if (comp=='s' and mine=='g'):
        return true
    elif(comp='w' and mine=='s'):
        return true
    elif(comp=='g' and mine=='w'):
        return true
    else:
        return False

choice =('s','w','g')
comp= random.randint(0,2)
comp= choice[comp]
mine= input('choice euther a,w or g')

win= swg(comp,mine)
if win:
    print("you won")
else:
    print("you lose")
    