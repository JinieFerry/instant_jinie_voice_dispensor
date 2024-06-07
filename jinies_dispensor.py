# Import the tkinter module
from tkinter import *
from elevenlabs import play
from elevenlabs.client import ElevenLabs
from pathlib import Path

# Initialize ElevenLabs client
client = ElevenLabs(
    api_key="e75347c1353dd3083be81b47c4705fd6",  # Defaults to ELEVEN_API_KEY
)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\MSI\Desktop\instant_jinie_voice_finalPt\figma_to_tkdesigner\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Function to generate and play audio using ElevenLabs
def generate_and_play_audio():
    text = entry_1.get("1.0", END).strip()
    if text:
        audio = client.generate(
            text=text,
            voice="TanIbI9Mp3LZpER1QOuv",  # Use the appropriate voice ID
            model="eleven_multilingual_v2"
        )
        play(audio)
    else:
        print("No text entered")

# Creating the GUI window.
window = Tk()
window.title("Istant JINIE Voice")
window.geometry("1280x720")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(640.0, 360.0, image=image_image_1)

canvas.create_text(
    606.0,
    154.0,
    anchor="nw",
    text="The Dispensor",
    fill="#000000",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_rectangle(
    204.0,
    230.0,
    1117.0,
    236.0,
    fill="#FFFFFF",
    outline=""
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=generate_and_play_audio,
    relief="flat"
)
button_1.place(
    x=261.0,
    y=276.0,
    width=848.0,
    height=84.0
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(684.0, 431.0, image=entry_image_1)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=261.0,
    y=388.0,
    width=846.0,
    height=84.0
)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(684.0, 543.0, image=entry_image_2)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=261.0,
    y=500.0,
    width=846.0,
    height=84.0
)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(684.0, 656.0, image=entry_image_3)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=261.0,
    y=613.0,
    width=846.0,
    height=84.0
)

window.resizable(False, False)
window.mainloop()
#push push