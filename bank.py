greeting = input("Enter greeteing: ").lower()
greeting = greeting.lstrip()
if greeting.startswith('hello'):
    print('$0')
elif greeting.startswith('h'):
    print('$20')
else:
    print('$100')     