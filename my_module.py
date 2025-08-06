def prime_num(num)-> int :
    if num <= 1:
        return False
    for i in range(2,int(num)): 
        if num % i == 0:
            return False
    return True

def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s
