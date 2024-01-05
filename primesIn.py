numbers = []
primes = []

firstNum = int(input("What is the first number? "))
secondNum = int(input("What is the second number? "))
for number in range(firstNum + 1, secondNum):
    numbers.append(number)

for num in numbers:
    for i in range(2, num):
        flag = False
        if num == 1 or num == 2:
                flag = True
                break
        elif num % i == 0:
                flag = True
                break
    if flag == False:
        primes.append(num)
# Prints the amount of primes (The primes list is the list which contains all the primes)
print(f"The amount of primes in between {firstNum} and {secondNum} (excluding {firstNum} and {secondNum}) is {len(primes)}")
