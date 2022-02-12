import sounddevice
from scipy.io.wavfile import write
import random
import string

def file_name():
    #generating random file name
    string.ascii_letters
    arry=[]
    length = 12
    def random_string(length):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))
    string.ascii_letters + string.digits
    a=random_string(length)
    file1 = open(r"file.txt", 'r')
    Lines = file1.readlines() 
    for line in Lines:
        x=line.strip()
        arry.append(x)
    for i in arry:
        if a == i :
            a = random_string(length-1)
    file1.close
    furl = r"file.txt"
    print(a, file=open(furl, "a+"))
    file1.close
    return a

#recording
def rec(a):
    fps = 15000
    duration = 7
    print("Recording....")
    recording = sounddevice.rec(int(duration*fps),samplerate=fps,channels=2)
    sounddevice.wait()
    print("Done!!!")
    b=".m4a"
    c = r"Samples\ "
    file_name = c + a + b
    write(file_name,fps,recording)

def recorder():
    rand_filename = file_name()
    rec(rand_filename)
    return rand_filename
