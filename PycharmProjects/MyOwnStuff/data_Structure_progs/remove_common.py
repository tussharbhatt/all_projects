

def main():
    items=[]
    for i in range(5):
        items.append(input("enter values  "))

    dict={}
    for item in items:
        #print(item)
        if item not in dict:
            dict['key']=item

    #for keys in dict.items():
        print(dict['key'])

main()