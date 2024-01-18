# 9.1
def good():
    list_a = ['Harry', 'Ron', 'Hermione']
    print(list_a)

# 9.2
def get_odds(start=1, end=10, step=2):
    while start < end:
        yield start
        start = start + step

num_list = []
for i in get_odds():
    num_list.append(i)
    if num_list.index(i) == 2:
        print(i)
    else:
        pass

# 9.3
def test_func(func):
    def inner_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return inner_func

# 9.4
class OopsException(Exception):
    def __init__(self):
        super().__init__('Caught an oops')

def raise_exception():
    try:
        a = 3
        if a % 3 == 0:
            raise OopsException
    except OopsException as e:
        print(e)

raise_exception()

