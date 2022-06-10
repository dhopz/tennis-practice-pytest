class Score():
    def __init__(self,initial_amount=0,transactions=[]):
        self.balance = initial_amount
        self.transactions = transactions


def is_even(n): 
    # your code here
    return n%2 == 0