print("-----------SIMPLE CALCULATOR---------")
a=0

while(a == 0):
    a = float(input("Enter the first number"))
    b = float(input("Enter the second number"))

    print("Enter 1 if you want to add them")
    print("Enter 2 if you want to subtract them")
    print("Enter 3 if you want to multiply them")
    print("Enter 4 if you want to divide them")
    

    c = int(input("Enter your choice"))

    if(c == 1):
        print(a + b)

    if(c == 2):
        print(a - b)

    if(c == 3):
        print(a * b)

    if(c == 4):
        if(b == 0):
            print("DIVISION BY ZERO IS NOT POSSIBLE!!!!")
            continue
        else:
            print(a / b)
    print("Enter 5 if you want to perform another calculation")
    print("Enter 6 if you want to exit")
    ch = int(input("Enter your choice "))
    if(ch==5):
        a =0
        
    if(ch==6):
       a = a + 1
print("------------Thank you!!------------")        
