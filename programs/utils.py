# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jutrera- <jutrera-@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/30 23:19:10 by jutrera-          #+#    #+#              #
#    Updated: 2024/11/30 23:19:10 by jutrera-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, sys
from . import *

def wait_for_keypress():
	message = f"\n  {B_ON_W}Press a key to continue...{RESET}"
	if os.name == 'nt':  # Windows
		import msvcrt
		print(message, end = '', flush = True)
		msvcrt.getch()
	else:  # Linux y macOS
		print(message, end = '', flush = True)
		import termios
		import tty
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def clear_terminal():
	# Para Linux y macOS
	if os.name == 'posix':
		os.system('clear')
	# Para Windows
	elif os.name == 'nt':
		os.system('cls')