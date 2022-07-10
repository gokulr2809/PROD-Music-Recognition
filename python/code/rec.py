import sounddevice
from scipy.io.wavfile import write

#recording
def rec():
    fps = 15000
    duration = 7
    print("Recording....")
    recording = sounddevice.rec(int(duration*fps),samplerate=fps,channels=2)
    sounddevice.wait()
    print("Done!!!")
    b="rec.m4a"
    c = r"Samples\"
    file_name = c+b
    write(file_name,fps,recording)

def recorder():
    rec()
