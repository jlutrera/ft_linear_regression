from unicodes import *
from utils import wait_for_keypress

def calc_price(theta0, theta1, mileage):
	price_pred = theta0 + theta1 * mileage
	if (price_pred < 0):
		price_pred = 0

	return price_pred

def predict_price(theta0, theta1):
	while True:
		try:
			mileage_input = float(input(f"  Enter the mileage: {GREEN}"))
			print(f"{RESET}", end = '')
			if mileage_input < 0:
				print(f"  {RED}Error: {RESET}Mileage must be a positive number.")
			else:
				break
		except ValueError:
			print(f"  {RED}Error: {RESET}Please enter a valid number.")

	price_pred = calc_price(theta0, theta1, mileage_input)
	print(f"  Predicted price: {GREEN}{price_pred:.2f}{RESET}")

	wait_for_keypress()

