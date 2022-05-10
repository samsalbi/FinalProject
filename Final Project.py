#import tk
import tkinter
import pickle

#create class for program
class Game:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.attributes('-fullscreen', True)

        #self.main_window.geometry("800x600")
        self.w, self.h = self.main_window.winfo_screenwidth(), self.main_window.winfo_screenheight()
        self.main_window.geometry("%dx%d" % (self.w, self.h))

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.very_bottom_frame = tkinter.Frame(self.main_window)
        #buttons
        self.prompt_label = tkinter.Label(self.top_frame, text='Welcome to Wordle!\n', font="Arial, 60")
        self.instructions = tkinter.Button(self.mid_frame, text='How To Play', height=1, width=10, font="Arial, 20", command=self.opened)
        self.play_button = tkinter.Button(self.mid_frame, text='Play', height=1, width=10, font="Arial, 20", command=self.opened2)
        self.play_button.pack(side='left', padx=50, pady=100)
        self.quit_button = tkinter.Button(self.mid_frame, text='Quit', command=self.quit, height=1, width=10, font="Arial, 20")
        self.quit_button.pack(side='right', padx=50, pady=100)
        self.bg = tkinter.PhotoImage(file="spacebg.gif")
        self.my_bg = tkinter.Label(self.main_window, image=self.bg)
        self.my_bg.place(x=0, y=0, relwidth=1, relheight=1)
        self.my_bg.pack(fill="both", expand=True)

        self.instructions.pack(side='left')
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
        self.instructions_window.geometry("1000x550")
        self.instructions_window.title('How to play Wordle!')
        self.instructions_header = tkinter.Label(self.instructions_window, text='\nInstructions \n _______________ \n', font="Arial, 50")
        self.instructions_header.pack()
        self.instructions_description = tkinter.Label(self.instructions_window,
                                                      text='Step 1: Press the play button at the home screen\nStep 2: Press the current level you are on, if starting; press 1\nStep 3: Guess the word based on the theme, you can buy a hint with points\nStep 4: Have fun!', font="Arial, 22", justify="left" )
        self.instructions_description.pack()
        self.back_button = tkinter.Button(self.instructions_window, text='Back', font="Arial, 20", height=1, width=10, command=self.back)
        self.back_button.pack(side='top', pady=10)

    def opened2(self):
        self.play_window = tkinter.Toplevel()
        self.play_window.title('Select A Level!')
        self.play_window.attributes('-fullscreen', True)
        self.play_label = tkinter.Label(self.play_window, text='Select Your Current Level!', font="Arial, 100")
        self.play_label.pack(pady=20)
        self.level1_button = tkinter.Button(self.play_window, text='Level 1', height=3, width=10, command=self.level1)
        self.level1_button.pack(side='top', padx=100)
        #self.level2_button = tkinter.Button(self.play_window, text='Ｌｅｖｅｌ ２ （ＢＯＳＳ）', height=3, width=20)
        #self.level2_button.pack(side='right', padx=400)
        self.back_button = tkinter.Button(self.play_window, text='Back', font="Arial, 20", height=1, width=10)
        self.back_button.pack(side='bottom', pady=10)

    def level1(self):
        self.level1_theme = tkinter.Label(self.play_window, text='You are in level 1 and your theme is: Class Subject:')
        self.level1_theme.pack(side='left', padx=1)
        self.level1_guess = tkinter.Text(self.play_window, width=30, height=1)
        self.level1_guess.pack(side='left', padx=1)
        self.level1_enter_button = tkinter.Button(self.play_window, text='Enter', font="Arial, 20", height=1, width=10, command=self.enter)
        self.level1_enter_button.pack()
        self.level1_hint_button = tkinter.Button(self.play_window, text='Hint', font="Arial, 20", height=1, width=10, command=self.hint)
        self.level1_hint_button.pack()
        self.level_1_score_label = tkinter.Radiobutton(self.play_window, text='Score:' + str(self.score), font="Arial, 20", height=1, width=10, command=self.label)
        self.level_1_score_label.pack()


    def save_file(self):
        try:
            save_file = open('save.dat', 'wb')
            self.save = pickle.load(save_file)
            save_file.close()
        except (FileNotFoundError, IOError):
            self.save = []





    def label(self, save_file):
        self.score = 0
        self.enter()
        pickle.load(save_file)
        pickle.dump(self.score, save_file)




    def enter(self):
        self.score = 0
        if self.level1_guess == "Math" or "math":
            self.score = self.score + 3
        else:
            self.level1_guess = tkinter.Text(self.play_window, width=30, height=1)
            self.level1_guess.pack(side='left', padx=1)

    def hint(self):
        self.score = self.score - 3
        self.question = tkinter.Label(self.play_window, text="What is the tallest mountain?")
        self.question_text = tkinter.Text(self.play_window, width=30, height=1)
        if self.question_text == "Mount Everest":
            self.hint_answer = tkinter.Label(self.play_window, text="The word is 4 letters")
            self.hint()
        else:
            self.hint()


    #def level2(self):



    def back(self):
        self.instructions_window.destroy()

    def back2(self):
        self.play_window.destroy()

    def quit(self):
        self.main_window.destroy()


#run the code
game = Game()
