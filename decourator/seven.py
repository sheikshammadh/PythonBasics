def outer():
    print("outer func")
    def inner():
        print("inner func")
    inner()
    inner()
    inner()
outer()
# outer func
# inner func
# inner func
# inner func
outer()
# outer func
# inner func
# inner func
# inner func
outer()
outer()
# outer func
# inner func
# inner func
# inner func
# outer func
# inner func
# inner func
# inner func

