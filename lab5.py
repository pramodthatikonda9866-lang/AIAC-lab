number = int(input("Enter a number: "))

if number > 1:
	divisor_sum = sum(divisor for divisor in range(1, number) if number % divisor == 0)
	if divisor_sum == number:
		print(f"{number} is a perfect number.")
	else:
		print(f"{number} is not a perfect number.")
else:
	print(f"{number} is not a perfect number.")
# generate a code where it should check the given input is a perfect number or not