chars = ["a", "c", "x", "d", "p", "a", "m", "q", "s", "t", "p", "a", "t", "c"]

dicChars = {}

for char in chars:
    if char not in dicChars:
        dicChars[char] = 1
    else:
        dicChars[char] += 1
    # if char not in dicChars:
    #     dicChars[char] = chars.count(char)
print(dicChars)

vs = dicChars.values()
max_count = max(vs)

for k, v in dicChars.items():
    if v == max_count:
        print(k)
