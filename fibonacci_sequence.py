fibonacci_length = int(input("Insert fibonacci sequence length: "))
n1, n2 = 0, 1
count=0

if fibonacci_length <=0:
    print("PLease insert positive integer")
elif fibonacci_length == 1:
    print("Fibonacci sequence upto", fibonacci_length, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count<fibonacci_length:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1

