#Great code amigo

#Maybe you cab add pictures and text

import random 

C_145 = ("C,F,G")
D_145 = ("D,G,A")
F_145 = ("F,Bb,C")
G_145 = ("G,C,D")
A_145 = ("A,D,E")

C_1645 = ("C,Am,F,G")
D_1645 = ("D,Bm,G,A")
F_1645 = ("F,Dm,Bb,C")
G_1645 = ("G,Em,C,D")
A_1645 = ("A,F#m,D,E")

C_251 = ("Dm7,G7,Cmaj7")
D_251 = ("Em7,A7,Dmaj7")
F_251 = ("Gma7,C7,Fmaj7")
G_251 = ("Am7,D7,Gmaj7")
A_251 = ("Bm7,E7,Amaj7")

C_1625 = ("C,Am,Dm,G")
D_1625 = ("D,Bm,Em,A")
F_1625 = ("F,Dm,Gm,C")
G_1625 = ("G,Em,Am,D")
A_1625 = ("A,F#m,Bm,E")

C_1564 = ("C,G,Am,F")
D_1564 = ("D,A,Bm,G")
F_1564 = ("F,C,Dm,Bb")
G_1564 = ("G,D,Em,C")
A_1564 = ("A,Em,F#m,D")

C_1465 = ("C,F,Am,G")
D_1465 = ("D,G,Bm,A")
F_1465 = ("F,Bb,Dm,C")
G_1465 = ("G,C,Em,D")
A_1465 = ("A,D,F#m,E")

C_1345 = ("C,Em,F,G")
D_1345 = ("D,F#m,G,A")
F_1345 = ("F,Am,Bb,C")
G_1345 = ("G,Bm,C,D")
A_1345 = ("G,Bm,C,D")

C_1415 = ("C,F,C,G")
D_1415 = ("D,G,D,A")
F_1415 = ("F,Bb,F,C")
G_1415 = ("G,C,G,D")
A_1415 = ("A,D,A,E")

C_1425 = ("C,F,Dm,G")
D_1425 = ("D,G,Em,A")
F_1425 = ("F,Bb,Gm,C")
G_1425 = ("G,C,Am,D")
A_1425 = ("A,D,Bm,E")

vars = (C_145,D_145,F_145,G_145,A_145,C_1645,D_1645,F_1645,G_1645,A_1645,C_251,D_251,F_251,G_251,A_251,C_1625,D_1625,F_1625,G_1625,A_1625,C_1564,D_1564,F_1564,G_1564,A_1564,C_1465,D_1465,F_1465,G_1465,A_1465,C_1345,D_1345,F_1345,G_1345,A_1345,C_1415,D_1415,F_1415,G_1415,A_1415,C_1425,D_1425,F_1425,G_1425,A_1425)

random_progression = random.choice(vars)

print ("Welcome to the CHORD GENERATOR!") 
print ()
print ("I am at your disposal, offering 45 different progressions in the keys of C, D, F, G, A. ") 
print ()
print ("Here is your first random chord progression:")
print ()
print (random_progression)
print ()
print ("Good luck!")

import time
print ()
for second in range(5,6):
    time.sleep(8)
    print("♪♪ Doo--Daah--Baa--Baa--Duu--Dahh ♪♪")
    time.sleep(6)
    print ()
    print("♪♪ Here comes the sun, doo-dn-ddu-duu ♪♪")
    print ()
    time.sleep(6)

print ("if you dont manage to come up with the next TWIST AND SHOUTER, you can always get new ones from me.")
print()
question = input ("Do you want some new chords????")

while question == ("yes"):
    random_progression = random_progression + (".....") + random.choice(vars)
    print (random_progression)
    question = input ("Do you want a new chord progression:")

print ("Good luck with the chosen progression")