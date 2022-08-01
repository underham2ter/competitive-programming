def calc_weight(boo, cols, rows):
    goo = {}
    for i in range(0, len(boo[0])):
        for j in range(len(boo)):
            if i not in cols: goo[f'col{i}'] = goo.get(f'col{i}', 0) + boo[j][i]
            if j not in rows: goo[f'row{j}'] = goo.get(f'row{j}', 0) + boo[j][i]
    return sorted(goo.items(), key=lambda x: x[0])


def min_row(boo):
    goo = {}
    for i in range(0, len(boo[0])):
        for j in range(len(boo)):
            goo[j] = goo.get(j, 0) + boo[j][i]
    return min(goo.items(), key=lambda x: x[1])


def min_col(boo):
    goo = {}
    for i in range(0, len(boo[0])):
        for j in range(len(boo)):
            goo[i] = goo.get(i, 0) + boo[j][i]
    return min(goo.items(), key=lambda x: x[1])


for v in range(int(input())):
    cols, rows = [], []
    h, d = list(map(int, input().split()))

    # moo = [[0 for d in range(d)] for h in range(h)]
    # for i in range(d):
    #     for j in range(h):
    #         moo[i][j] = int(input())
    moo = [list(map(int, input().split())) for h in range(h)]
    c, r = min_col(moo), min_row(moo)
    while c[1] < 0 or r[1] < 0:
        if r[1] < c[1]:
            # moo = list(map(lambda x: [*x[0:c[0]], -x[c[0]], *x[c[0]+1:d]], moo))
            for i in range(d):
                moo[r[0]][i] *= -1
            rows.append(r[0])
        else:
            for i in range(h):
                moo[i][c[0]] *= -1
            cols.append(c[0])
            # moo[r[0]] = list(map(lambda x: -x, moo[r[0]]))

        c, r = min_col(moo), min_row(moo)
    R, C = [], []
    for i in list(filter(lambda x: rows.count(x) % 2 == 1, rows)):
        if i not in R: R.append(i)

    for i in list(filter(lambda x: cols.count(x) % 2 == 1, cols)):
        if i not in C: C.append(i)

    print("Yes")
    print(len(R))
    # print(*map(lambda x: x+1, sorted(rows)))
    # print(*map(lambda x: x+1, rows))
    for i in R:print(i+1, end=' ')
    print()
    print(len(C))
    # print(*map(lambda x: x+1, sorted(cols)))
    for j in C:print(j+1, end=' ')
    # print(*map(lambda x: x+1, cols))









