import random

print('this is a guessing game\n\n')
the_number=random.randint(0,100)
number=int(input('guess the number..  '))
flag= False
while flag==False:
    if number== the_number:
        print("congrats!  you have guessed right...it is  "+ str(the_number))
        flag=True
    elif number<the_number:
        print("no ! that's too big")
    else:
        print("no ! that's too small")

