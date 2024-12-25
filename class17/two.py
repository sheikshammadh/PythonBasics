def login_required(func):
    def inner(name,status):
        if status== False:
            print("login required")
        else:
            func(name,status)

    return inner

def home_page(name,login_status):
    print("home page")
def about_page(name,login_status):
    print("about page")
@login_required
def history_page(name,login_status):
    print("history page")
@login_required
def profile_page(name,login_status):
    print("profile page")   
home_page("shyam",True)
about_page("shyam",True)
history_page("shyam",False)
profile_page("shyam",False)