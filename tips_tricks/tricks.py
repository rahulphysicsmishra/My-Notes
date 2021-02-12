# Python shortcuts
# Ternary conditions
condition = True

if condition:
    x = 1
else:
    x = 0

print(x)

# Another shortcut to do the same thing

x = 1 if condition else 0
print(x)


print('*'*100)
# Large Numbers

num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2
print(total)

# To make it look easily read
print(f'{total:,}')

# looping example shortcut
print('*'*100)
# bad way
names = ['Hari', 'Narayan', 'Govind', 'Narsimha']

index = 0
for name in names:
    print(index, name)
    index += 1

# Good and easy way
# No need for index = 0 variable
for index1, name in enumerate(names, start=1):  # start = 0 is by default after names parameter in enumerate
    print(index1, name)




