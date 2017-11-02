def edit_distance(s, t):
    array = [[0 for x in range(len(t) + 1)] for y in range(len(s) + 1)]

    for x in range(len(t) + 1):
        array[0][x] = x
    for x in range(len(s) + 1):
        array[x][0] = x

    for j in range(1, len(t) + 1):
        for i in range(1, len(s) + 1):

            insert = array[i][j - 1] + 1
            delete = array[i - 1][j] + 1
            match = array[i - 1][j - 1]
            mismatch = array[i - 1][j - 1] + 1
            if s[i - 1] == t[j - 1]:
                array[i][j] = min(insert, delete, match)
            else:
                array[i][j] = min(insert, delete, mismatch)

    return array[i][j]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
