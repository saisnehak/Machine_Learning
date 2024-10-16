def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def mult(a,b):
    return a*b

while True:
    a=float(input("Enter a:"))
    b=float(input("Enter b:"))
    
    print("Press 1 = Addition")
    print("Press 2 = Subtraction")
    print("Press 3= Multiplication")
    print("Press 4= Division")
    choice=int(input("Press:"))

    if choice==1:
        print(add(a,b))
        
    elif choice==2:
        print(sub(a,b))
    elif choice==3:
        print(mult(a,b))
    elif choice==4:
    
            if b==0:
                print("zero Division Error")
            else:
                print(a/b)
       
    else:
        
        print("Invalid input")
    print("Do you want to input again press 1 or 0")
    n=int(input())

    if n==0:
        
        break
    