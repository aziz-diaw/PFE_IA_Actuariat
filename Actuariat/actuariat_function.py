TD_88_90 = [100000, 99129, 99057, 99010, 98977, 98948, 98921, 98897, 98876, 98855, 98835, 98814, 98793, 98771, 98745,
            98712, 98667, 98606, 98520, 98406, 98277, 98137, 97987, 97830, 97677, 97524, 97373, 97222, 97070, 96916,
            96759, 96597, 96429, 96255, 96071, 95878, 95676, 95463, 95237, 94997, 94746, 94476, 94182, 93868, 93515,
            93133, 92727, 92295, 91833, 91332, 90778, 90171, 89511, 88791, 88011, 87165, 86241, 85256, 84211, 83083,
            81884, 80602, 79243, 77807, 76295, 74720, 73075, 71366, 69559, 67655, 65649, 63543, 61285, 58911, 56416,
            53818, 51086, 48251, 45284, 42203, 39041, 35824, 32518, 29220, 25962, 22780, 19725, 16843, 14133, 11625,
            9389, 7438, 5763, 4350, 3211, 2315, 1635, 1115, 740, 453, 263, 145, 76, 37, 17, 7, 2]


def qx(x, table):
    return (table[x] - table[x+1])/table[x]



def px(x, table):
    return 1 - qx(x, table)


def dx(x, table):
    return table[x] - table[x+1]

