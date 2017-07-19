import os


def get_file_name(name):
    filename = os.path.abspath(os.path.join("journals", name))
    return filename


def load(name):
    '''

    :param name: name of the journal
    :return: list populated with data on the file
    '''
    data = []
    file_name = get_file_name(name)
    # if os.path.exists(file_name):
    with open(file_name) as fin:
        for item in fin.readlines():
            # print(item.rstrip())
            data.append(item.rstrip())
        return data


def save(name, journal_data):
    file_name = get_file_name(name)
    print("saving at .. {}".format(file_name))
    with open(file_name, 'w') as fout:
        for items in journal_data:
            fout.write(items + '\n')


def show_all_journals():
    pass


def add_entry(text, journal_data):
    journal_data.append(text)
