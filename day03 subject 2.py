# 6.1
for i in range(3,-1,-1):
    print(i)

# 6.2
guess_me = 7
number = 1
while number != guess_me:
    if number < guess_me : print("too low")
    elif number > guess_me : print("oops")
    number = number + 1
print('found it')

# 6.3
guess_me = 5
for number in range(10):
    if number < guess_me:
        print("too low")
    elif number > guess_me:
        print("too high")
    else:
        print('found it')


