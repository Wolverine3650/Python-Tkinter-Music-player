from tkinter import * 
from tkinter import filedialog
import pygame
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
root = Tk()

root.title("MP3 Player")
root.geometry("500x400")

#initialize pygame
pygame.mixer.init()

#Create a function to deal with time
def play_time():
	#check to see if song is stopped
	if stopped:
		return
	#grab current song time
	current_time= pygame.mixer.music.get_pos() / 1000
	#convert song time to time format
	converted_current_time = time.strftime('%M:%S',time.gmtime(current_time))
	#find current song length
	song = playlist_box.get(ACTIVE)
	song=f'C:/Users/sable/OneDrive/Desktop/Projects2020/Py-tkinter MP3 player/mp3/audio/{song}.mp3'
	song_mut=MP3(song)
	global song_length
	song_length = song_mut.info.length
	#convert to time format
	converted_song_length = time.strftime('%M:%S',time.gmtime(song_length))
	#check to see the song is over
	if int(song_slider.get())==int(song_length):
		stop()

	elif paused:
		#check to see if paused, if so -pass
		pass
	else:
		#Move slider along 1 second at a time
		next_time = int(song_slider.get()) + 1
		#output new time value to slider and to length of song
		song_slider.config(to=song_length,value=next_time)

		#convert slider position to time format

		converted_current_time = time.strftime('%M:%S',time.gmtime(int(song_slider.get())))

		#output slider
		status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}  ')

	if current_time>=1:
		status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}  ')
	#add current time to status bar
	
	#create loop to check time every second
	my_label.after(1000,play_time)
#create function to add one song to playlist
def add_song():
	song = filedialog.askopenfilename(initialdir='audio/',title='Choose A Song',filetypes=(( "mp3 Files","*.mp3"),
		))
	#my_label.config(text=song)
	#Strip out directory structure and .mp3 from song
	song=song.replace("C:/Users/sable/OneDrive/Desktop/Projects2020/Py-tkinter MP3 player/mp3/audio/","")
	song=song.replace(".mp3","")
	playlist_box.insert(END,song)
#create function to add many songs to playlist
def add_many_songs():
	songs = filedialog.askopenfilenames(initialdir='audio/',title='Choose A Song',filetypes=(( "mp3 Files","*.mp3"),
		))
	#loop through song list and replace directory structure
	for song in songs:
		#Strip out directory structure and .mp3 from song
		song=song.replace("C:/Users/sable/OneDrive/Desktop/Projects2020/Py-tkinter MP3 player/mp3/audio/","")
		song=song.replace(".mp3","")
		#Add to end of playlist
		playlist_box.insert(END,song)

#Create Function to delete one song from the list
def delete_song():
	#delete highlighted song from playlist
	playlist_box.delete(ANCHOR)
#Create Function to delete all song from the list
def delete_all_song():
	playlist_box.delete(0,END)


#create play function
def play():
	#set stopped to false since a song is now playing
	global stopped
	stopped=False
	#Reconstruct song with directory structure stuff
	song = playlist_box.get(ACTIVE)
	song=f'C:/Users/sable/OneDrive/Desktop/Projects2020/Py-tkinter MP3 player/mp3/audio/{song}.mp3'
	#load song with pygame mixer
	pygame.mixer.music.load(song)
	#play song with pygame mixer
	pygame.mixer.music.play(loops=0)
	#get song time
	play_time()


#Create stopped variable
global stopped
stopped=False
#create a stop function
def stop():
	#Stop the song
	pygame.mixer.music.stop()
	#clearplaylist box
	playlist_box.selection_clear(ACTIVE)
	status_bar.config(text='')
	#set out slider to zero
	song_slider.config(value=0)
	#set stop variable to TRUE
	global stopped
	stopped=True
#create function to play next song
def next_song():
	#reset slider position and status bar
	status_bar.config(text='')

	song_slider.config(value=0)
	#get the current song number
	next_one=playlist_box.curselection()
	#add one to current song number tuple/list
	next_one=next_one[0] + 1
	#grab the song title from playlist
	song=playlist_box.get(next_one)
	#add directory structure stuff
	song=f'C:/Users/sable/OneDrive/Desktop/Projects2020/Py-tkinter MP3 player/mp3/audio/{song}.mp3'
	#load song with pygame mixer
	pygame.mixer.music.load(song)
	#play song with pygame mixer
	pygame.mixer.music.play(loops=0)
	#clear active bar in playlist
	playlist_box.selection_clear(0,END)

	#move active bar to next song
	playlist_box.activate(next_one)

	#set active bar to next song
	playlist_box.selection_set(next_one,last=None)

