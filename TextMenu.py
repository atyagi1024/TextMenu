#!/usr/bin/python3
#
# File: TextMenu.py
# Author: Atul.Tyagi<atul.tyagi@dimensiondata.com>
#
#
import os
import sys

class MainMenu:
	def __init__(self,menu):
		self.menu = menu
		self.MainMenu_Options = self.menu.sections()

	def ShowMenu(self):		
		os.system('clear')
		print()
		print('What would you like to do in Dimension Data Cloud: ')
		print('======================================================')
		print()
		for i, option in enumerate(self.MainMenu_Options):
			print('{}'.format(i),'{}'.format(option))
		print()
		return

	def ReturnMainMenuOption(self):
		flag = True
		while (flag == True):
			option_selected = input("Please enter the option: ")
			print()
			if int(option_selected) < len(self.MainMenu_Options):
				ret_option = self.MainMenu_Options[int(option_selected)]
				flag = False
		return ret_option
		
class SubMenu:
	def __init__(self,menu):
		self.menu = menu
		
	def ShowSubMenu(self,mainmenu_option):
		if len(self.menu[mainmenu_option]) == 0:
			sys.exit
		else:
			os.system('clear')
			print()
			print('What would you further like to do : ')
			print('===================================')
			print()
			for option,item in self.menu[mainmenu_option].items():
				print('{} {}'.format(option,item))
			print()
		return

	def ReturnSubMenuOption(self,mainmenu_option):
		if len(self.menu[mainmenu_option]) == 0:
			ret_option = None
		else:
			flag = True
			while (flag == True):
				option_selected = input("Please enter the option: ")
				print()
				if option_selected in self.menu[mainmenu_option].keys():
					ret_option = self.menu[mainmenu_option][option_selected]
					flag = False
		return ret_option

if __name__ == '__main__':
	pass
