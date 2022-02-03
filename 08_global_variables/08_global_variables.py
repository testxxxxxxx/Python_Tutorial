x = "Server"

def myFunction():
    global x
    x = "New Server"
    print(x)

myFunction()
print(x)