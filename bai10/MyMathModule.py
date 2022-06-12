def is_prime(number):
    for ele in range(number):
        if(ele > 1) and (number % ele ==0):
            return False
    return True

def plus(n1, n2):
    return n1 + n2

def divide(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    else: return n1/n2

