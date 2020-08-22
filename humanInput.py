import pyttsx3
import os

pyttsx3.speak("Hi I'm your virtual assistant. Tell me what you would like me to launch ")

while True:
	print("")
	print("Tell me what you would like me to launch : " , end='')

	p = input()
	
	if   ("help"in p) and (("how"in p) or ("what" in p)) :
		print("I can open any software, apllication from your computer")
		pyttsx3.speak("I can open any software, apllication from your computer.")

	elif   (("run"in p) or ("execute" in p) or ("launch" in p)) and (("chrome"in p) or ("browser" in p)) :
		pyttsx3.speak("Opening Chrome Browser")
		os.system("chrome")

	elif   (("run"in p) or ("execute" in p) or ("launch" in p)) and (("notepad" in p) or ("editor"in p)) :
		pyttsx3.speak("Opening Notepad")	
		os.system("notepad")
	
	elif   (("run"in p) or ("execute" in p) or ("launch" in p)) and (("VLC" in p) or ("Media player"in p) or ("vlc"in p)) :
		pyttsx3.speak("Opening VLC  player, Enjoy")	
		os.system("vlc")

	elif   (("run"in p) or ("execute" in p)) and ("paint" in p) :
		pyttsx3.speak("Opening Paint")	
		os.system("mspaint")

	elif   (("run"in p) or ("execute" in p) or ("launch" in p)) and (("snipping" in p) or ("snipping tool"in p) or ("crop tool"in p)) :
		pyttsx3.speak("Opening Snipping Tool")	
		os.system("SnippingTool")

	elif   (("run"in p) or ("execute" in p) or ("launch" in p)) and (("calculator" in p)) :
		pyttsx3.speak("Opening Calculator")	
		os.system("calc")

	elif   (("run"in p) or ("execute" in p) or ("launch" in p)) and (("media player" in p) or ("media"in p)) :
		pyttsx3.speak("Opening Window Media Player")	
		os.system("wmplayer")

	elif   (("run"in p) or ("execute" in p) or ("launch" in p)) and ("wordpad" in p) :
		pyttsx3.speak("Opening Wordpad")	
		os.system("wordpad")

	elif   (("exit"in p) or ("stop" in p)):
		pyttsx3.speak("Closing Virtual assistant, thanks for using me")	
		break
	else:
		print("Sorry!!!  not supported")
		pyttsx3.speak("Sorry not supported")