def rase_exception():
    age = int(input("please input your age"))
    if age >120:
        raise Exception ("please correct age")



try:
    rase_exception()
except:
    print("please input correct age")
