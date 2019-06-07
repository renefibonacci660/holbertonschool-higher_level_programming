#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    '''
        Contains function that inserts a line of text to a file,
        after each line containing a specific string 
    '''
    MynewStr = ""
    with open(filename, mode='r', encoding='utf-8') as a_file:
        for line in a_file:
            MynewStr += line
            if search_string in line:
                MynewStr += new_string

    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(MynewStr)
