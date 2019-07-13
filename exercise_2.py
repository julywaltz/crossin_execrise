for a in [1, 2, 3, 4]:
    for b in [1, 2, 3, 4]:
        for c in [1, 2, 3, 4]:
            if a != b and b != c and a != c:
                print('%d%d%d' % (a, b, c))
