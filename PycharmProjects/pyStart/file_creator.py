import os
name="default.txt"

# file_name=os.path.join("C:\Newfolder",name)
'''file_name=os.path.abspath(os.path.join("journals",name))
#the_file=open(file_name,'w')
with open(file_name,'w') as the_file:
    the_file.write("hello world")
    #the_file.close()


file_path=None
file_path=os.path.abspath(file_path)
print(file_path)'''

path="C:\\Users\\tushar.bhatt\\Desktop\\offc\\tick_desc_jpn_clean.txt"
#file_path=os.path.join(path,name)
with open(path,'r') as fout:
    dat=fout.read()
    '''for i in range(1,9):
        fout.write(str(i))'''
    print(dat)

