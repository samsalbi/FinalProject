# import tk
import tkinter
import pickle
import GameClass


# create class for program
class Game:
    def __init__(self, master):
        self.master = master
        self.master.attributes('-fullscreen', True)
        self.master.title('Wordle Game!')
        # self.main_window.geometry("800x600")
        self.w, self.h = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        self.master.geometry("%dx%d" % (self.w, self.h))

        self.top_frame = tkinter.Frame(self.master)
        self.mid_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)
        self.very_bottom_frame = tkinter.Frame(self.master)
        # buttons
        self.prompt_label = tkinter.Label(self.top_frame, text='Welcome to Wordle!', font="Arial, 60")
        self.instructions = tkinter.Button(self.bottom_frame, text='How To Play', height=1, width=10, font="Arial, 20",
                                           command=self.how_to_play)
        self.top_score = []
        self.top_score_name = tkinter.StringVar()
        self.Leader_header_label = tkinter.Label(self.mid_frame, text="Users who completed Wordle!\n ------------------------\n\n", font="Arial, 20")

        self.Leader_label = tkinter.Label(self.mid_frame, textvariable=self.top_score_name,
                                          font="Arial, 20")

        self.Leader_header_label.pack()
        self.Leader_label.pack()

        self.play_button = tkinter.Button(self.bottom_frame, text='Play', height=1, width=10, font="Arial, 20",
                                          command=self.play)
        self.play_button.pack(side='left', padx=50, pady=100)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.quit, height=1, width=10,
                                          font="Arial, 20")
        self.quit_button.pack(side='right', padx=50, pady=100)
        self.bg = tkinter.PhotoImage(file="spacebg.gif")
        self.my_bg = tkinter.Label(self.master, image=self.bg)
        self.my_bg.place(x=0, y=0, relwidth=1, relheight=1)
        self.my_bg.pack(fill="both", expand=True)
        #load
        self.load_top_score()
        self.instructions.pack(side='left')
        self.my_bg.pack()
        self.prompt_label.pack()
        # self.instructions_window_text.pack()
        # pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        self.very_bottom_frame.pack()
        tkinter.mainloop()

    def quit(self):
        self.master.destroy()

    def how_to_play(self):
        _ = HowToPlay(self.master)

    def play(self):
        _ = Play(self.master)

    def load_top_score(self):
        filename = "top-score_list.dat"
        try:
            input_file = open(filename, 'rb')
            self.top_score = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.top_score = []
        if len(self.top_score) >= 1:
            self.top_score_name.set("\n".join(self.top_score))
        else:
            self.top_score_name.set("Try wordle and pass the BOSS level to be on the leaderboard")


class HowToPlay:
    def __init__(self, master):
        self.instructions_window = tkinter.Toplevel(master)
        self.instructions_window.geometry("1000x550")
        self.instructions_window.title('How to play Wordle!')
        self.instructions_header = tkinter.Label(self.instructions_window, text='\nInstructions \n _______________ \n',
                                                 font="Arial, 40")
        self.instructions_header.pack()
        self.instructions_description = tkinter.Label(self.instructions_window,
                                                      text='Step 1: Press the play button at the home screen\nStep 2: '
                                                           'Press the current level you are on, if starting; press 1 '
                                                           '\nStep 3: Guess the word based on the theme, you can buy '
                                                           'a hint with points\nStep 4: Have fun!', font="Arial, 22",
                                                      justify="left")
        self.instructions_description.pack()
        self.back_button = tkinter.Button(self.instructions_window, text='Close', font="Arial, 20", height=1, width=10,
                                          command=self.close)
        self.back_button.pack(side='top', pady=10)

    def close(self):
        self.instructions_window.destroy()


