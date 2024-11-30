from unicodes import *
from utils import wait_for_keypress
import csv

def read_csv_data():
	mileage = []
	price = []
	csv_file = "data.csv"
	try:
		with open(csv_file, 'r') as file:
			reader = csv.reader(file)
			next(reader)
			for row in reader:
				mileage.append(float(row[0]))
				price.append(float(row[1]))
	except Exception as e:
		print(f"  {RED}Error: {RESET}{e.args[1]}")
		return None, None

	return mileage, price

def read_parameters():
	while True:
		try:
			alpha = float(input(f"  Enter the learning rate (alpha): {GREEN}"))
			print(f"{RESET}", end = '')
			if alpha <= 0:
				print(f"  {RED}Error: {RESET}Learning rate must be a positive number.")
			else:
				break
		except ValueError:
			print(f"  {RED}Error: {RESET}Please enter a valid number.")

	while True:
		try:
			iterations = int(input(f"  Enter the number of iterations: {GREEN}"))
			print(f"{RESET}", end = '')
			if iterations <= 0:
				print(f"  {RED}Error: {RESET}Number of iterations must be a positive integer.")
			else:
				break
		except ValueError:
			print(f"  {RED}Error: {RESET}Please enter a valid number.")

	return alpha, iterations

def calc_linear_regression(x, y, alpha, iterations):
	"""Performs gradient descent to learn theta0 and theta1."""
	theta0, theta1 = 0, 0
	n = len(x)

	# Normalize the data
	x_min, x_max = min(x), max(x)
	norm_x = [(xi - x_min) / (x_max - x_min) for xi in x]
	y_min, y_max = min(y), max(y)
	norm_y = [(yi - y_min) / (y_max - y_min) for yi in y]

	# Gradient descent
	for _ in range(iterations):

		errors = [theta0 + theta1 * xi - yi for xi, yi in zip(norm_x, norm_y)]
    
		temp_theta0 = sum(errors) / n
		temp_theta1 = sum(error * xi for error, xi in zip(errors, norm_x)) / n
        
		theta0 -= alpha * temp_theta0
		theta1 -= alpha * temp_theta1

	# Denormalize the data
	theta1 = theta1 * (y_max - y_min) / (x_max - x_min)
	theta0 = y_min + (theta0 - theta1 * x_min / (x_max - x_min)) * (y_max - y_min)
	
	return theta0, theta1

def train_program():
	mileage, price = read_csv_data()
	alpha, iterations = read_parameters()
	if mileage and price:
		theta0, theta1 = calc_linear_regression(mileage, price, alpha, iterations)
		print(f"  Model trained {GREEN}successfully!{RESET}")
	wait_for_keypress()

	return mileage, price, theta0, theta1
