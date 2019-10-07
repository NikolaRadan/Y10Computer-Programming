x=input("enter number:")
if(x.isdigit() == True):
    x = int(x)
    result = str(x*x)
    print("your result is: " + result)
else:
    print("you did not enter a number")
