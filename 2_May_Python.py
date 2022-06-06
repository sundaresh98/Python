##var=10/0
##print(var)
##print("welcome")
##

##try:
##    var=10/0
##    print(var)
##except:
##    print("sorry try again")
##    

##try:
##    var="A"+ 10
##    print(var)
##except TypeError:
##    print("sorry try again")
##print("welcome")
  
##try:
##    var="A"+ 10
##    print(var)
##except TypeError:
##    print("sorry try again")
##except ZeroDivisionError:
##    print("sorry")
##print("welcome")
  

##try:
##    var=10/0
##    print(var)
##except TypeError as ex:
##    print("sorry try again") 
##except ZeroDivisionError as ex:
##    print(ex)
##print("welcome")

##try:
##    var=10/0
##    print(var)
##except (TypeError,ZeroDivisionError) as ex:
##    print(ex) 
##except:
##    print("welcome")



##try:
##    var=10/0
##    print(var)
##except (TypeError,ZeroDivisionError) as ex:
##    print(ex) 
##except:
##    print("welcome")
##else:
##    print("sundaresh")
##finally:
##    print("praveen")

##try:
##    var=10/2
##    print(var)
##except (TypeError,ZeroDivisionError) as ex:
##    print(ex) 
##except:
##    print("welcome")
##else:
##    print("sundaresh")
##finally:
##    print("praveen")


##try:
##    var=10
##    if var>5:
##       raise IndexError
##except IndexError as ex:
##    print(ex)







##try:
##    var=10
##    if var>5:
##       raise MyError
##except MyError as ex:
##    print(ex)
##
##It would be error it can be done by


##class MyError(Exception):
##    pass
##try:
##    var=10
##    if var> 5:
##        raise MyError
##except MyError:
##    print("Exception")

class MyError(Exception):
    my_data = "user defind in data"
try:
    var=10
    if var> 5:
        raise MyError
except MyError as ex:
    print(ex.my_data)

    







  
