#revise decorator.
def trytolog(func):
    def inner(name,status):
        if status==False:
            print("login required")
        else:
            func(name,status)
    return inner
@trytolog
def profilelog(name,status):
    print("prfile page")

profilelog("shyam",False)
