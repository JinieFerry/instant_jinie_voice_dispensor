# Git , Git Bash , Vscode (Visual Studio for Code) 다운 & 연동
https://www.youtube.com/watch?v=lelVripbt2M

#README.md 작성
https://www.youtube.com/watch?v=MFJIOqxK6k8

#KU'S ORIGIN_TextInput

'''python
# Import the tkinter module
from tkinter import * 
from elevenlabs import play
from elevenlabs.client import ElevenLabs

# Creating the GUI window.
window = Tk()
window.title("Welcome to geeksforgeeks")
window.geometry("800x100")

client = ElevenLabs(
	api_key="e75347c1353dd3083be81b47c4705fd6", # Defaults to ELEVEN_API_KEY
)

# Creating the function to set the text 
# with the help of button
def set_text_by_button():

	# Delete is going to erase anything
	# in the range of 0 and end of file,
	# The respective range given here
	#sample_text.delete(0,"end")
	
	# Insert method inserts the text at
	# specified position, Here it is the
	# beginning
	#sample_text.insert(0, sample_text.get())
	#print(sample_text.get())	

	audio = client.generate(
		text=sample_text.get(),
  		#text="Hello! 你好! Hola! नमस्ते! Bonjour! こんにちは! مرحبا! 안녕하세요! Ciao! Cześć! Привіт! வணக்கம்!",
  		voice="Rachel", # try Nicole
  		model="eleven_multilingual_v2"
	)
	play(audio)

# Creating our text widget.
sample_text = Entry(window)
sample_text.pack()

# Setting up the button, set_text_by_button() 
# is passed as a command
set_up_button = Button(window, height=1, width=10, text="Set", 
					command=set_text_by_button)

set_up_button.pack()

window.mainloop()
'''
