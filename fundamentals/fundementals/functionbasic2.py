def countdown(x):
    Thelist = []
    for i in range(x,-1,-1):
        Thelist.append(i)
    return Thelist
print(countdown(5))


# = the list

def print_return(x):
    print(x[0])
    return x[1]
print(print_return([1,2]))


#x = the list

def firstplusarray(x):
    return x[0] + len(x)
print(firstplusarray([1,2,3,4,5,]))

#x = the list
#y = output

def biggerthan2nd(x):
    if len(x) < 2:
        return False
    y = []
    for i in range(0,len(x)):
        if x[i] > x[1]:
            y.append(x[i])
    print(len(y))
    return y
print(biggerthan2nd([5,2,3,2,1,4]))
print(biggerthan2nd([3]))

#x = length
#y = num
#z= output

def lengthvalue(x,y):
    output =[]
    for i in range(0,x):
        output.append(y)
    return output
print(lengthvalue(4,7))
print(lengthvalue(7,4))