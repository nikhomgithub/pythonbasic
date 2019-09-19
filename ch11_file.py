def read_file(file_name):
    a_file=open(file_name,"r")
    if(a_file.readable()):
        print(a_file)
        print(a_file.readline())
        print(a_file.read())
    else:
        print("File can not be read")

    a_file.close()

read_file("content.txt")
"""
<_io.TextIOWrapper name='content.txt' mode='r' encoding='UTF-8'>
table of content

ch01 = string
ch02 = number
ch03 = list
ch04 = tuple
"""

def read_file2(file_name):
    a_file=open(file_name,"r")
    if(a_file.readable()):
        for l in a_file.readlines():
            print(l)
        a_file.close()
    else:
        print("File can not be read")

    
read_file2('content.txt')
"""
table of content
ch01 = string
ch02 = number
ch03 = list
ch04 = tuple
"""

def write_file(file_name,new_line):
    a_file=open(file_name,"a")
    if(a_file.readable()):
        a_file.write(new_line)
        print(a_file.read())
        a_file.close()
    else:
        print("File can not be read")


write_file("copy.txt","\nNew Line...")