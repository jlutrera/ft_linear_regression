# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    errors.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jutrera- <jutrera-@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/30 23:12:36 by jutrera-          #+#    #+#              #
#    Updated: 2024/11/30 23:12:36 by jutrera-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from. import *
from .utils import wait_for_keypress

def calc_error(x, y, theta0, theta1):
	n = len(x)
	y_pred = [theta0 + theta1 * xi for xi in x]
	errors = [yi - y_hat for yi, y_hat in zip(y, y_pred)]

	mae = sum(abs(error) for error in errors) / n
	mse = sum(error ** 2 for error in errors) / n
	rmse = mse ** 0.5

	y_mean = sum(y) / n
	ss_total = sum((yi - y_mean) ** 2 for yi in y)
	ss_residual = sum((yi - y_hat) ** 2 for yi, y_hat in zip(y, y_pred))
	r2 = 1 - (ss_residual / ss_total)

	return {"MAE": mae, "MSE": mse,	"RMSE": rmse, "R2": r2 * 100}

def err(mileage, price, theta0, theta1):
	if mileage and price and theta0 is not None and theta1 is not None:
		errors = calc_error(mileage, price, theta0, theta1)
		print(f"  MAE  = {GREEN}{errors['MAE']:.2f}{RESET}")
		print(f"  MSE  = {GREEN}{errors['MSE']:.2f}{RESET}")
		print(f"  RMSE = {GREEN}{errors['RMSE']:.2f}{RESET}")
		print(f"  R{SQUARE}   = {GREEN}{errors['R2']:.2f}%{RESET}")
	else:
		print(f"  {RED}Error: {RESET}Could not calculate the prediction errors.")

	wait_for_keypress()
