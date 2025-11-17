##############################
# Minecraft Arena Fight Game #
# by Me                      #
##############################

import os
import time


#  weapons
weapons = [["Bow",              10],
           ["Iron sword",       15],
           ["Netherite sword",  20],
           ["Spear",            60],
           ["Mace",            100]
         ]


#  mobs
mobs = [['skeleton',     10, 1,  1],
        ['zombie',       15, 1,  2],
        ['enderman',     20, 1,  3],
        ['weather',      60, 1,  4],
        ['enderdragon', 100, 1, -1]
       ]


#  eq

eq = [weapons[0]]

def getMobsAlive():
    m = 0
    for i in range(0, len(mobs)):
        m += mobs[i][2]
    return m

gameover = 0

while getMobsAlive() > 0 and gameover == 0:
    os.system('cls')
    print ('My eq:')
    for i in range(0, len(eq)):
        print("   " + str(i+1) + " " + eq[i][0] + " damage: " + str(eq[i][1]))
    w = int(input('Choose weapon ')) - 1
    if w > len(eq):
        w = 0
    print ('You chose ' + eq[w][0])
    print ('Mobs alive:')
    for i in range(0, len(mobs)):
        if mobs[i][2] == 1: 
            print("   " + str(i+1) + " " + mobs[i][0] + ", hp: " + str(mobs[i][1]))
    m = int(input('Choose mob to fight ')) - 1       
    if m < len(mobs):
        if mobs[m][2] == 1:
            if eq[w][1] >= mobs[m][1]:                 
                print('You defeated mighty ' + mobs[m][0] + ' with ' + eq[w][0] + '.')
                mobs[m][2] = 0
                if mobs[m][3] > 0:
                    eq .append(weapons[mobs[m][3]])
                    print('You got a new ' + eq[len(eq)-1][0])                 
            else:
                print('The mighty ' + mobs[m][0] + ' defeated you.')           
                gameover = 1
        else:
            print('This mob is already dead!!!')
    else:
        print('There is no such mob!!!')
    time.sleep(3)
if getMobsAlive() == 0:
    print('You won!!!')
else:
    print('You lost!!!')


    
   



