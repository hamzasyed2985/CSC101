a= str(input("ENTER FOUR DIGIT NUMBER"))
if len(a)>3 and len(a)<=4:
     if (a[0]==a[3]) and (a[1]==a[2]):
         print("Palindrome ",a)
     else:
         print("Not Palindrome ",a)
else:
        print("PLEASE ENTER 4 DIGIT NUMBER:")