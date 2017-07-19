import os
lists=[]
path="C:/Users/tushar.bhatt/Downloads"
folder=os.path.join(path,'')
if os.path.isdir(folder):
    print("True")
else:
    print("false")
lists=os.listdir(folder)
print(lists)