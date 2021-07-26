import keyword
list=["if","else","Hii","for","sravani"]
def foo(li):
    for i in range(len(li)):
        if keyword.iskeyword(li[i]):
            print(li[i]+" :is a keyword")
        else:
            print(li[i]+" :is not a keyword")

foo(list)     
