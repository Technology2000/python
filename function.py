def getInteger():
    output=int(input("Enter an integer: "))
    return output
def Main():
    print("Started")
    result=getInteger()
    return result    
if __name__=="__main__":
    op=Main()
    print("Output is: ",op)
