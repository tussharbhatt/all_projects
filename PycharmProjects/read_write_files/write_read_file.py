file_name = "random_number.txt"

file_object = open(file_name,'w')
for row in range(1,4):
    for colum in  range(1,4):
        number = 1
        file_object.write(str(number))
        number += 1
        file_object.write(" ")

    file_object.write("\n")
file_object.close()


data = []

file_object = open(file_name, 'r')
space = " "
line = "\n"
for line in file_object:
    rd=line.rstrip().split(' ')
    data.append(rd)
    #for character in line:
        #if character != ' ' and character != '\n':
        #data.append(character.rsplit(' '))
        #print(character)

print(data)