def find_last_index(n, bool_cond):
    for i,d in enumerate(reversed(n)):
        if bool_cond(i,d,n):
            return len(n)-i-1

def next_string(n):
    ind = find_last_index(n, lambda i,d,n: i>0 and d < n[-i])
    # last index of small element followed by larger one
    if ind is not None:
        repl = find_last_index(n, lambda i,d,n: n[ind] < d)
        # last index of element larger than n[ind]
        return n[:ind] + n[repl] + n[-1:repl:-1] + n[ind] + n[repl-1:ind:-1]
            
while(True):
    n = input()
    print(next_string(n))
        
