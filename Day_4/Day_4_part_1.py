#Day_4

a,b,c,d = "Thirty","Days","Of","Python"
print(f"{a} {b} {c} {d}")

e,f,g = 'Coding','For','All'
print(f"{e} {f} {g}")

company = "Coding For All"
print(company)

print(len(company))
print(company.upper())
print(company.lower())
print(company.title())
print(company.swapcase())

challenge = 'thirty days of python'
print(challenge.capitalize())

a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area)
print(formated_string)