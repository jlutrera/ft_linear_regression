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

from . import *
import csv

def read_csv_data():
	mileage = []
	price = []
	csv_file = input("Enter the name of the CSV (with the relative path): ")

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

def calc_values(x, y):
	# --- 1. Normalización Min-Max ---
	x_min, x_max = min(x), max(x)
	y_min, y_max = min(y), max(y)

	norm_x = [(xi - x_min) / (x_max - x_min + EPS) for xi in x]
	norm_y = [(yi - y_min) / (y_max - y_min + EPS) for yi in y]

	# --- 2. Inicialización ---
	previous_loss = float('inf')
	theta0, theta1 = 0, 0
	n = len(x)

	alphas = []
	# --- 3. Gradient Descent ---
	for t in range(ITER):
		# Learning rate decay
		alpha = ALPHA0 / (1 + K * t) 
		# Also could be done with ALPHA0 * (exp(-K * t))
		alphas.append(alpha)

		# Hipótesis sobre datos normalizados
		errors = [theta0 + theta1 * xi - yi for xi, yi in zip(norm_x, norm_y)]

		# Gradientes
		grad0 = sum(errors) / n
		grad1 = sum(error * xi for error, xi in zip(errors, norm_x)) / n

		# Actualización simultánea
		theta0 -= alpha * grad0
		theta1 -= alpha * grad1

		# Cálculo del coste
		loss = sum(e * e for e in errors) / (2 * n)
		
		# Early stopping
		if previous_loss - loss < EPSILON:
			break

		previous_loss = loss

	# --- 4. Desnormalización ---
	b = theta1 * (y_max - y_min) / (x_max - x_min)
	a = y_min + theta0 * (y_max - y_min) - b * x_min

	return a, b, alphas, t, 1

def training():
	mileage, price = read_csv_data()
	if mileage and price:
		theta0, theta1, alphas, t, e = calc_values(mileage, price)
	else:
		theta0, theta1, alphas, t, e = 0, 0, [], 0, 0
	return mileage, price, theta0, theta1, alphas, t, e
