def swap(x,y): 
    print("Before swapping a :",x)
    print("Before swapping b :",y)
    #logic to swap without using third variable 
    x,y=y,x
    return x,y 

a=int(input("Enter value : "))
b=int(input("Enter value : "))    
a,b=swap(a,b) 
print("After swapping a becomes :",a)
print("After swapping b becomes :",b)