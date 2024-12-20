def outer():
    print("hi")
    def inner():
        print("hello")
    return inner
inner=outer()
inner()
inner()