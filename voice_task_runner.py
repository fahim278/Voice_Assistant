# # ===============================
# # 🎙️ AI Voice Command Task Runner
# # Built by Fahim 💻
# # ===============================

# import speech_recognition as sr
# import pyttsx3
# import pyautogui
# import os
# import webbrowser
# import time
# import subprocess

# # =============== SETUP ===============
# engine = pyttsx3.init()
# engine.setProperty('rate', 175)
# engine.setProperty('volume', 1.0)

# def speak(text):
#     """Convert text to speech"""
#     print("🤖 AI Assistant:", text)
#     engine.say(text)
#     engine.runAndWait()

# def listen_command():
#     """Listen to user voice input"""
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("\n🎧 Listening...")
#         r.adjust_for_ambient_noise(source)
#         audio = r.listen(source)
#     try:
#         command = r.recognize_google(audio)
#         print(f"🎯 Command Detected: {command}\n")
#         return command.lower()
#     except sr.UnknownValueError:
#         speak("Sorry, I could not understand that.")
#         return ""
#     except sr.RequestError:
#         speak("Network error while recognizing speech.")
#         return ""

# # =============== TASK ACTIONS ===============
# def process_command(command):
#     """Decide and execute actions based on command"""
#     if "open browser" in command or "open google" in command:
#         speak("Opening Google Chrome...")
#         webbrowser.open("https://www.google.com")

#     elif "open youtube" in command:
#         speak("Opening YouTube...")
#         webbrowser.open("https://www.youtube.com")

#     elif "open notepad" in command:
#         speak("Opening Notepad...")
#         os.system("notepad")

#     elif "play music" in command:
#         music_path = "C:\\Users\\Public\\Music\\Sample Music\\Kalimba.mp3"  # change path if needed
#         if os.path.exists(music_path):
#             speak("Playing your favorite music...")
#             os.startfile(music_path)
#         else:
#             speak("Music file not found. Please update the path.")

#     elif "take screenshot" in command:
#         speak("Taking a screenshot...")
#         screenshot = pyautogui.screenshot()
#         file_name = f"screenshot_{int(time.time())}.png"
#         screenshot.save(file_name)
#         speak(f"Screenshot saved as {file_name}")

#     elif "open camera" in command:
#         speak("Opening camera...")
#         subprocess.run("start microsoft.windows.camera:", shell=True)

#     elif "shutdown" in command:
#         speak("Shutting down your computer in 5 seconds...")
#         os.system("shutdown /s /t 5")

#     elif "restart" in command:
#         speak("Restarting your computer in 5 seconds...")
#         os.system("shutdown /r /t 5")

#     elif "lock" in command:
#         speak("Locking your computer...")
#         ctypes.windll.user32.LockWorkStation()

#     elif "hello" in command:
#         speak("Hello Fahim! How can I assist you today?")

#     elif "time" in command:
#         current_time = time.strftime("%I:%M %p")
#         speak(f"The current time is {current_time}")

#     elif "exit" in command or "stop" in command or "quit" in command:
#         speak("Goodbye Fahim! Have a productive day!")
#         exit()

#     else:
#         speak("Sorry, I didn’t understand that command.")

# # =============== MAIN LOOP ===============
# if __name__ == "__main__":
#     speak("Hello Fahim, your AI Automation Assistant is now active.")
#     while True:
#         command = listen_command()
#         if command:
#             process_command(command)



##   Fully Functional Code ###


# import sounddevice as sd
# from scipy.io.wavfile import write
# import speech_recognition as sr
# import pyttsx3
# import pyautogui
# import time
# import os

# # === Text-to-Speech ===
# engine = pyttsx3.init()
# engine.setProperty('rate', 175)

# def speak(text):
#     print("🤖 AI Assistant:", text)
#     engine.say(text)
#     engine.runAndWait()

# # === Record Audio using sounddevice ===
# def record_audio(filename="command.wav", duration=5, fs=44100):
#     speak("Listening... please speak your command.")
#     print("🎙️ Recording...")
#     audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
#     sd.wait()
#     write(filename, fs, audio)
#     print("✅ Audio saved:", filename)
#     return filename

