result, num = "", 26
while num > 0:
    result += chr((num - 1) % 26 + 65)
    num = (num - 1) // 26
print(result[::-1])
