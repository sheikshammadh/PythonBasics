try:#try block will execute first and risky code will be written here
    a = int(input("Enter First Number"))
    b = int(input("Enter Second Number"))
    print(a+b)
except TypeError as te:#handle the exception
    print("Type Mismatch")

except ValueError as ve:#handle the exception
    print("Unable to Convert")

finally:
    print("finally Block will execute always")#finally block will execute always