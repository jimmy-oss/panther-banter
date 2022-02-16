class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Panther Banter")
        self.window.geometry("850x530")
        # self.window.configure(bg='blue')
        self.window['background']='#FAD586'