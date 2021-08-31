def decorator(func):

    def wrapper(*args,**kwargs):
            print("This is decorated")
            print(func(*args,**kwargs))

    return wrapper

@decorator
def isThisDecorated(text):
    print(text)
    return text

isThisDecorated('damn')
