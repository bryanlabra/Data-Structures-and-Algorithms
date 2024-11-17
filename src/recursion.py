def recursion(count):
    if count == 500:
        return 0
    else:
        print(f"hello world {count+1}")
        recursion(count+1)

#count = 0
#recursion(count)
############ CONTROL OF A FUNCTION ###################

def fun():
    val = 10
    return val

def example():
    print("UL")
    x = fun()
    y = 20
    result = x + y
    return result

#example()
######################################### all is good

def fun():
    val = 10
    return val

def example():
    print("UL")
    x = fun() * 2  #this is fine
    y = 20
    result = x + y + fun() #what happens here?  result = (x=20) + (y=20) + (func()=10)
    return result

#example()
################### Tracing Tree ###################### 

def run1(n):
    if n == 0:
        return  #base case will never be reached if n never changes

    print(n)
    run1(n-1) #key

#n = 3
#run1(n)
#print("completed")

######################################### 

def run2(n):
    if n == 0:
        return
    print(n)
    run2(n-1)

#n = 3
#run2(n)
#print("completed")

######################################### 

def run3(n):
    if n == 0:
        return
    print(n)
    run3(n-1)

#n = 3
#run3(n)
#print("completed")

###############  flipping print and run function  ################ 

def run4(n):
    if n == 0:
        return
    run4(n-1) #how does the output change when you move this line before the print statement
    print(n)

#n = 3
#run4(n)
#print("completed")

######################################### 

def run5(n):
    if n == 0:
        return
    
    print(f"UL {n}")
    run5(n-1)
    print(f"UL {n}")

#n = 3
#run5(n)
#print("completed")

############################# CALL STACK ############### 

def run6(n):
    if n == 0:
        return
    
    print(f"")
    run5(n-1)

n = 3
run6(n)