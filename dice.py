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
print("rolls is: ", rolls)

highh = max(rolls)
loww = min(rolls)

print("low is " + str(loww) + "  high is " + str(highh))

resoo = 3
y_list = []
y_steps = 0
yy = loww
while yy < highh:
    # yy = yy + (y_steps * resoo)
    # yy = yy + resoo
    # print("yy is " + str(yy))
    y_list.append(yy)
    yy = yy + resoo
    # y_steps = y_steps + 1
# print("yy is " + str(yy))
y_list.append(yy)

print(y_list)

"""
create dictionary of dice and frequency
"""
rolls_dct = {i: rolls[i] for i in range(0, len(rolls), 1)}
print("rolls_dct is: ", rolls_dct)

"""
print heading
"""
# print('\n' * 10)
print("       ", end='')
for key in rolls_dct:
    print("      ", end='')
    print(str(key + 1), end='')
print()
# print("--__-__--", end='')

# print("where are the underlines ___?")
print("       ", end='')
print("     ---", end='')
print("    ---", end='')
print("    ---", end='')
print("    ---", end='')
print("    ---", end='')
print("    ---", end='')
print()

print("        ", end='')
for key in rolls_dct:
    print("    " + str(rolls_dct[key]), end='')
print('\n' * 10)


