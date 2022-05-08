#import tk
import tkinter

#create class for program
class HomeScreen:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("800x600")
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.very_bottom_frame = tkinter.Frame(self.main_window)
        #buttons
        self.prompt_label = tkinter.Label(self.top_frame, text='Welcome to Wordle!', font=("Arial, 60"))
        self.instructions = tkinter.Button(self.bottom_frame, text='How To Play', height=1, width=10, font="Arial, 20", command=self.opened)
        self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.quit)
        self.quit_button.pack(side='bottom')
        self.bg = tkinter.PhotoImage(file="spacebg.gif")
        self.my_bg = tkinter.Label(self.main_window, image=self.bg)
        self.my_bg.place(x=0, y=0, relwidth=1, relheight=1)
        self.my_bg.pack(fill="both", expand=True)

        self.instructions.pack(side='bottom')
        self.my_bg.pack()
        self.prompt_label.pack()
        #self.instructions_window_text.pack()
        #pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        self.very_bottom_frame.pack()
        tkinter.mainloop()
    #back button
    def opened(self):
        self.instructions_window = tkinter.Toplevel()
        self.instructions_window.title('How to play Wordle!')
        self.instructions_window_text = tkinter.Label(self.instructions_window, text='Step 1: Play')
        self.instructions_window_text.pack()
        self.back_button = tkinter.Button(self.instructions_window, text='Back', command=self.back)
        self.back_button.pack(side='bottom')

    def back(self):
        self.instructions_window.destroy()

    def quit(self):
        self.main_window.destroy()

#run the code
home_screen = HomeScreen()


class PlayScreen(HomeScreen):
    def __init__(self):
        HomeScreen.__init__(self)
        self.main_window = tkinter.Tk()
        self.main_window.geometry("800x600")
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.very_bottom_frame = tkinter.Frame(self.main_window)
        self.play_button = tkinter.Button(self.mid_frame, text='Play', height=1, width=10, font=("Arial, 20"), command=self.opened2)
        self.play_button.pack(pady=80)

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        self.very_bottom_frame.pack()
        tkinter.mainloop()

    def opened2(self):
        self.play_window = tkinter.Toplevel()
        self.play_window.title('Select A Level!')
        self.back_button = tkinter.Button(self.play_window, text='Back', command=self.back)
        self.back_button.pack(side='bottom')

    def back(self):
        self.play_window.destroy()


play_screen = PlayScreen()
