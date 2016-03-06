import os
class Menu:
	def __init__(self, actions,options,functions):
		self.actions = actions
		self.options = options
		self.functions = functions

	def printMenu(self):
		os.system("clear")
		for i in xrange(len(self.actions)):
			print i+1,") ",self.actions[i],"\n"
		opt = int(raw_input(": "))
		os.system("clear")
		if(self.actions[opt-1] == "Salir"):
			self.functions[self.actions[opt-1]]()
			return 0
		else:
			for i in xrange(len(self.options)):
				print i+1,") ",self.options[i],"\n"
			opt2 = int(raw_input(": "))
			os.system("clear")
			self.functions[self.actions[opt-1]][self.options[opt2-1]]()
		self.printMenu();


		