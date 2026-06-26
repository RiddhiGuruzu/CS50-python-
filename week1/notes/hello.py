# Create our own function 1

#defining a function hello that prints hello
#setting the default value of the parameter to "world"
def hello(to="world"):
    print("hello,",to)

name = input("What's your name?")
#calling the function hello witjh the argument name
hello(name)
#calling the function hello without any arguments, so it will use the default value "world"
hello()


# Create our own function 2

#creating a main function to call the hello function
#to be able to create hello function at any point in the code, we need to define the main function and call it at the end of the code. 
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,",to)

main()
