def out_function(nout):
    def inner_function():
        return nout * nout
    return inner_function

a = out_function(1)
b = out_function(2)
print(a(),b())