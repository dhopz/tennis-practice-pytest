class Score():
    def __init__(self,initial_amount=0,transactions=[]):
        self.balance = initial_amount
        self.transactions = transactions


def is_even(n): 
    # your code here
    return n%2 == 0

def paul(x):
    points = {'kata':5, "Petes kata":10, "life":0, "eating":1}
    score = 0

    for i in x:
        score += points[i]

    if score < 40:
        return "Super happy!"
    elif score < 70:
        return "Happy!"
    elif score < 100:
        return "Sad!"
    else:
        return "Miserable!"