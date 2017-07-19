import os
brac_stac=[]
file_path="D:/folder/program.txt"
#name="program"
file_path=os.path.join('.',file_path)

#dict = {'{':0,'}':0}

def read_file(file_path):
    temp=0
    temp1=0
    with open(file_path,'r') as fout:
        for line in fout:
            for ch in line:
                if ch is '{':
                    #temp=dict['[']
                    temp+=1
                    #dict['{']=temp
                elif ch is '}':
                    #temp = dict['}']
                    temp1 += 1
                    #dict['}'] = temp
                else:
                    continue

        if temp == temp1:
            print("brackets are balanced")

        else:
            print("brackets are unbalanced")
            print(temp,temp1)




def main():
    read_file(file_path)

if __name__ == '__main__':
    main()