def main():
    #items=[]
    #for item in range(5):
        #items.append(int(input("enter no")))
    #print(items)
    #print(sorted(items))
    #items.sort()
    #print(items)
    #items.sort()
    #print(items)
    #items.reverse()
    #for i in items:
    #    if items.index(i)==2:
    #        continue
    #    else:
    #        print(i)
    #print(items)
    used=[]
    name=input("enter string  ")
    #print(name[::-2])
    #used=name.split('0')
    #print(used)
    count=0
    for i in range(len(name)):
        #print(name[i])
        if name[i]=='0':
            count+=1
            print("the {} zero is at position {}".format(count,i+1))
    #print("total no of zeros are  {}".format(count))
main()