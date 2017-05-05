def is_sum_zero(l):
    # linear time if l is sorted (otherwise set() is O(nlog n))
    return any([True for x in l if x in set([-x for x in l if x <= 0])])

with open("lists_of_integers.txt", "r") as lists:
    for l in lists:
        print(l.strip())
        print("  ----> " + str(is_sum_zero([int(i.strip()) for i in l.split(",")])))
