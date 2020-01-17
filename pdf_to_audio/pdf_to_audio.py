from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pdftotext
from gtts import gTTS

Tk().withdraw()
filelocation = askopenfilename()

with open(filelocation, "rb") as f:
    pdf = pdftotext.PDF(f)

string_of_text = ''
for text in pdf:
    string_of_text += text

final_file = gTTS(text=string_of_text, lang='fr')
final_file.save("speech.mp3")
