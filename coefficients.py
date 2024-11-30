from unicodes import *
from utils import wait_for_keypress


def calc_correlation(x, y):
	n = len(x)
	avg_x = sum(x) / n
	avg_y = sum(y) / n
	r = sum((xi - avg_x) * (yi - avg_y) for xi, yi in zip(x, y))
	r = r / (sum((xi - avg_x)**2 for xi in x) * sum((yi - avg_y)**2 for yi in y))**0.5

	return r

def print_coefficients(theta0, theta1, mileage, price):
	print(f"  Linear regression coefficients:")
	print(f"    Intercept: {THETA}0 = {GREEN}{theta0:.2f}{RESET}")
	print(f"    Slope    : {THETA}1 = {GREEN}{theta1:.2f}{RESET}")

	print(f"\n  Equation of the regression line:")
	if theta1 < 0:
		print(f"    y = {GREEN}{theta0:.2f}{RESET} - {GREEN}{-theta1:.2f}{RESET}*x")
	else:
		print(f"    y = {GREEN}{theta0:.2f}{RESET} + {GREEN}{theta1:.2f}{RESET}*x")

	r = calc_correlation(mileage, price)

	print(f"\n  Correlation coefficient:")
	print(f"    r = {GREEN}{r:.2f}{RESET}")

def coef(mileage, price, theta0, theta1):
	if mileage and price and theta0 is not None and theta1 is not None:
		print_coefficients(theta0, theta1, mileage, price)
	else:
		print(f"  {RED}Error: {RESET}Could not calculate the linear regression coefficients.")

	wait_for_keypress()
