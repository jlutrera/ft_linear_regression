# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    training.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jutrera- <jutrera-@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/30 23:14:08 by jutrera-          #+#    #+#              #
#    Updated: 2024/11/30 23:14:08 by jutrera-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from macros import *
from plotting import plot_alpha
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

def calc_linear_regression(x, y):
	# Normalize the data
	x_min, x_max = min(x), max(x)
	norm_x = [(xi - x_min) / (x_max - x_min) for xi in x]
	y_min, y_max = min(y), max(y)
	norm_y = [(yi - y_min) / (y_max - y_min) for yi in y]

	# Initialize the parameters
	previous_loss = float('inf')  # Initialize the loss with a large value
	theta0, theta1 = 0, 0
	n = len(x)

	# Gradient descent
	alphas = []
	for t in range(ITER):
		alpha = ALPHA_0 / (1 + K * t) # Learning rate decay
		#Also could be done with ALPHA_0 * (exp(-K * t))

		alphas.append(alpha)
		errors = [theta0 + theta1 * xi - yi for xi, yi in zip(norm_x, norm_y)]
		temp_theta0 = sum(errors) / n
		temp_theta1 = sum(error * xi for error, xi in zip(errors, norm_x)) / n
		theta0 -= alpha * temp_theta0
		theta1 -= alpha * temp_theta1
		# Calculate the loss
		loss = sum(error ** 2 for error in errors) / (2 * n)
		# Early stopping
		if previous_loss - loss < EPSILON:
			break
		# Update the previous loss
		previous_loss = loss
	# Denormalize the data
	theta1 = theta1 * (y_max - y_min) / (x_max - x_min)
	theta0 = y_min + (theta0 - theta1 * x_min / (x_max - x_min)) * (y_max - y_min)
	plot_alpha(alphas, t)
	return theta0, theta1

def train_program():
	mileage, price = read_csv_data()
	if mileage and price:
		theta0, theta1 = calc_linear_regression(mileage, price)
	else:
		print(f"  {RED}Error: {RESET}Could not train the model.")
		wait_for_keypress()
		theta0, theta1 = None, None
	return mileage, price, theta0, theta1
