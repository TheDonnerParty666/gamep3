
Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> questionOneCorrect = 0
print("Welcome to Hadestown.  Didn't you learn the first time?") 
print("First Level.")
while questionOneCorrect == 0:
    print("How many pomegrantes did Persephone eat that doomed her to shared time in Hell?")
    questionOneAnswer = raw_input()
    questionOneAnswer = str(questionOneAnswer)
    if str.lower(questionOneAnswer) == "six":
        print("Good... for a fool")
        questionOneCorrect = 1
    elif questionOneAnswer == "6":
        print("Good... for a fool")
        questionOneCorrect = 1
    else:
        print("FAILURE.")
questionTwoCorrect = 0
print("Second Level.")
while questionTwoCorrect == 0:
    print("How many heads does Ceberus have?")
    questionTwoAnswer = raw_input()
    questionTwoAnswer = str(questionTwoAnswer)
    if str.lower(questionTwoAnswer) == "three":
        print("Correct!")
        questionTwoCorrect = 1
    elif questionOneAnswer == "3":
        print("Good... for a fool")
    else:
        print("%&^$%%%*$@#")
questionThreeCorrect = 0
print("Cerberus.")
while questionThreeCorrect == 0:
    print("WHO IS PERSEPHONE?")
    questionThreeAnswer = raw_input()
    questionThreeAnswer = str(questionThreeAnswer)
    if str.lower(questionThreeAnswer) == "queen of the underworld":
        print("Ceberus, allow them through.")
        questionThreeCorrect = 1
    elif str.lower(questionThreeAnswer) == "hades' wife":
        print("Enter Further")
        questionThreeCorrect = 1
    elif questionOneAnswer == "greek goddess":
        print("Good... for a fool")
     elif questionOneAnswer == "goddess of the underworld":
        print("Hither")
  elif questionOneAnswer == "demeter's daughter":
        print("Good... for a fool")
    else:
        print("@$  NO  @(*T@)@")
print("Fourth question.")
questionFourCorrect = 0
while questionFourCorrect == 0:
    print("What realm does Hades reside over?")
    questionFourAnswer = raw_input()
    questionFourAnswer = str(questionFourAnswer)
    if questionFourAnswer == "hell":
        print("Correct!")
        questionFourCorrect = 1
          questionFourAnswer = raw_input()
    questionFourAnswer = str(questionFourAnswer)
    if questionFourAnswer == "the underworld":
        print("Correct!")
        questionFourCorrect = 1
    else:
        print("Incorrect!")
print("Fifth question. Getting hot in here!")
questionFiveCorrect = 0
while questionFiveCorrect == 0:
    print("From what mythos do Hades and Persephone reside?")
    questionFiveAnswer = raw_input()
    if str.lower(questionFiveAnswer) == "greek":
        print("Correct!")
        questionFiveCorrect = 1
    else:
        print("3-3-14u+@# WRONG")

for count in range(100):
          print("")
print("Well done...")
