import random
# print("roll of dice equals " + str(random.randint(1,6)))
minn = 1
maxx = 6
rolls = [0,0,0,0,0,0,0]
cntt = 0
highh = 0
loww = 0

"""
generate 5000 data points
"""
while cntt< 5000:
    dice = random.randint(minn,maxx)
    rolls[dice] = rolls[dice] + 1
    cntt = cntt + 1
    # print(cntt)

highh = max(rolls)
loww = min(rolls)

print("low is " + str(loww) + "  high is " + str(highh))

resoo = 3
y_list = []
y_steps = 0
yy = loww
while yy < highh:
    yy = yy + (y_steps * resoo)
    y_list.append(yy)
    y_steps = y_steps + 1

print(y_list)

"""
create dictionary of dice and frequency
"""
rolls_dct = {i: rolls[i] for i in range(1, len(rolls), 1)} 
# print(rolls_dct)

"""
print heading
"""
# print('\n' * 10)
print("       ", end='')
for key in rolls_dct:
    print("      " + str(key), end='')
print()

print("       ", end='')
print("     ___", end='')
print("    ___", end='')
print("    ___", end='')
print("    ___", end='')
print("    ___", end='')
print("    ___", end='')
print()


print("        ", end='')
for key in rolls_dct:
    print("    " + str(rolls_dct[key]), end='')
print('\n' * 10)


'''
dice = random.randint(minn,maxx)
print(str(dice))
rolls[dice] = rolls[dice] + 1
print(rolls[dice])

dice = random.randint(minn,maxx)
print(str(dice))
rolls[dice] = rolls[dice] + 1
print(rolls[dice])

dice = random.randint(minn,maxx)
print(str(dice))
rolls[dice] = rolls[dice] + 1
print(rolls[dice])

dice = random.randint(minn,maxx)
print(str(dice))
rolls[dice] = rolls[dice] + 1
print(rolls[dice])

dice = random.randint(minn,maxx)
print(str(dice))
rolls[dice] = rolls[dice] + 1
print(rolls[dice])

print(rolls)
'''


