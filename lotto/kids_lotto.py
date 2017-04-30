from random import shuffle

def make_lists(kids,t):
    shuffle(kids)
    kids += kids
    # duplicate list: easier than using modulo in the list comprehension
    return [kids[i:i+t+1] for i in range(0,int(len(kids)/2))]

with open("kids_lotto.txt", "r") as lines:
    content = [x.strip() for x in lines.readlines()]
    print(make_lists(content[0].split(";"),int(content[1])))
