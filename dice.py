"""
/home/thuston88/Downloads/GIT/dice-pareto-chart/dice.py
"""
import random
# print("roll of dice equals " + str(random.randint(1,6)))
minn = 1
maxx = 6
rolls = [0, 0, 0, 0, 0, 0, 0]
cntt = 0
highh = 0
loww = 0

"""
generate 5000 data points
"""
while cntt < 5000:
    dice = random.randint(minn, maxx)
    # print("this dice roll is: ", dice)
    rolls[dice] = rolls[dice] + 1
    cntt = cntt + 1
    # print(cntt)

"""
remove zero item
"""
# print(rolls)
rolls.remove(0)
# print("rolls is: ", rolls)

resoo = 3
highh = max(rolls)
loww = min(rolls) - (2 * resoo)

# print("low is " + str(loww) + "  high is " + str(highh))

y_list = []
y_steps = 0
yy = loww
col = [" ", " ", " ", " ", " ", " ", " "]

while yy < highh:
    # yy = yy + (y_steps * resoo)
    # yy = yy + resoo
    # print("yy is " + str(yy))
    y_list.append(yy)
    yy = yy + resoo
    # y_steps = y_steps + 1
# print("yy is " + str(yy))
y_list.append(yy)
y_list.reverse()

# print(y_list)

"""
create dictionary of dice and frequency
"""
rolls_dct = {i: rolls[i] for i in range(0, len(rolls), 1)}


"""
print heading
"""
print('\n' * 10)
print("rolls_dct is: ", rolls_dct)
print("  " + "CNT" + "  ", end='')
for key in rolls_dct:
    print("      ", end='')
    print(str(key + 1), end='')
print()
# print("--__-__--", end='')

# print("where are the underlines ___?")
print("  ---   ", end='')
print("    ---", end='')
print("    ---", end='')
print("    ---", end='')
print("    ---", end='')
print("    ---", end='')
print("    ---", end='')
print()

"""
print("        ", end='')
for key in rolls_dct:
    print("    " + str(rolls_dct[key]), end='')
print('\n' * 10)
"""
for s in y_list:
    axis = "  " + str(s) + "   "
    for key in rolls_dct:
        # print("key is: " + str(key) + "  s is: " + str(s) +
        #      "  rolls_dct[key] is: " + str(rolls_dct[key]))

        if rolls_dct[key] > s:
            col[key + 1] = "    " + str(rolls_dct[key])
        else:
            col[key + 1] = "       "

    col_total = col[1] + col[2] + col[3] + col[4] + col[5] + col[6]
    print(axis + col_total)
