
#MadLibGenerator
print ("Mad Lib Generator version 1.2\n")
print ("Made by Niral P.\n")
print ("Hi, there! Do you want to play a fun game? It's called a Mad Lib! Type either '1' (which means yes) or '2' and hit enter.")
con = input()
while con == ('1'):
  print ("Let's play a new game. We have one game option currently available. Sorry! Press 1 to select your game.")
  game = input()
  if game == ('1'):
    print ("Okay. Name an adjective:")
    a = input() 
    print ("Okay. Name another adjective:")
    b = input()
    print ("Okay. Name an animal that you do not like:")
    c = input()
    print ("Okay. Name a location.")
    d = input()
    print ("Okay. Name a past tense verb:")
    e = input()
    print ("Okay. Name a verb:")
    f = input()
    print ("Okay. Name someone you know:")
    g = input()
    print ("Okay. Name a noun:")
    h = input()
    print ("Okay. Name a food item:")
    i = input()
    print ("Okay. Name a verb ending in -ing.")
    j = input()
    print ("Okay. Name a part of the body that's plural:")
    k = input()
    print ("Okay. Name a plural noun:")
    l = input()
    print ("Okay. Name a verb ending in -ing:")
    m = input()
    print ("Last one! Name a noun:")
    n = input()
    print ("Nice! Here's your silly story.")
    print ("It was a " + a + ", cold December day. I woke up to the " + b + " smell of " + c + " roasting in the " + d + " downstairs. Finally! I " + e + " down the stairs to see if I could help " + f +  " the dinner. My mom said, 'See if " + g + " needs a fresh " + h + ".' So I carried a tray full of " + i + " into the " + j + " room. When I got there, I couldn't believe my " + k + "! There were " + l + " " + m + " on the " + n + "!")
    print ('Do you want to play again?')
    con = input()
print ('Okay, then. Goodbye!')

#Story 2: Last night's _______ was really ___. We ate _____ ______ and played _____. But then _____ made ____ really angry because they said ______ really _____ in ____'s ear. 
