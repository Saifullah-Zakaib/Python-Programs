number=int(input("Enter the Number:"))
def check(number):
    if number & 1==0:
        print("Even Number")
    else:
        print("Odd Number")
check(number)