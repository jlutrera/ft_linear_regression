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

from utils import *
from prediction import predict_price
from training import train_program
from plotting import plot_data
from coefficients import coef
from errors import err
from unicodes import *

def init(k):
	if k == 1:
		print(f"  Program reset {GREEN}successfully!{RESET}")
		wait_for_keypress()

	return 0, 0, [], []

def print_menu(theta0, theta1):
	clear_terminal()
	print(f"{CYAN}*** Linear Regression Program ***{RESET}\n")
	if theta0 == 0 and theta1 == 0:
		print(f"{YELLOW}Choose an option{RESET}  ( Current model: {RED}UNTRAINED{RESET} )\n")
	else:
		print(f"{YELLOW}Choose an option{RESET}  ( Current model: {GREEN}TRAINED{RESET} )\n")
	print(f"  {YELLOW}1{RESET}. Predict the price of a car with a given mileage")
	print(f"  {YELLOW}2{RESET}. Train the model with a CSV file.")
	print(f"  {YELLOW}3{RESET}. Plot the data and the regression line")
	print(f"  {YELLOW}4{RESET}. Print the equation and coefficients")
	print(f"  {YELLOW}5{RESET}. Print the prediction errors")
	print(f"  {YELLOW}6{RESET}. Reset the program")
	print(f"  {YELLOW}7{RESET}. Exit\n")
	
	option = input(f"Enter the number of the option: {YELLOW}")
	print(f"{RESET}\n", end = '')
	
	return option

def main():
	theta0, theta1, mileage, price =init(0)
	while True:
		option = print_menu(theta0, theta1)
		match option:
			case '1':
				predict_price(theta0, theta1)
			case '2':
				mileage, price, theta0, theta1 = train_program()
			case '3':
				plot_data(mileage, price, theta0, theta1)
			case '4':
				coef(mileage, price, theta0, theta1)
			case '5':
				err(mileage, price, theta0, theta1)
			case '6':
				theta0, theta1, mileage, price = init(1)
			case '7':
				break
			case _:
				print(f"  {RED}Error: {RESET}Invalid option. Please enter a number between 1 and 7.")
				wait_for_keypress()
	
	print(f"{CYAN}*** Goodbye! ***{RESET}\n")

if __name__ == "__main__":
	main()