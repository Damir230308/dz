def reversed_number(number):
    return str(number) if number < 10 else str(number % 10) + reversed_number(number // 10)

number = int(input("Write u number in this --> : "))
print(f'Your number: {reversed_number(number)}')
