
def mydec(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)*n
        return wrapper
    return decorator

@mydec
def one(n):
    #start = datetime.now()
    l = []
    for i in range(n):

            l.append(i)
    #print(datetime.now() - start)
    return l



if __name__ == "__main__":
    # l1 = one(9)
    # print(l1)
