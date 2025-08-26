def memoize(funs):
    cache ={}
    def wrapper(*args,**kwargs):
        key=(args,tuple(sorted(kwargs.items())))

        if key in cache:
            print(f"fetching from cache for{args} {kwargs}")
            return cache[key]
        print(f"computing from cache for {args} {kwargs}")

        result=funs(*args,**kwargs)
        cache[key]=result
        return result
    return wrapper

def fibonacci(n):
    if (n <=1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))
print(fibonacci(15))




 