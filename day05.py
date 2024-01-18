def squares(*n):
    """
    넘겨 받은 수치 데이터들의 거듭제곱을 리스트에 담아서 리턴
    :param n: tuple
    :return: list
    """
    return [pow(i,2) for i in n]

def run_function(func, *number ):
    return func(*number)

print(run_function(squares,9,10))