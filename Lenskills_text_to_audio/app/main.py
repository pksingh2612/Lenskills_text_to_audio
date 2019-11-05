import os
from gtts import gTTS

f = open("file.txt", "r")
x=f.read()
#print(x)

#Saving part starts from here 
tts = gTTS(x,lang='en')
tts.save("saved_file.mp3")
print("File saved!")

#Playing Audio File
print("Playing Audio")
os.system("saved_file.mp3")
print("Done Playing")
