import os
#import journalFront

list_all = "index"


def get_file_name(name):
    name=name+'.txt'
    file_name=os.path.join("journals",name)
    return file_name

def list_journals():
    #index_file=get_file_name(list_all)
    load(list_all)


def load(name):
   data=[]
   file_name=get_file_name(name)
   with open(file_name) as fin:
       for items in fin.readlines():
           data.append(items.rstrip())

   journalFront.list(data)



def save(name, journal_data):
    file_name=get_file_name(name)
    print("saving at ..  {}".format(file_name))
    with open(file_name,'w') as fout:
        for items in journal_data:
            fout.write(items+'\n')





def add_entries(journal_data):
    pass