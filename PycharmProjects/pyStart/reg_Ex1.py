import re,journal,os


filename=journal.get_file_name("plain_text.txt")
#print(filename)
stringtoSearch=" "
with open(filename ,'r') as fin:
    for line in fin:
        stringtoSearch+=line

    #print(stringtoSearch)



patfinder=re.compile('\s\w{6}\s')
#findpattern=re.search(patfinder,stringtoSearch)
findpattern=re.findall(patfinder,stringtoSearch)
#print("\n\n"+ findpattern.span()+"\n--------")
serch_res=[]
for i in findpattern:
    serch_res.append(i)
print(serch_res)
