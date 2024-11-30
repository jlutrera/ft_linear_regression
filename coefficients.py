# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    coefficients.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jutrera- <jutrera-@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/30 23:12:23 by jutrera-          #+#    #+#              #
#    Updated: 2024/11/30 23:12:23 by jutrera-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from macros import *
from utils import wait_for_keypress

def print_coefficients(theta0, theta1):
	print(f"  Linear regression coefficients:")
	print(f"    {THETA}{SUB0} = {GREEN}{theta0:.2f}{RESET}")
	print(f"    {THETA}{SUB1} = {GREEN}{theta1:.2f}{RESET}")

	print(f"\n  Equation of the regression line:")
	if theta1 < 0:
		print(f"    y = {GREEN}{theta0:.2f}{RESET} - {GREEN}{-theta1:.2f}{RESET}{DOT}x")
	else:
		print(f"    y = {GREEN}{theta0:.2f}{RESET} + {GREEN}{theta1:.2f}{RESET}{DOT}x")

def coef(mileage, price, theta0, theta1):
	if mileage and price and theta0 is not None and theta1 is not None:
		print_coefficients(theta0, theta1)
	else:
		print(f"  {RED}Error: {RESET}Could not calculate the linear regression coefficients.")

	wait_for_keypress()
