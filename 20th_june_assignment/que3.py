try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or not



#  output:  An exception
#    error occured - NameError : Hi there
