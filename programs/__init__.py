#__init__.py

RESET  = "\033[0m"
B_ON_W = "\033[30;47m"

RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
MAGENTA= "\033[35m"
CYAN   = "\033[36m"

THETA  = "\u03B8"
ALPHA  = '\u03B1'
SQUARE = '\u00B2'
SUB0   = '\u2080'
SUB1   = '\u2081'
DOT	   = '\u00B7'

K      = 0.0001 # Decay rate
ALPHA_0= 0.1   # Initial learning rate
EPSILON= 1e-8 # Stop when the loss is not decreasing significantly
ITER   = 1000000 # Maximum number of iterations

__all__ = ["RESET", "B_ON_W", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "THETA", "ALPHA", "SQUARE", "SUB0", "SUB1", "DOT", "K", "ALPHA_0", "EPSILON", "ITER"]