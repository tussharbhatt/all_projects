import journal

file_name = "default.txt"
entries = list()


def user_input():
    cmd = None

    while cmd != 'x':
        cmd = input("enter [l] for listing [a] for adding [e] to exit   ")
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries()

        elif cmd == 'a':
            add_entries()

        elif cmd == 'x':
            print("good bye...!!!")
            journal.save(file_name,entries)

        else:
            print("wrong choice..please input again...")


def list_entries():
    #journal.load(file_name)
    entries = journal.load(file_name)
    for idx, entry in enumerate(entries):
        print("{}) {}".format(idx + 1, entry))



def add_entries():
    data = input("please enter the record :  ")
    journal.add_entry(data,entries)
    # entries.append(data)


user_input()
