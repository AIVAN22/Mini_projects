from tkinter import *
from tkinter import filedialog
import pygame
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title("MP3_PLAYER")
root.geometry("620x300")

# pygame_mixer
pygame.mixer.init()

# Volume
def vol(x):
    pygame.mixer.music.set_volume(slider_vol.get())
    current_vol = pygame.mixer.music.get_volume()


# time song
def play_time():
    if stopped:
        return
    current_time = pygame.mixer.music.get_pos() / 1000

    the_current_time = time.strftime("%M:%S", time.gmtime(current_time))
    # Change the path to make it work
    # Current playing song
    the_song = playlist.get(ACTIVE)
    the_song = f"C:/Users/Alexander/P/media/audio/{the_song}.mp3"

    # geting length of the song with mutigen
    mutagen_song = MP3(the_song)

    global song_len
    song_len = mutagen_song.info.length
    format_mutagen_time = time.strftime("%M:%S", time.gmtime(song_len))

    current_time += 1
    if int(slider.get()) == int(song_len):
        status_bar.config(text=f"{format_mutagen_time}")
    elif paused:
        pass
    elif int(slider.get()) == int(current_time):
        slider_position = int(song_len)
        slider.config(to=slider_position, value=int(current_time))
    else:
        slider_position = int(song_len)
        slider.config(to=slider_position, value=int(slider.get()))
        the_current_time = time.strftime("%M:%S", time.gmtime((int(slider.get()))))
        status_bar.config(text=f"{slider.get()}/{format_mutagen_time}")

        next_time = int(slider.get()) + 1
        slider.config(value=next_time)

    # res time for slider

    status_bar.after(1000, play_time)


# delete song
def delete_song():
    stop()
    playlist.delete(ANCHOR)
    pygame.mixer.music.stop()


# delete sons
def delete_songs():
    stop()
    playlist.delete(0, END)
    pygame.mixer.music.stop()


# add songs
def add_multiple_song():
    the_songs = filedialog.askopenfilenames(
        initialdir="media/audio/",
        title="Pick song",
        filetypes=(("mp3 files", "*.mp3"),),
    )
    # loop to replace songs
    for the_song in the_songs:
        the_song = the_song.replace("C:/Users/Alexander/P/media/audio/", "")
        the_song = the_song.replace(".mp3", "")
        playlist.insert(END, the_song)


# play song
def play():

    global stopped
    stopped = False
    the_song = playlist.get(ACTIVE)
    the_song = f"C:/Users/Alexander/P/media/audio/{the_song}.mp3"

    pygame.mixer.music.load(the_song)
    pygame.mixer.music.play(loops=0)
    # calling the timer when song is started
    play_time()
    current_vol = pygame.mixer.music.get_volume()


# call next song
def next():
    status_bar.config(text="")
    slider.config(value=0)
    # finding the index of the tuple
    next_song = playlist.curselection()
    # adding one to the index to call next index
    next_song = next_song[0] + 1
    the_song = playlist.get(next_song)
    the_song = f"C:/Users/Alexander/P/media/audio/{the_song}.mp3"

    pygame.mixer.music.load(the_song)
    pygame.mixer.music.play(loops=0)
    playlist.select_clear(0, END)
    playlist.activate(next_song)
    playlist.select_set(next_song, last=None)


# call previews song
def back():
    status_bar.config(text="")
    slider.config(value=0)
    next_song = playlist.curselection()
    next_song = next_song[0] - 1
    the_song = playlist.get(next_song)
    the_song = f"C:/Users/Alexander/P/media/audio/{the_song}.mp3"

    pygame.mixer.music.load(the_song)
    pygame.mixer.music.play(loops=0)
    playlist.select_clear(0, END)
    playlist.activate(next_song)
    playlist.select_set(next_song, last=None)


# pause song
global paused
paused = False


def pause(is_paused):
    global paused
    paused = is_paused

    if is_paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


global stopped
stopped = False

# stop song
def stop():
    status_bar.config(text="")
    slider.config(value=0)

    pygame.mixer.music.stop()
    playlist.select_clear(ACTIVE)
    status_bar.config(text="")

    global stopped
    stopped = True


def slide(x):
    the_song = playlist.get(ACTIVE)
    the_song = f"C:/Users/Alexander/P/media/audio/{the_song}.mp3"

    pygame.mixer.music.load(the_song)
    pygame.mixer.music.play(loops=0, start=int(slider.get()))


Frame_playlist = Frame(root)
Frame_playlist.pack(side="left")

# play_list
playlist = Listbox(
    Frame_playlist,
    bg="lightblue",
    fg="black",
    width=50,
    selectbackground="lightgreen",
    selectforeground="gray",
)
playlist.pack(padx=25)

# player_buttons_images
play_img = PhotoImage(file="media/images/play_50.png")
pause_img = PhotoImage(file="media/images/pause_50.png")
next_img = PhotoImage(file="media/images/next_50.png")
back_img = PhotoImage(file="media/images/back_50.png")
stop_img = PhotoImage(file="media/images/stop_50.png")
#

# Control Buttons
Frame_control = Frame(root)
Frame_control.pack(side="right", padx=55)

play_button = Button(
    Frame_control, image=play_img, borderwidth=2, command=play, width=120
)
pause_button = Button(
    Frame_control,
    image=pause_img,
    borderwidth=2,
    command=lambda: pause(paused),
    width=120,
)
next_button = Button(
    Frame_control, image=next_img, borderwidth=2, command=next, width=120
)
back_button = Button(Frame_control, image=back_img, borderwidth=2, width=120)
stop_button = Button(
    Frame_control, image=stop_img, borderwidth=2, command=stop, width=120
)

play_button.grid(row=0, column=0, pady=2)
pause_button.grid(row=1, column=0, pady=2)
next_button.grid(row=2, column=0, pady=2)
back_button.grid(row=3, column=0, pady=2)
stop_button.grid(row=4, column=0, pady=2)

# menu

the_menu = Menu(root)
root.config(menu=the_menu)

add_song = Menu(the_menu)
the_menu.add_command(label="Add songs", command=add_multiple_song)

# delete_song menu
delete_menu = Menu(the_menu)
the_menu.add_cascade(label="Delete songs", menu=delete_menu)
delete_menu.add_command(label="Delete song", command=delete_song)
delete_menu.add_command(label="Delete all songs", command=delete_songs)

# Time
status_bar = Label(Frame_playlist, text="", bd=3, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side="top", padx=25, pady=12)


# slider vol

slider_vol = ttk.Scale(
    root,
    from_=0,
    to=1,
    orient=VERTICAL,
    value=1,
    command=vol,
    length=120,
)
slider_vol.pack(pady=60)
# Slider song

slider = ttk.Scale(
    Frame_playlist,
    from_=0,
    to=100,
    orient=HORIZONTAL,
    value=0,
    command=slide,
    length=260,
)
slider.pack(pady=6)

root.mainloop()
