'''
evens = [2]
num = 2

while evens[-1] < 50:
    num += 2
    evens.append(num)

print(evens)
'''

evens = []
for num in range(2, 51, 2):
    evens.append(num)
print(evens)
