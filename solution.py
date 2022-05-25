# my solution to https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7021
def func(I, P, tc):
    len_p = len(P)
    len_i = len(I)
    if I == P:
        return f"Case #{tc}: 0"
    elif len_p < len_i:
        return f"Case #{tc}: IMPOSSIBLE"
    idx_p = 0
    idx_i = 0
    while idx_p < len_p and idx_i < len_i:
        p = P[idx_p]
        i = I[idx_i]
        if i!=p:
            if i not in P[idx_p:] or len(I[idx_i:])>=len(P[idx_p:]):
                return f"Case #{tc}: IMPOSSIBLE"
            idx_p +=1
            continue
        idx_p +=1
        idx_i +=1
    if idx_i == len_i:
        counter = len_p-len_i
        return f"Case #{tc}: {counter}"
    else:
        return f"Case #{tc}: IMPOSSIBLE"
t = int(input())
tc = 0
while t>0:
    I = input()
    P = input()
    tc += 1
    print(func(I, P, tc))
    t -= 1
