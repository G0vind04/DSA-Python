n =int(input("enter a number"))
num = n
total = 0
length = len(str(num))

while num > 0:
    digit = num % 10
    total += digit ** length
    num = num // 10

if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
