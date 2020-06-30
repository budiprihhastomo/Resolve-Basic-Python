def terkecil_kedua(a, b, c, d, e, f, g, h, i, j):
    tampung = [a, b, c, d, e, f, g, h, i, j]

    def testCase(val):
        if val <= -100 or val >= 100:
            print("Bilangan tak sesuai")
            return False

    for index, a in enumerate(sorted(tampung)):
        testCase(a)
        tampung[index] = a

    return tampung[1]


print(terkecil_kedua(20, 15, 19, 11, 7, 23, 8, 11, 9, 13))
