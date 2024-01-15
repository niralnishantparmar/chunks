#COLORS
white = "\033[0;37m"
cyan = "\033[0;36m"
bright_black = "\033[0;90m"
yellow = "\033[0;33m"
red = "\033[0;31m"
#INTRO
print ("Version 3.4 of HOMEMADE CALCULATOR\n")
print (cyan, "Hi!" )
print (white, "")
repeat = "yes"
#THE ACTUAL PROGRAM :)
while repeat == "yes":
  x = float (input ("Type in the first number you want to calculate: "))
  #EASTER EGG
  if x == float (404):
    print (red, "SECRET CODE INITIATED.\n DINO MODE. 🦕 ")
  elif x == float (405):
    print ('You nearly guessed the secret code right! Whoa! Buuuut you got one digit wrong. Pico.')
  else:
    y = float (input ("Type in the second number that you want to calculate: "))
    sign = input ("Type in if you want to multiply, divide, add, or subtract the two numbers. (* means multiplication, + means addition, / means division, and - means subtraction): ")
    if sign == "*":
      ans = x*y
      print ("The answer is " + str(ans) + ".")
    elif sign == "/":
      ans = x/y
      print ("The answer is " + str(ans)+ ".")
    elif sign == "+":
      ans = x+y
      print ("The answer is " + str(ans)+ ".")
    elif sign == "-":
      ans = x-y
      print ("The answer is " + str(ans)+ ".")
    else:
      print ("Wrong operation. Please try again. Sorry!")
    repeat = (input ("Do you want to use the calculator again? (Type yes or no ONLY) "))
    
print ("Okay, then. Goodbye!\n")
print (yellow, ":)")
#Cool, right?
