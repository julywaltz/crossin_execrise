for x in range(1, 5):
    for y in range(1, 5):
        if x == y:
            continue
        for z in range(1, 5):
            if z == y:
                continue
            if z == x:
                continue
            print("%d%d%d" % (x, y, z))
