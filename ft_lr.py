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

import csv, os, sys
import matplotlib.pyplot as plt

RED    = "\033[31m"
GREEN  = "\033[32m"
BLUE   = "\033[34m"
CYAN   = "\033[36m"
YELLOW = "\033[33m"
B_ON_W = "\033[30;47m"
RESET  = "\033[0m"

def clear_terminal():
	# Para Linux y macOS
	if os.name == 'posix':
		os.system('clear')
	# Para Windows
	elif os.name == 'nt':
		os.system('cls')

def wait_for_keypress():
	message = f"{B_ON_W}\nPress a key to continue...{RESET}"
	if os.name == 'nt':  # Windows
		import msvcrt
		print(message, end = '', flush = True)
		msvcrt.getch()
	else:  # Linux y macOS
		print(message, end = '', flush = True)
		import termios
		import tty
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def read_csv_data():
	mileage = []
	price = []
	csv_file = input(f"  Enter the name of the CSV file: {GREEN}")
	print(f"{RESET}", end = '')
	try:
		with open(csv_file + ".csv", 'r') as file:
			reader = csv.reader(file)
			next(reader)  # Skip the header row
			for row in reader:
				if len(row) >= 2:
					mileage.append(float(row[0]))
					price.append(float(row[1]))
	except FileNotFoundError:
		print(f"{RED}Error: {RESET}Could not find the file {csv_file}")
		return None, None
	return mileage, price

def calculate_linear_regression(x, y):
	"""Calculates the linear regression coefficients (a and b) for y = a + b * x."""
	n = len(x)
	if n == 0:
		print(f"{RED}Error: {RESET}Empty lists.")
		return None, None
	if n != len(y):
		print(f"{RED}Error: {RESET}Lists with different lengths.")
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

def calculate_correlation(x, y):
	n = len(x)
	# Calculate averages
	avg_x = sum(x) / n
	avg_y = sum(y) / n

	# Calculate correlation coefficient
	r = sum((xi - avg_x) * (yi - avg_y) for xi, yi in zip(x, y))
	r = r / (sum((xi - avg_x)**2 for xi in x) * sum((yi - avg_y)**2 for yi in y))**0.5
	return r

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

def predict_price(a, b):
	print(f"{YELLOW}Predict the price of a car with a given mileage{RESET}")
	while True:
		try:
			mileage_input = float(input(f"  Enter the mileage: {GREEN}"))
			print(f"{RESET}", end = '')
			if mileage_input < 0:
				print(f"{RED}Error: {RESET}Mileage must be a positive number.")
			else:
				break
		except ValueError:
			print(f"{RED}Error: {RESET}Please enter a valid number.")
	price_pred = a + b * mileage_input
	if (price_pred < 0):
				price_pred = 0
	print(f"  Predicted price: {GREEN}{price_pred:.2f}{RESET}")

def init():
	a, b = 0, 0
	mileage, price = [], []
	return a, b, mileage, price

def print_menu(a, b):
	clear_terminal()
	print(f"{CYAN}*** Linear Regression Program ***{RESET}\n")
	if a == 0 and b == 0:
		print(f"{YELLOW}Choose an option{RESET}  ( Current model: {RED}NO TRAINED !{RESET})\n")
	else:
		print(f"{YELLOW}Choose an option{RESET}  ( Current model: {GREEN}TRAINED !{RESET})\n")
	print(f"  {YELLOW}1{RESET}. Predict the price of a car with a given mileage")
	print(f"  {YELLOW}2{RESET}. Train the model with a CSV file.")
	print(f"  {YELLOW}3{RESET}. Plot the data and the regression line")
	print(f"  {YELLOW}4{RESET}. Print the linear regression and correlation coefficients")
	print(f"  {YELLOW}5{RESET}. Reset the program")
	print(f"  {YELLOW}6{RESET}. Exit\n")
	option = input(f"  Enter the number of the option: {YELLOW}")
	print(f"{RESET}\n", end = '')
	return option

def print_coefficients(a, b, mileage, price):
	print(f"{YELLOW}Linear regression coefficients:{RESET}")
	print(f"  a = {GREEN}{a:.2f}{RESET}  (Intercept)")
	print(f"  b = {GREEN}{b:.2f}{RESET} (Slope)")

	r = calculate_correlation(mileage, price)
	print(f"{YELLOW}Correlation coefficient:{RESET}")
	print(f"  r = {GREEN}{r:.2f}{RESET}")

	print(f"{YELLOW}Equation of the regression line:{RESET}")
	if b < 0:
		print(f"  y = {GREEN}{a:.2f}{RESET} - {GREEN}{-b:.2f}{RESET}x")
	else:
		print(f"  y = {GREEN}{a:.2f}{RESET} + {GREEN}{b:.2f}{RESET}x")

def main():
	a, b = 0, 0
	mileage, price = [], []
	while True:
		option = print_menu(a, b)
		
		match option:
			case '1':
				predict_price(a, b)
				wait_for_keypress()
			case '2':
				mileage, price = read_csv_data()
				if mileage and price:
					a, b = calculate_linear_regression(mileage, price)
					if a is not None and b is not None:
						print(f"  Model trained {GREEN}successfully!{RESET}")
				wait_for_keypress()
			case '3':
				if mileage and price and a is not None and b is not None:
					print(f"{B_ON_W}Close window to continue...{RESET}")
					plot_regression(mileage, price, a, b)
				else:
					print(f"{RED}Error: {RESET}Could not plot the data and the regression line.")
					wait_for_keypress()
			case '4':
				if mileage and price and a is not None and b is not None:
					print_coefficients(a, b, mileage, price)
				else:
					print(f"{RED}Error: {RESET}Could not calculate the linear regression coefficients.")
				wait_for_keypress()
			case '5':
				a, b, mileage, price = init()
				print(f"  Program reset {GREEN}successfully!{RESET}")
				wait_for_keypress()
			case '6':
				print(f"{CYAN}Goodbye!{RESET}")
				break
			case _:
				print(f"{RED}Error: {RESET}Invalid option. Please enter a number between 1 and 6.")
				wait_for_keypress()
		
if __name__ == "__main__":
	main()