##var={"name":"kholi", "age":55}
##for x in var:
##    print(x)




##var={"name":"kholi", "age":55}
##for x in var.items():
##    print(x)


##var={"name":"kholi", "age":55}
##for x in var.values():
##    print(x)



##var={"name":"kholi", "age":55}
##for key,value in var.items():
##    print(key)
##    print(value)


##output= {0.0,1.1,1.2,1.3}
##output={}
##for x in range(4):
##    output[x]=x*x
##    print(output)

##dictionary comprehension
##getting the output in onesort of line

##output={x:x*x for x in range(4)}
##print(output)


##output=[]
##for x in range(10):
##    if x%2==0:
##        output.append(x)
##print(output)

##list comprehension
##getting the output in onesort of line


##output=[x for x in range(10) if x%2==0]
##print(output)





##Removing the index by using pop, clear and delete

##in this it will remove the last index because index is not mentioned
##var=[1,2,3]
##var.pop()
##print(var)

##this can be done in pop method only it will remove the 0 th index
##var=[1,2,3]
##print (var.pop())




##in this we have pop to remove 2 index
##var=[1,2,3]
##var.pop(2)
##print(var)

##in these it will clear all the function
##var=[1,2,3]
##var.clear()
##print(var)

##in these we have delete the var so it deletes the whole var and output will error
##var=[1,2,3]
##del var
##print(var)









##in this we are commenting to delete the index 2 and index 2 will be deleted 
##var=[1,2,3]
##del var[1]
##print(var)


