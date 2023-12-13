import tkinter as tk
import pyaudio
import wave
import os
import time

class VoiceRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder App")

        self.record_button = tk.Button(self.root, text="Record", command=self.start_recording)
        self.record_button.pack(pady=20)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.timer_label = tk.Label(self.root, text="00:00")
        self.timer_label.pack(pady=10)

        self.file_name_entry = tk.Entry(self.root)
        self.file_name_entry.pack(pady=10, padx=20)

        self.start_time = None
        self.timer_running = False
        self.file_path = None  # Define file_path globally

    def start_timer(self):
        self.start_time = time.time()
        self.update_timer()

    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            formatted_time = time.strftime('%M:%S', time.gmtime(elapsed_time))
            self.timer_label.config(text=formatted_time)
            self.root.after(1000, self.update_timer)

    def start_recording(self):
        self.record_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.file_name = self.file_name_entry.get()
        if not self.file_name:
            self.file_name = "recording.wav"

        directory_path = r"D:\Studies\Interships\Coderscave\Python Development [Nov to Dec 2023]\Tasks\Recordings"
        self.file_path = os.path.join(directory_path, self.file_name)

        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        self.frames = []

        self.timer_running = True
        self.start_timer()

        self.root.update()
        self.is_recording = True
        while self.is_recording:
            data = self.stream.read(1024)
            self.frames.append(data)
            self.root.update()

    def stop_recording(self):
        self.is_recording = False
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

        wave_file = wave.open(self.file_path, 'wb')
        wave_file.setnchannels(1)
        wave_file.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        wave_file.setframerate(44100)
        wave_file.writeframes(b''.join(self.frames))
        wave_file.close()

        self.record_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.file_name_entry.delete(0, tk.END)
        self.file_name_entry.insert(tk.END, "Recording saved")

        self.timer_running = False
        self.timer_label.config(text="00:00")

def main():
    root = tk.Tk()
    app = VoiceRecorderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
