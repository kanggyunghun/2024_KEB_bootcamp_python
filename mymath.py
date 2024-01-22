def is_prime(num) -> bool: # help() 와 같이 사용
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean으로 리턴
    :param num: 판정할 매개변수
    :return: 소수면 True, 소수가 아니면 False
    """
    if num < 2:
        return False
    else:
        i = 2
        while i*i <= num:
            if num % i == 0:
                return False
            i += 1
        return True