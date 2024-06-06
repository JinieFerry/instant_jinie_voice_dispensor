# Import the tkinter module
from tkinter import * 
from tkinter import messagebox  # 오류 메시지 박스를 위해 추가
from elevenlabs import play
from elevenlabs.client import ElevenLabs

# Creating the GUI window.
window = Tk()
window.title("Instant JINIE Voice")
window.geometry("1600x800")

client = ElevenLabs(
    api_key="e75347c1353dd3083be81b47c4705fd6",
)

# Creating the function to set the text with the help of button
def set_text_by_button():
    # 입력된 텍스트 가져오기
    input_text = sample_text.get()

    # 입력 검증
    if not input_text.strip():
        messagebox.showwarning("경고", "텍스트를 입력해주세요.")
        return

    try:
        audio = client.generate(
            text=input_text,
            voice="TanIbI9Mp3LZpER1QOuv",  # try Nicole
            model="eleven_multilingual_v2"
        )
        play(audio)
    except Exception as e:
        messagebox.showerror("오류", f"음성 변환 중 오류가 발생했습니다: {e}")

# Creating our text widget.
sample_text = Entry(window)
sample_text.pack()

# Setting up the button, set_text_by_button() is passed as a command
set_up_button = Button(window, height=10, width=70, text="Give Me Jinie Voice", 
                    command=set_text_by_button)

set_up_button.pack()

window.mainloop()

#for check my github

#final pt git hub test 
#text push lfs update