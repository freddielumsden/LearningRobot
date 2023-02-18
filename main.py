import random


class Robot():
	def getMessage(self):
		self.user_message = input("")
		return self.user_message

	def processMessage(self):
		with open("database.txt", "r") as f:
			file = f.readlines()
		file = [i.split('/') for i in file]
		for i in file:
			if self.user_message.lower() == i[0].lower():
				self.robot_message = random.choice(i[1:]).capitalize()
				return
		return "unkown"

	def sendMessage(self):
		print(self.robot_message)

	def addMessage(self):
		print("This robot doesn't understand that yet...\nBut you could help it do so by providing the message " + self.user_message + " with some responses!\nAlternatively just press enter.")
		while True:
			responses = input("Type all the responses seperated by /'s\n For instance, if the message was hello, you could type yo/hi/hey there/nice to meet you!").split()
			if responses == "":
				return
			print("Here is a list of the responses you wrote:\n" + responses)
		
		

print("Welcome to the greetings bot!!!\nPress enter to quit.")
robot = Robot()
user_message = robot.getMessage()
while user_message != "":
	message_understood = robot.processMessage()
	if message_understood == "unkown":
		robot.addMessage()
	else:
		robot.sendMessage()
	user_message = robot.getMessage()
