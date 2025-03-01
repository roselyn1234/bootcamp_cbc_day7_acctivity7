import os

def create_file(filename, content):
    with open(filename, 'w') as f: f.write(content)

def read_file(filename):
    with open(filename, 'r') as f: print(f.read())

def append_file(filename, content):
    with open(filename, 'a') as f: f.write(content)

def delete_file(filename):
    os.remove(filename)
create_file('test.txt', 'HELLO GUYS,!')
read_file('test.txt')
append_file('test.txt', '\nAppended text.')
read_file('test.txt')
delete_file('test.txt')
