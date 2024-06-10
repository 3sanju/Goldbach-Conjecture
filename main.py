#Check for prime
def prime(num):
    if num<=1:
        return False
    for i in range(2,(num//2)+1):
        if num%i==0:
            return False
    return True

#Check for even
def even(num):
    if num%2==0:
        return True
    return False

#To check goldbach condition
def goldbach(num):
    flag=False
    t=[]
    if not prime(num) and num<=2:
        return False
    for i in range(2,num):
        if prime(i) and prime(num-i):
            t.append((i,num-i))
            print(t)
            sum=i+(num-i)
            if(sum==num):
              flag= True
    if flag==True:
        return True
    else:
        return False
    
#Main code for goldbach
def check_goldbach(num):
    if even(num) and num>2:
        if goldbach(num):
            print("goldbach's number")
        else:
            print("not goldbach's number")
    else:
        print("Invalid number")

#Driver's code
number=int(input("enter the number"))
check_goldbach(number)
