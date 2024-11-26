# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_linear_regresion.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jutrera- <jutrera-@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/26 18:50:52 by jutrera-          #+#    #+#              #
#    Updated: 2024/11/26 18:50:52 by jutrera-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv
import matplotlib.pyplot as plt

RED    = "\033[31m"
GREEN  = "\033[32m"
BLUE   = "\033[34m"
CYAN   = "\033[36m"
YELLOW = "\033[33m"
RESET  = "\033[0m"

def read_csv_data():
	mileage = []
	price = []
	csv_file = input("Enter the name of the CSV file: ")
	try:
		with open(csv_file + ".csv", 'r') as file:
			reader = csv.reader(file)
			next(reader)  # Skip the header row
			for row in reader:
				if len(row) >= 2:
					mileage.append(float(row[0]))
					price.append(float(row[1]))
	except FileNotFoundError:
		print(f"Error: Could not find the file {csv_file}")
		return None, None
	return mileage, price

def calculate_linear_regression(x, y):
	"""Calculates the linear regression coefficients (a and b) for y = a + b * x."""
	n = len(x)
	if n == 0 or n != len(y):
		print("Error: Empty lists or lists of different lengths.")
		return None, None
	# Calculate summations
	sum_x = sum(x)
	sum_y = sum(y)
	sum_xy = sum(xi * yi for xi, yi in zip(x, y))
	sum_x2 = sum(xi**2 for xi in x)

	# Calculate slope (b) and intercept (a)
	b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
	a = (sum_y - b * sum_x) / n
	return a, b

def plot_regression(mileage, price, a, b):
	# Original data points
	plt.scatter(mileage, price, color='blue', label='Original Data')

	# Generate points for the regression line
	x_min = min(mileage)
	x_max = max(mileage)
	x_line = [x_min, x_max]
	y_line = [a + b * x_min, a + b * x_max]

	# Plot the line
	plt.plot(x_line, y_line, color='red', label=f'Regression Line: y = {a:.2f} + {b:.2f}x')

	# Configure the plot
	plt.xlabel('Mileage')
	plt.ylabel('Price')
	plt.title('Linear Regression')
	plt.legend()
	plt.grid(True)
	plt.show()

def main():
	
	mileage, price = read_csv_data()
	if mileage and price:
		a, b = calculate_linear_regression(mileage, price)
		if a is not None and b is not None:
			print(f"{YELLOW}The linear regression coefficients are:{RESET}")
			print(f"  Intercept (a): {GREEN}{a:.2f}{RESET}")
			print(f"  Slope     (b): {GREEN}{b:.2f}{RESET}")
			print(f"{YELLOW}Equation:{RESET}")
			print(f"  y = {GREEN}{a:.2f}{RESET}", end = '')
			if (b < 0):
				print(f" - {GREEN}{-b:.2f}{RESET}x")
			else:
				print(f" + {GREEN}{b:.2f}{RESET}")
			print(f"{YELLOW}The correlation coefficient is:{RESET}")
			avg_x = sum(mileage) / len(mileage)
			avg_y = sum(price) / len(price)
			r = b**2
			r = r * sum((xi - avg_x)**2 for xi in mileage)
			r = r / sum((yi - avg_y)**2 for yi in price)
			r = r**0.5
			print(f"  r = {GREEN}{r:.2f}{RESET}")
			plot_regression(mileage, price, a, b)

			print(f"{YELLOW}Predict the price of a car with a given mileage:{RESET}")
			while True:
				try:
					mileage_input = float(input("Enter the mileage: "))
					if mileage_input < 0:
						print(f"{RED}Error: Mileage must be a positive number.{RESET}")
					else:
						break
				except ValueError:
					print(f"{RED}Error: Please enter a valid number.{RESET}")
			price_pred = a + b * mileage_input
			print(f"The predicted price for a car with {mileage_input} km is {GREEN}{price_pred:.2f}{RESET}")
		else:
			print(f"{RED}Error: Could not calculate the linear regression coefficients.{RESET}")


if __name__ == "__main__":
	main()