#Create funtion to play previous song
def previous_song():
	#reset slider position and status bar
	status_bar.config(text='')

	song_slider.config(value=0)
	#get the current song number
	next_one=playlist_box.curselection()
	#subtract one to current song number tuple/list
	next_one=next_one[0] - 1
	#grab the song title from playlist
	song=playlist_box.get(next_one)
	#add directory structure stuff
	song=f'C:/Users/sable/OneDrive/Desktop/Projects2020/Py-tkinter MP3 player/mp3/audio/{song}.mp3'
	#load song with pygame mixer
	pygame.mixer.music.load(song)
	#play song with pygame mixer
	pygame.mixer.music.play(loops=0)
	#clear active bar in playlist
	playlist_box.selection_clear(0,END)

	#move active bar to next song
	playlist_box.activate(next_one)

	#set active bar to next song
	playlist_box.selection_set(next_one,last=None)


#create paused variable
global paused
paused = False
#Create Pause function
def pause(is_paused):
	global paused
	paused=is_paused

	if paused:
		#unpause
		pygame.mixer.music.unpause()
		paused = False
	else:
		#pause
		pygame.mixer.music.pause()
		paused = True

#create volume function
def volume(x):
	pygame.mixer.music.set_volume(volumn_slider.get())
#create main frame

#create a slide function for song position
def slide(x):
	song = playlist_box.get(ACTIVE)
	song=f'C:/Users/sable/OneDrive/Desktop/Projects2020/Py-tkinter MP3 player/mp3/audio/{song}.mp3'
	#load song with pygame mixer
	pygame.mixer.music.load(song)
	#play song with pygame mixer
	pygame.mixer.music.play(loops=0,start=song_slider.get())


main_frame=Frame(root)
main_frame.pack(pady=20)


#Create playlist BOX
playlist_box=Listbox(main_frame, bg="black", fg="green", width=60, selectbackground="green",selectforeground='black')
playlist_box.grid(row=0,column=0)

#Create volumn slider frame
volume_frame=LabelFrame(main_frame,text="Volumne")
volume_frame.grid(row=0,column=1,padx=20)
#create volumn slider
volumn_slider = ttk.Scale(volume_frame,from_=1,to=0,orient=VERTICAL,length=125,value=0,command=volume)
volumn_slider.pack(pady=10)

#create song slider
song_slider =ttk.Scale(main_frame,from_=0,to=100,orient=HORIZONTAL,length=360,value=0,command=slide)
song_slider.grid(row=2,column=0,pady=20)
#Define Button Images For COntrols
back_btn_img= PhotoImage(file='images/back50.png')
forward_btn_img=PhotoImage(file='images/forward50.png')
play_btn_img=PhotoImage(file='images/play50.png')
pause_btn_img=PhotoImage(file='images/pause50.png')
stop_btn_img=PhotoImage(file='images/stop50.png')

#create button frame
control_frame=Frame(main_frame)
control_frame.grid(row=1,column=0,pady=20)
#Create Buttons (play,pause)
back_button=Button(control_frame, image=back_btn_img,borderwidth=0,command=previous_song)
forward_button=Button(control_frame, image=forward_btn_img,borderwidth=0,command=next_song)
play_button=Button(control_frame, image=play_btn_img,borderwidth=0,command=play)
pause_button=Button(control_frame, image=pause_btn_img,borderwidth=0,command=lambda: pause(paused))
stop_button=Button(control_frame, image=stop_btn_img,borderwidth=0,command=stop)

back_button.grid(row=0,column=0,padx=10)
forward_button.grid(row=0,column=1,padx=10)
play_button.grid(row=0,column=2,padx=10)
pause_button.grid(row=0,column=3,padx=10)
stop_button.grid(row=0,column=4,padx=10)

#Create manin MENU
my_menu=Menu(root)
root.config(menu=my_menu)


#Create add Song menu DropDown
add_song_menu= Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Add Songs",menu=add_song_menu)
#add one song to playlist
add_song_menu.add_command(label="Add one Song to Playlist",command=add_song)
#add many songs to playlist
add_song_menu.add_command(label="Add Many Song to Playlist",command=add_many_songs)


#Create Delete song menu dropdowns
remove_song_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Remove Songs",menu=remove_song_menu)
remove_song_menu.add_command(label="Delete a song from playlist",command=delete_song)
remove_song_menu.add_command(label="Delete all songs from playlist",command=delete_all_song)

#create status bar
status_bar = Label(root,text='',bd=1,relief=GROOVE,anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=2)

#Temporary label
my_label=Label(root,text='')
my_label.pack(pady=20)
root.mainloop()