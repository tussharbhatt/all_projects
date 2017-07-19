import journalBack
import  middleWare


entries=[]

def user_inp():
    jrName=input("give your input here..  ")
    jrName=jrName.lower().strip()
    entries = []
    if jrName=='add':
        data = None
        while data != 'xxx':
            data = input("enter the record..  ")
            entries.append(data)

        #journalBack.add_entries(entries)
        jrName = input("enter name for the new journal  ")

        journalBack.save(jrName, entries)
    else:
        entries = journalBack.load(jrName)
        list(entries)



def list(entries):
    for indx,items in enumerate(entries):
        print("{}) {}".format(indx+1,items))


def add():
    pass

def main():
    journalBack.list_journals()
    user_inp()


main()
