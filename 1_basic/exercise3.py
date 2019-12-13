# Challenge - Functions Exercise

# Create a function named tripleprint that takes a string as a parameter
# and prints that string 3 times in a row.
# So if I passed in the string "hello",
# it would print "hellohellohello"

def tripleprint(inpString):
    for x in range(3):
        if(x < 2):
            print(inpString, end = '')
        else:
            print(inpString)

tripleprint("Hello")