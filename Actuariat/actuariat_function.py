TD_88_90 = [100000, 99129, 99057, 99010, 98977, 98948, 98921, 98897, 98876, 98855, 98835, 98814, 98793, 98771, 98745,
            98712, 98667, 98606, 98520, 98406, 98277, 98137, 97987, 97830, 97677, 97524, 97373, 97222, 97070, 96916,
            96759, 96597, 96429, 96255, 96071, 95878, 95676, 95463, 95237, 94997, 94746, 94476, 94182, 93868, 93515,
            93133, 92727, 92295, 91833, 91332, 90778, 90171, 89511, 88791, 88011, 87165, 86241, 85256, 84211, 83083,
            81884, 80602, 79243, 77807, 76295, 74720, 73075, 71366, 69559, 67655, 65649, 63543, 61285, 58911, 56416,
            53818, 51086, 48251, 45284, 42203, 39041, 35824, 32518, 29220, 25962, 22780, 19725, 16843, 14133, 11625,
            9389, 7438, 5763, 4350, 3211, 2315, 1635, 1115, 740, 453, 263, 145, 76, 37, 17, 7,
            2]

TV_88_90 = [100000, 99352, 99294, 99261, 99236, 99214, 99194, 99177, 99161, 99145, 99129, 99112, 99096, 99081, 99062,
            99041, 99018, 98989, 98955, 98913, 98869, 98823, 98778, 98734, 98689, 98640, 98590, 98537, 98482, 98428,
            98371, 98310, 98247, 98182, 98111, 98031, 97942, 97851, 97753, 97648, 97534, 97413, 97282, 97138, 96981,
            96810, 96622, 96424, 96218, 95995, 95752, 95488, 95202, 94892, 94560, 94215, 93848, 93447, 93014, 92545,
            92050, 91523, 90954, 90343, 89687, 88978, 88226, 87409, 86513, 85522, 84440, 83251, 81936, 80484, 78880,
            77104, 75136, 72981, 70597, 67962, 65043, 61852, 58379, 54614, 50625, 46455, 42130, 37738, 33340, 28980,
            24739, 20704, 16959, 13580, 10636, 8118, 6057, 4378, 3096, 2184, 1479, 961, 599, 358, 205, 113, 59, 30, 14,
            6, 2]
TH_00_02 = [100000, 99511, 99473, 99446, 99424, 99406, 99390, 99376, 99363, 99350, 99338, 99325, 99312, 99296, 99276,
            99250, 99213, 99163, 99097, 99015, 98921, 98820, 98716, 98612, 98509, 98406, 98303, 98198, 98091, 97982,
            97870, 97756, 97639, 97517, 97388, 97249, 97100, 96939, 96765, 96576, 96369, 96141, 95887, 95606, 95295,
            94952, 94575, 94164, 93720, 93244, 92736, 92196, 91621, 91009, 90358, 89665, 88929, 88151, 87329, 86460,
            85538, 84558, 83514, 82399, 81206, 79926, 78552, 77078, 75501, 73816, 72019, 70105, 68070, 65914, 63637,
            61239, 58718, 56072, 53303, 50411, 47390, 44234, 40946, 37546, 34072, 30575, 27104, 23707, 20435, 17338,
            14464, 11852, 9526, 7498, 5769, 4331, 3166, 2249, 1549, 1032, 663, 410, 244, 139, 75, 39, 19, 9, 4, 2, 1, ]

TF_00_02 = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000,
            100000, 100000, 100000, 100000, 99988, 99977, 99967, 99957, 99947, 99936, 99925, 99913, 99900, 99883, 99863,
            99839, 99810, 99777, 99742, 99707, 99672, 99637, 99602, 99563, 99521, 99474, 99423, 99366, 99302, 99233,
            99157, 99074, 98981, 98879, 98767, 98643, 98507, 98358, 98196, 98004, 97799, 97580, 97348, 97104, 96847,
            96574, 96282, 95971, 95639, 95264, 94870, 94453, 94011, 93538, 93030, 92482, 91838, 91137, 90373, 89539,
            88625, 87621, 86518, 85306, 83972, 82501, 80663, 78625, 76365, 73863, 71094, 68034, 64662, 60971, 56968,
            52685, 48172, 43502, 38776, 33634, 28742, 24153, 19509, 15400, 11857, 8888, 6470, 4563, 3110, 2043, 1289,
            779, 450, 246, 127, 63, 29, 13, 6, 1]

tables = [TD_88_90, TV_88_90, TH_00_02,TF_00_02]


def qx(x, table):
    if x >= len(table) - 1:
        return 1
    else:
        return (table[x] - table[x + 1]) / table[x]


def px(x, table):
    if x >= len(table) - 1:
        return 0
    else:
        return 1 - qx(x, table)


def dx(x, table):
    if x >= len(table) - 1:
        return 0
    else:
        return table[x] - table[x + 1]


def npx(x, n, table):
    if x >= len(table) - 1:
        return 0
    return table[x + n] / table[x]


def nqx(x, n, table):
    return 1 - npx(x, n, table)
