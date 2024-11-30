import matplotlib.pyplot as plt
from unicodes import *
from utils import wait_for_keypress

def plot_regression(mileage, price, theta0, theta1):
	# Original data points
	plt.scatter(mileage, price, color='blue', label='Original Data')
	# Generate points for the regression line
	x_min = min(mileage)
	x_max = max(mileage)
	x_line = [x_min, x_max]
	y_line = [theta0 + theta1 * x_min, theta0 + theta1 * x_max]
	# Plot the line
	if theta1 < 0:
		plt.plot(x_line, y_line, color='red', label=f'Regression Line: y = {theta0:.2f} - {-theta1:.2f}x')
	else:
		plt.plot(x_line, y_line, color='red', label=f'Regression Line: y = {theta0:.2f} + {theta1:.2f}x')
	# Configure the plot
	plt.xlabel('Mileage')
	plt.ylabel('Price')
	plt.title('Linear Regression')
	plt.legend()
	plt.grid(True)
	plt.show()

def plot_data(mileage, price, theta0, theta1):
	if mileage and price and theta0 is not None and theta1 is not None:
		print(f"  {B_ON_W}Close window to continue...{RESET}")
		plot_regression(mileage, price, theta0, theta1)
	else:
		print(f"  {RED}Error: {RESET}Could not plot the data and the regression line.")
		wait_for_keypress()
