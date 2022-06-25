from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    windows=Tk()
    windows.withdraw()
    rob=simpledialog.askstring(title='orbs',prompt='are you happy?')
    if rob=='yes':
        messagebox.showinfo(title='nice',message='keep doing what you are doing')
    elif rob=='no':
        kyle=simpledialog.askstring(title='you ok?',prompt='do you want to be happy?')
    if kyle=='yes':
        messagebox.showinfo(title=':(',message='change something')
    elif kyle=='no':
        messagebox.showinfo(title='awwwwww', message="keep doing whatever you're doing")
    pass
