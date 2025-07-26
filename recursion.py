
#this is the example of infinite recursion
# def greet():
#     print("govind")
#     greet()
# greet()

#print "Govind" 5 times using recursion

count=0
def name():
    global count
    if count==5:
        return
    print("Govind")
    count+=1
    name()
name()