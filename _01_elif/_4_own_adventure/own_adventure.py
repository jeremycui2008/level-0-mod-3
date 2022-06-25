from tkinter import simpledialog, messagebox, Tk
import webbrowser



def play_video(url):
    webbrowser.open(url)
# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
messagebox.showinfo(title='story', message='you wake up in a forest amd find 2 paths, you do not know where either leads but you know you must go down one of the paths, decide which path to go down.')
orb=paths=simpledialog.askstring(title='choice 1',prompt='do you choose path 1 or path 2?')
if orb=='path 1':
    messagebox.showinfo(title='death',message='you died')
    play_video('https://www.youtube.com/watch?v=6O5fRLU0tZo')
elif orb=='path 2':
    messagebox.showinfo(title='you lived',message='you find a cave along the path and decide to take refuge in it for the day, you also find some rations and decide to take them, as you prepare to sleep you hear some noises, do you want to stay in the cave or head out?')
    beans=simpledialog.askstring(title='stay or leave',prompt='do you leave the cave or stay?')
    if beans=='leave':
        messagebox.showinfo(title='you were consumed', message='after leaving the cave some entity consumed your whole being and you were sent into some sort of limbo eternally.')
    elif beans=='stay':
        messagebox.showinfo(title='you hear the sound pass',message='you hear the noise pass and whatever thing that was close to the cave leave the area. You know this is your best opportunity to leave so you leave and run a good distance from the cave. After you finish running and make sure nothing is around you very suddenly hear a screech and turn around to see an animal has somehow appeared behind you.The animal seemed horribly disfigured and like something straight out of a horror movie. It starts running towards you and you notice there is a waterfall. You can either jump off the waterfall or you can attempt to outrun it, what do you do?')
        double=simpledialog.askstring(title='???', prompt='run or jump?')
        if double=='jump':
            messagebox.showinfo(title='freedom?', message='you plunged into the water and held your breath after a bit you surfaced and found that the creature was gone, when you looked around you noticed you had escaped the forest and could see the landscape better. You saw man villages and a larger kingdom and you knew that whatever this place was it was not home, but you knew you would have to survive whatever twisted things this new world woulf throw at you, somehow... to be continued never.')
        elif double=='run':
            messagebox.showinfo(title='demise',message='you were consumed and sent to an eternal limbo.')