# # === Recognize speech from saved audio ===
# def recognize_speech(filename="command.wav"):
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(filename) as source:
#         audio_data = recognizer.record(source)
#     try:
#         text = recognizer.recognize_google(audio_data)
#         print("🗣️ You said:", text)
#         return text.lower()
#     except sr.UnknownValueError:
#         speak("Sorry, I could not understand.")
#         return ""
#     except sr.RequestError:
#         speak("Speech service unavailable.")
#         return ""

# # === Execute actions ===
# def run_command(cmd):
#     if "open browser" in cmd:
#         speak("Opening browser...")
#         os.system("start chrome")
#     elif "close browser" in cmd:
#         speak("Closing browser...")
#         os.system("taskkill /IM chrome.exe /F")
#     elif "open notepad" in cmd:
#         speak("Opening Notepad...")
#         os.system("notepad")
#     elif "take screenshot" in cmd:
#         speak("Taking screenshot...")
#         img = pyautogui.screenshot()
#         img.save("screenshot.png")
#         speak("Screenshot saved.")
#     elif "play music" in cmd:
#         speak("Playing sample sound...")
#         os.startfile("C:\\Windows\\Media\\Alarm01.wav")
#     elif "hello" in cmd:
#         speak("Hello Fahim, I am ready for your next command.")
#     elif "exit" in cmd or "quit" in cmd:
#         speak("Goodbye Fahim!")
#         exit(0)
#     else:
#         speak("I didn’t recognize that command.")

# # === Main ===
# if __name__ == "__main__":
#     speak("Hello Fahim, your AI Automation Assistant is now active.")
#     while True:
#         filename = record_audio()
#         command = recognize_speech(filename)
#         if command:
#             run_command(command)
#         speak("You can give another command or say exit to quit.")
#         time.sleep(1)



import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import pyttsx3
import pyautogui
import time
import os

# === Text-to-Speech ===
engine = pyttsx3.init()
engine.setProperty('rate', 175)

def speak(text):
    print("🤖 AI Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# === Record Audio using sounddevice ===
def record_audio(filename="command.wav", duration=5, fs=44100):
    speak("Listening... please speak your command or stay silent to stop.")
    print("🎙️ Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, audio)
    print("✅ Audio saved:", filename)
    return filename

# === Recognize speech from saved audio ===
def recognize_speech(filename="command.wav"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        print("🗣️ You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        return ""  # No voice or unclear audio
    except sr.RequestError:
        speak("Speech service unavailable.")
        return ""

# === Execute actions ===
def run_command(cmd):
    if "open browser" in cmd:
        speak("Opening browser...")
        os.system("start chrome")
    elif "close browser" in cmd:
        speak("Closing browser...")
        os.system("taskkill /IM chrome.exe /F")
    elif "open notepad" in cmd:
        speak("Opening Notepad...")
        os.system("notepad")
    elif "take screenshot" in cmd:
        speak("Taking screenshot...")
        img = pyautogui.screenshot()
        img.save("screenshot.png")
        speak("Screenshot saved.")
    elif "play music" in cmd:
        speak("Playing sample sound...")
        os.startfile("C:\\Windows\\Media\\Alarm01.wav")
    elif "hello" in cmd:
        speak("Hello Fahim, I am ready for your next command.")
    elif "exit" in cmd or "quit" in cmd or "stop" in cmd:
        speak("Goodbye Fahim! See you soon.")
        return False
    else:
        speak("I didn’t recognize that command.")
    return True

# === Main ===
if __name__ == "__main__":
    speak("Hello Fahim, your AI Automation Assistant is now active.")
    while True:
        filename = record_audio()
        command = recognize_speech(filename)

        # Stop if user stays silent
        if not command.strip():
            speak("No command detected. Stopping now. Goodbye!")
            break

        should_continue = run_command(command)
        if not should_continue:
            break

        speak("You can give another command or stay silent to stop.")
        time.sleep(1)
