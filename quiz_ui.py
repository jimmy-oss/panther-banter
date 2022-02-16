class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Panther Banter")
        self.window.geometry("850x530")
        # self.window.configure(bg='blue')
        self.window['background']='#FAD586'

    
        # Display Title
        self.display_title()

        # Create a canvas for question text, and dsiplay question
        self.canvas = Canvas(width=1300, height=1300,bg="#FAD586")
        self.question_text = self.canvas.create_text(400, 125,
                                                     text="Question here",
                                                     width=680,
                                                     fill=THEME_COLOR,
                                                     font=(
                                                         'acme', 15, 'italic')
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        # Declare a StringVar to store user's answer
        self.user_answer = StringVar()

        # Display four options (radio buttons)
        self.opts = self.radio_buttons()
        self.display_options()

        # To show whether the answer is right or wrong
        self.feedback = Label(self.window, pady=10, font=("Acme", 15, "bold"))
        self.feedback.place(x=300, y=380)