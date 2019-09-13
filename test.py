for d in range(11, 99):
    sd = str(d)
    sm = sd[::-1]
    if int(sm) > int(sd):
        print(d)


def age(d, m):
    if d < m:
        d += 1; m += 1
        return d, m
