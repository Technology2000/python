mylist=[]
def mean(myList):
    result_mean=sum(myList)/len(myList)
    return result_mean
n=int(input("Enter the number of elements in the list")) 
for i in range(n):
    num=int(input("Enter list elements"))
    mylist.append(num)
print("mean= ",mean(mylist))    
