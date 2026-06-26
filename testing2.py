print("--" * 60)
print("hello worldd")
age=int(input("Enter your age: "))
print("--" * 60)
if age > 18:
    print("you are eligible for applying loan")
    loanamount=int(input("enter the loanamount: "))
    if loanamount < 50000:
        print("eligible for loan")
        pf=int(input("enter your pf: "))
        if pf > 10000:
            print ("satisfied with pf")
            print("your loan amount will be processed")
        else:
            print("pf<10000 is not satisfied")
    else:
        print("not eligible for loan")
        
else:
    print("you are not eligible for applying the loan")
