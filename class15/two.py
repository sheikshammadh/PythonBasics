def outer():
    print("inside outer function")
    def inner():
        print("inside inner function")
    
outer()
inner()# name error.