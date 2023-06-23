def dna_seq():
    a=str(input("ENTER THE String "))
    count=0
    index=0
    print("LENGTH IS: ",len(a))
    for i in range(len(a)):
        if a[index]=="a":
            count+=1
        index+=1
    print("A's in this sting are ",count)
dna_seq()