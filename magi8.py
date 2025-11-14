import random

name = "Marx"
question = "Is all of this real?"
anwser = ""
random_number = random.randint(1,15)

if random_number == 1:
  anwser += "Yes - definetly"
elif random_number == 2:
  anwser += "It is decidedly so"
elif random_number == 3:
  anwser += "Without a doubt"
elif random_number == 4:
  anwser += "Reply hazy, try again"
elif random_number == 5:
  anwser += "Ask again later"
elif random_number == 6:
  anwser += "Better not tell you now"
elif random_number == 7:
  anwser += "My sources say no"
elif random_number == 8:
  anwser += "Outlook not so good"
elif random_number == 9:
  anwser += "It depends, is it?"
elif random_number == 10:
  anwser += "You know the anwser"
elif random_number == 11:
  anwser += "Wrong question"
elif random_number == 12:
  anwser += "The true anwser is the next anwser"
elif random_number == 13:
  anwser += "Indubidaudably"
elif random_number == 14:
  anwser += "Sure, why not."
elif random_number == 15:
  anwser += "I don't think so."
else: anwser += "Error, number out of scope"

if name == "":
  print(question)
else:
  print(name + " " + "asks:" + " " + question)

if question == "":
  print("The Magic 8-Ball cannot provide your fortune if you do not provide a qestion!")
else:
  print("Magic 8-Ball's anwser:" + " " + anwser)