import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip

class MP4toMP3Converter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MP4 to MP3 Converter")
        self.mp4_file_path = None

        tk.Label(self, text="Select an MP4 file and convert it to MP3").pack(pady=10)

        self.select_button = tk.Button(self, text="Select MP4 File", command=self.select_file)
        self.select_button.pack(pady=5)

        self.convert_button = tk.Button(self, text="Convert to MP3", state='disabled', command=self.convert_to_mp3)
        self.convert_button.pack(pady=5)

    def select_file(self):
        self.mp4_file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
        if self.mp4_file_path:
            self.convert_button['state'] = 'normal'
            messagebox.showinfo("File Selected", "MP4 file selected successfully!")

    def convert_to_mp3(self):
        mp3_file_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                      filetypes=[("MP3 files", "*.mp3")])
        if mp3_file_path:
            try:
                video_clip = VideoFileClip(self.mp4_file_path)
                video_clip.audio.write_audiofile(mp3_file_path)
                video_clip.close()
                messagebox.showinfo("Success", "File has been converted successfully!")
            except Exception as e:
                messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = MP4toMP3Converter()
    app.mainloop()
