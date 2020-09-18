from movie import *
import scifi
import action_m

a = input("Enter Your Choice \t " + "1.Movies \t" + "2.Scifi Movies \t" + "3.Action Movies")
if (a == 1):
    movie.get_movie()

elif (a == 3):
    action_m.action()

elif (a == 2):
    scifi.sci()
