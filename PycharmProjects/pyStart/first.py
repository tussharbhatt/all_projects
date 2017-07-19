import random

print('guess this no game')
print()
# the_number
number=random.randint(0,100)
# TODO print(number)
flag= False
while flag== False:
    the_number= input('guess the number\n')
    the_number=int(the_number)
    if the_number == number:
        flag= True
        print('congrats!  you have guessed the number  it is ... '+ str(the_number))
        break
    elif the_number > number:
        print("no that's too big")

    else:
        print("no that's too small")


