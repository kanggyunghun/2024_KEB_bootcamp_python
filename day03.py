univ = "inha"
# i = 0
# while i < len(univ):
#     print(univ[i])
#     i += 1

for letter in univ:
    print(letter, end='')

print()

for k in range(0,len(univ)):
    print(univ[k], end = '')

print()

for letter in univ:
    if letter == 'h':
        break
    print(letter, end='')