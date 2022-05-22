
def repeat(random_):
    print()
    def wrapper(*args, **kwargs):
        print()
        def wrapper_2(*args, **kwargs):
            print()
            wrapper = wrapper_2(wrapper)
            random_ = wrapper(random_)
            return random_
        return wrapper_2()
    return wrapper()

    count = 0
    while True:
        #if n > 0:
            return n
            count += 1
@repeat
def ramdom_(n):
    return (i for i in range(n))



if "__name__" == "__main__":


    print(ramdom_(4))