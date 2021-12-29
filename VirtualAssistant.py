import speech_recognition
from random import randint
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
while True:
	with speech_recognition.Microphone() as mic:
		robot_ear.adjust_for_ambient_noise(mic)
		print("Robot: I'm listening.")
		audio = robot_ear.listen(mic,timeout=5)
	print("Robot: ....")
	try:
		you = robot_ear.recognize_google(audio )
	except:
		you = ""
	print("You: " + you)

	if you == "":
		robot_brain = "I can't hear you, try again."
	elif "hello" in you:
		robot_brain = "Hello Minh Vu."
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y") 
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "bye" in you:
		print("See you again")
		robot_mouth.say("See you again.")
		robot_mouth.runAndWait()
		break
	elif "game" in you:
		while True:	
			print("Robot: Do you want to play Game 1 or Game 2?")
			robot_mouth.say("Do you want to play Game 1 or Game 2?")
			robot_mouth.runAndWait()
			game=input()
			print("You:" + game)
			if "Out" in game:
				print("Robot: See you again.")
				robot_mouth.say("See you again.")
				robot_mouth.runAndWait()
				break
			elif "1" in game:
				while True:
					print("You choose: ")
					robot_mouth.say("You choose:")
					robot_mouth.runAndWait()
					player = input()
					computer = randint(0,2)
					print("---")

					if computer == 0:
						computer = "Bua"
					if computer == 1:
						computer = "Keo"
					if computer ==2:
						computer = "Bao"

					print("You: " + player)
					print("Robot: " + computer)
					print("---")
					if player == computer:
						print("Draw!")
						robot_mouth.say("Draw!")
						robot_mouth.runAndWait()
					elif player == "Keo":
						if computer == "Bao":
							print("Win!")
							robot_mouth.say("Win!")
							robot_mouth.runAndWait()
						else:
							print("Lose!")
							robot_mouth.say("Lose!")
							robot_mouth.runAndWait() 
					elif player == "Bao":
						if computer == "Keo":
							print("Lose!")
							robot_mouth.say("Lose!")
							robot_mouth.runAndWait()
						else:
							print("Win!")
							robot_mouth.say("Win!")
							robot_mouth.runAndWait()
					elif player == "Bua":
						if computer == "Keo":
							print("Win!")
							robot_mouth.say("Win!")
							robot_mouth.runAndWait()
						else:
							print("Lose!")
							robot_mouth.say("Lose!")
							robot_mouth.runAndWait()

					else: 
						print("Wrong Typed. ")
						robot_mouth.say("Wrong Typed.")
						robot_mouth.runAndWait()

					print("-----")
					print("Try again or Out?")
					robot_mouth.say("Try again or Out?")
					robot_mouth.runAndWait()	
					choose = input()
					if choose == "Out":
						robot_mouth.say("See you again!")
						robot_mouth.runAndWait()
						break
			elif "2" in game:
				while True:
					print("(Trai/Phai) -- 1st Steps: ")
					Step1 = input()

					Check1 = randint (0,1)

					if Check1 == 0:
						Check1 = "Trai"
					else:
						Check1 = "Phai"

					if Check1 == Step1:
						print("----")
						print("You: " + Step1)
						print("Robot: " + Check1)
						print("----")
						print("Pass!")
						robot_mouth.say("Pass!")
						robot_mouth.runAndWait()

						print("------------")
						print("(Trai/Phai) -- 2st Steps: ")

						Step2 = input()

						Check2 = randint (0,1)

						if Check2 == 0:
							Check2 = "Trai"
						else:
							Check2 = "Phai"

						if Check2 == Step2:
							print("----")
							print("Your steps: " + Step2)
							print("Correct steps: " + Check2)
							print("----")
							print("Pass!")
							robot_mouth.say("Pass!")
							robot_mouth.runAndWait()
							print("-------------")
							print("You are a Champion!!!")
							robot_mouth.say("You are a Champion!!!")
							robot_mouth.runAndWait()
						elif Step2 == "Trai" or Step2 == "Phai":
							print("----")
							print("Your steps: " + Step2)
							print("Correct steps: " + Check2)
							print("----")
							print("Fall")
							robot_mouth.say("Fall!")
							robot_mouth.runAndWait()
							print("-------------")
							print("You lose!!!")
							robot_mouth.say("You lose!")
							robot_mouth.runAndWait()
						else:
							print("Wrong Typed")
							robot_mouth.say("Wrong Typed!")
							robot_mouth.runAndWait()

					elif Step1 == "Trai" or Step1 == "Phai":
						print("----")
						print("Your steps: " + Step1)
						print("Correct steps: " + Check1)
						print("----")
						print("Fall")
						robot_mouth.say("Fall!")
						robot_mouth.runAndWait()
						print("-------------")
						print("You lose!!!")
						robot_mouth.say("You lose!")
						robot_mouth.runAndWait()
					else:
						print("Wrong Typed!")
						robot_mouth.say("Wrong Typed!")
						robot_mouth.runAndWait()

					print("-----")
					print("Try again or Out?")
					robot_mouth.say("Try again or Out?")
					robot_mouth.runAndWait()	
					choose = input()
					if choose == "Out":
						robot_mouth.say("See you again!")
						robot_mouth.runAndWait()
						break
				
			else:
				print("Wrong Typed. Try again or Out")
				robot_mouth.say("Wrong Typed. Try again or Out.")
				robot_mouth.runAndWait()
				robot_brain = input()
		
	print("Robot: " + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()
	voices = robot_mouth.getProperty('voices')
	robot_mouth.setProperty('voice', voices[1].id)




