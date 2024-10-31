import os
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import webbrowser
import subprocess

class GifPlayer(tk.Label):
    def __init__(self, master, gif_path, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.frames = []
        self.load_gif(gif_path)
        self.current_frame = 0
        self.update_gif()

    def load_gif(self, gif_path):
        gif = Image.open(gif_path)
        try:
            while True:
                frame = ImageTk.PhotoImage(gif.copy())
                self.frames.append(frame)
                gif.seek(len(self.frames))
        except EOFError:
            pass

    def update_gif(self):
        frame = self.frames[self.current_frame]
        self.config(image=frame)
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.after(50, self.update_gif)

root = tk.Tk()
root.title("DOUBLE X")
root.geometry("800x400")
root.resizable(False, False)
root.iconbitmap() #icon โปรแหกรม แนะนำให้เป็น .ico


# โหลด GIF
gif_path = () #ตำแหน่งพื้นหลัง
gif_player = GifPlayer(root, gif_path)
gif_player.pack()



start_main = "https://cdn.discordapp.com/attachments/1288873922506522777/1301599305295069194/TEST.png?ex=67251050&is=6723bed0&hm=640ee0b724e853effaa02a7b8feb2d88895a06b7da126f631cd77d2f80d96e73&"
response_button = requests.get(start_main)
start_main_button = response_button.content
button_start_main_image = Image.open(BytesIO(start_main_button))
button_start_main = ImageTk.PhotoImage(button_start_main_image)

url_yt_button = "https://cdn.discordapp.com/attachments/1288873922506522777/1301605821192601721/TEST.png?ex=67251662&is=6723c4e2&hm=820f40782888f50fadaf042a8a631c49d9f33a580f25ab4c5f253e8d6b42fc05&"
response_button = requests.get(url_yt_button)
img_data_yt_button = response_button.content
button_ty_image = Image.open(BytesIO(img_data_yt_button))
button_yt_photo = ImageTk.PhotoImage(button_ty_image)

discord_button_url = "https://cdn.discordapp.com/attachments/1288873922506522777/1300012173350797352/1.png?ex=6724902f&is=67233eaf&hm=afd836338804cd3101ceb785743650c71eb93fef04007e030fcfd7ed9da8daab&"
response_discord_button = requests.get(discord_button_url)
img_data_discord_button = response_discord_button.content
button_discord_image = Image.open(BytesIO(img_data_discord_button))
button_discord_photo = ImageTk.PhotoImage(button_discord_image)

def open_yt_link():
    webbrowser.open("https://www.youtube.com/@_namo759")

def run_main():
    subprocess.Popen(["start", "cmd", "/k", "python", "main.py"], shell=True)

def open_discord_link():
    webbrowser.open("https://discord.gg/U2GBUxqGbm")

button_nuker = tk.Button(root, command=run_main, borderwidth=0, activebackground='black', image=button_start_main)
button_nuker.place(x=449, y=195, width=165, height=77)

button_open_yt = tk.Button(root, command=open_yt_link, borderwidth=0, activebackground='black', image=button_yt_photo)
button_open_yt.place(x=170, y=195, width=165, height=77)

button_discord = tk.Button(root, command=open_discord_link, borderwidth=0, activebackground='black', image=button_discord_photo)
button_discord.place(x=10, y=320, width=40, height=40)

button_nuker.config(highlightthickness=0, relief='flat')
button_open_yt.config(highlightthickness=0, relief='flat')
button_discord.config(highlightthickness=0, relief='flat')

root.mainloop()
