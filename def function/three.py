def login(user,password):
    if (user=='rahul' and password=='i love india'):
        print("hi",user,"login success")
    else:
        print('login failed')

login('rahul',123)
login('rahul','i love india')
