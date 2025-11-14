import random

name = "Marx"
question = "Is all of this real?"
answer = ""
random_number = random.randint(1,15)

if random_number == 1:
  answer += "Yes - definetly"
elif random_number == 2:
  answer += "It is decidedly so"
elif random_number == 3:
  answer += "Without a doubt"
elif random_number == 4:
  answer += "Reply hazy, try again"
elif random_number == 5:
  answer += "Ask again later"
elif random_number == 6:
  answer += "Better not tell you now"
elif random_number == 7:
  answer += "My sources say no"
elif random_number == 8:
  answer += "Outlook not so good"
elif random_number == 9:
  answer += "It depends, is it?"
elif random_number == 10:
  answer += "You know the anwser"
elif random_number == 11:
  answer += "Wrong question"
elif random_number == 12:
  answer += "The true anwser is the next anwser"
elif random_number == 13:
  answer += "Indubidaudably"
elif random_number == 14:
  answer += "Sure, why not."
elif random_number == 15:
  answer += "I don't think so."
else: answer += "Error, number out of scope"

if name == "":
  print(question)
else:
  print(name + " " + "asks:" + " " + question)

if question == "":
  print("The Magic 8-Ball cannot provide your fortune if you do not provide a question!")
else:
  print("Magic 8-Ball's anwser:" + " " + answer)