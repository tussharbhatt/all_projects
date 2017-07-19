import os

import commonHeader


def main():
    commonHeader.print_header()
    folder = get_search_folder()
    if not folder:
        print("sorry this folder does not exists... exitting  ..")
        return


    search_text = get_search_text()
    if not search_text:
        print("sorry can't search that..bye..  ")
        return
    all_matches = search_files(folder, search_text)
    line_no=1
    for lines in all_matches:
        print("{}. {}".format(line_no,lines))
        print()
        print()
        line_no+=1
    return

def get_search_folder():
    folder = input("enter the folder you want to search in..  ")
    if not os.path.isdir(folder) or not folder:
        print("False")
        return
    return folder


def get_search_text():
    search_text = input("enter the text you want to search..   ")
    if not search_text:
        return
    return search_text.lower()


def search_files(folder, search_text):

    items=[]
    all_match=list()
    items = os.listdir(folder)
    #print(items)
    match=[]
    for item in items:
        if os.path.isdir(item):
            continue
        else:
            file_path = os.path.join(folder, item)
            print(file_path)

            #print("in file at {}".format(file_path))
            with open(file_path, 'r', encoding='utf-8') as fin:
                for line in fin:
                    if line.lower().find(search_text) >= 0:
                        match.append(line)

        all_match.extend(match)

    return all_match

if __name__=='__main__':
    main()