phrase = "Coding For All"
print(phrase[0:6])

print(phrase.find("Coding"))

print(phrase.replace("All", 'Everyone'))

print(phrase.startswith("Coding"))
print(phrase.endswith("coding"))

print('I hope everyone is enjoying the Python Challenge.\nAre you ?')
print('Name\tAge\tCountry\tCity')
print('Naing\t250\tUK\tLandon')

phrase_2 = '   Coding For All      '

print(phrase_2.strip("   "))

identifier_phrase1 = "30DaysOfPython"        #False
identifier_phrase2 = "thirty_days_of_python" #True

print(identifier_phrase1.isidentifier())
print(identifier_phrase2.isidentifier())

a = 5
b = 4
print("{} + {} = {}".format(a,b,a + b))

Cuz_repeat = 'You cannot end a sentence with because because because is a conjunction'
print(Cuz_repeat.find("because"))