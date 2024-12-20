def outer():
    print("inside outer function")
    def inner():
        print("inside inner function")
    inner()
    inner()
outer()
