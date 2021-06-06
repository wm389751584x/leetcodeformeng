env = [[5,4],[6,4],[6,7],[2,3]]

a = sorted(env, key=lambda x: (x[0]))

b = sorted(env, key=lambda x: -x[0])

print(a)
print(b)