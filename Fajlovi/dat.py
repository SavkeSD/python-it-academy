file = open('python-it-academy/Fajlovi/file_path.txt', 'a')  # file je descriptor u stvari
file.write('Hello World !!! \n')
file.close()

file = open('python-it-academy/Fajlovi/file_path.txt', 'a')
try:
    file.write('Hello World iz try blocka \n')
finally:
    file.close()


with open('python-it-academy/Fajlovi/file_path.txt', 'a') as file:    ### Ovo je skraceni zapis trya i finallyija
    file.write('Hello World iz one liner-a \n')


class MessageWriter2:
    def __init__(self, file_name):
        self.file_name = file_name
 
    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file
 
    def __exit__(self, *args):
        self.file.close()
 
 
# using with statement with MessageWriter
 
with MessageWriter2('my_file.txt') as xfile:
    xfile.write('hello world.........')