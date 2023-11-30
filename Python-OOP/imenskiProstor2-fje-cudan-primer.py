#### 

def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function

my_function = outer_function("Hi")

print(type(my_function))
my_function()    