class Play:
    def __init__(self, master):

        self.play_window = tkinter.Toplevel(master)
        self.play_window.title('GAME ON')
        self.play_window.attributes('-fullscreen', True)
        self.level_themes = []
        self.top_score=[]

        self.theme_index = tkinter.IntVar()
        self.current_score = tkinter.IntVar()
        self.Add_to_leaderboard = tkinter.BooleanVar()
        self.current_score_label = tkinter.StringVar()
        # Set frames
        self.top_frame = tkinter.Frame(self.play_window)
        self.play_frame = tkinter.Frame(self.play_window)
        self.bottom_frame = tkinter.Frame(self.play_window)
        # Set labels
        self.play_label = tkinter.Label(self.top_frame, text='Guess the word!', font="Arial, 50", pady=10,
                                        justify="left", padx=50)

        self.score_label = tkinter.Label(self.top_frame, textvariable=self.current_score_label, font="Arial, 30",
                                         justify="right")
        self.play_label.pack(side=tkinter.TOP, padx=10, pady=5)
        self.score_label.pack(side=tkinter.BOTTOM, padx=200, pady=10, ipadx=100, ipady=20)

        self.level1_button = tkinter.Button(self.play_frame, text='Play level 1', height=3, width=10,
                                            command=self.play_level1)
        self.level1_button.pack(side='left', padx=100)

        self.level2_button = tkinter.Button(self.play_frame, text='Ｌｅｖｅｌ ２ （ＢＯＳＳ）', height=3, width=20,
                                            command=self.play_level2)

        self.current_theme = tkinter.StringVar()
        self.level_theme = tkinter.Label(self.play_frame, textvariable=self.current_theme, font="Arial, 20")
        self.level_guess = tkinter.Text(self.play_frame, width=30, height=1, font="Arial, 20")
        self.level_enter_button = tkinter.Button(self.play_frame, text='Enter', font="Arial, 20", height=1, width=10,
                                                 command=self.evaluate)
        self.level_theme.pack(side=tkinter.TOP, pady=10)
        # hint section
        self.hint_answer = tkinter.StringVar()
        self.hint_label = tkinter.Label(self.play_frame, textvariable=self.hint_answer)
        self.back_button = tkinter.Button(self.bottom_frame, text='Quit', font="Arial, 20", height=1, width=10,
                                          command=self.exit)
        self.level_hint_button = tkinter.Button(self.bottom_frame, text='Hint', font="Arial, 20", height=1, width=10,
                                                command=self.hint)

        self.back_button.pack(padx=10, pady=300, side=tkinter.LEFT)

        # pack the frames

        self.top_frame.pack()
        self.play_frame.pack()
        self.bottom_frame.pack()

    # Exit
    def exit(self):
        self.play_window.destroy()

    # Load level themes
    def play_level2(self):
        self.level_themes.clear()
        theme1 = GameClass.Game("City: ", "7 letters", "CHICAGO")
        theme2 = GameClass.Game("Italian food: ", "5 letters", "PIZZA")
        theme3 = GameClass.Game("Greek God: ", "4 letters", "ZEUS")
        theme4 = GameClass.Game("US State:", "8 letters", "ILLINOIS")
        self.level_themes = [theme1, theme2, theme3, theme4]
        self.theme_index.set(0)
        self.current_theme.set(self.level_themes[0].get_question())
        self.level1_button.pack_forget()
        self.level_theme.pack(side=tkinter.TOP, pady=10)
        self.level_enter_button.pack(side=tkinter.BOTTOM, pady=10)
        self.level_guess.pack(pady=10)
        self.level2_button.pack_forget()
        self.current_score_label.set("")

    # Load level themes

    def play_level1(self):

        theme1 = GameClass.Game("Class Subject: ", "4 letters", "MATH")
        theme2 = GameClass.Game("Sports: ", "6 Letters", "SOCCER")
        theme3 = GameClass.Game("Soda: ", "5 letters", "PEPSI")
        theme4 = GameClass.Game("Coding Language: ", "6 letters", "PYTHON")
        self.level_themes = []
        self.level_themes = [theme1, theme2, theme3, theme4]
        self.theme_index.set(0)
        self.current_theme.set(self.level_themes[0].get_question())
        self.level1_button.pack_forget()
        self.level_enter_button.pack(side=tkinter.BOTTOM, pady=10)
        self.level_guess.pack(pady=10)
        self.level_hint_button.pack(padx=100, pady=300, side=tkinter.RIGHT)

    def add_user(self):
        filename = "top-score_list.dat"
        try:
            input_file = open(filename, 'rb')
            self.top_score = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.top_score = []
        name = self.level_guess.get("1.0", 'end-1c')
        self.top_score.append(name)
        input_file=open(filename,'wb')
        pickle.dump(self.top_score,input_file)
        input_file.close()
        self.exit()


    def evaluate(self):
        if self.Add_to_leaderboard.get():
            self.add_user()


        if self.level_guess.get("1.0", 'end-1c').upper() == self.level_themes[self.theme_index.get()].get_solution():
            self.current_score.set(self.current_score.get() + 3)
            # print(self.level_guess.get("1.0", 'end-1c'))
        else:
            self.current_score.set(self.current_score.get() - 3)
        self.current_score_label.set("Your score is: " + str(self.current_score.get()))

        self.hint_label.pack_forget()
        self.level_guess.delete("1.0", "end")
        if self.theme_index.get() + 1 < 4:
            self.theme_index.set(self.theme_index.get() + 1)
            self.current_theme.set(self.level_themes[self.theme_index.get()].get_question())

        else:
            self.level_enter_button.pack_forget()
            self.level_guess.pack_forget()
            self.level_hint_button.pack_forget()

            if self.current_score.get() == 12:
                self.level2_button.pack(side='right', padx=400)
                self.current_score_label.set("Congratulations, you passed level 1 and now you can play the BOSS level")
                self.level_theme.pack_forget()
            elif self.current_score.get() >= 24:
                self.level2_button.pack(side='right', padx=400)
                self.current_score_label.set("Congratulations, you have complete the Wordle game!")
                self.level2_button.pack_forget()
                #Now need to ask the user for their name and record
                self.current_theme.set("Please enter your name to be added to the leaderboard")
                self.Add_to_leaderboard.set(1)
                self.level_guess.pack(pady=10)
                self.level_enter_button.pack(side=tkinter.BOTTOM)


            # end of level 1
            #

    def hint(self):
        self.hint_answer.set(self.level_themes[self.theme_index.get()].get_hint())
        self.hint_label.pack()


def main():
    root = tkinter.Tk()
    _ = Game(root)
    root.mainloop()


main()
