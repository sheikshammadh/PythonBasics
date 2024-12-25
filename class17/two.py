def login_status(func):
    def inner(name,login_status):
        if status==False:
            print("login required")
        else:
            func(name,login_status)
    return inner
login_status(name,login_status)
   
