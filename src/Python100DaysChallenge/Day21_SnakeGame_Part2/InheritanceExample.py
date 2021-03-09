class Father:
    def __init__(self):
        self.num_of_sons = 4

    def learnt_vedas(self):
        print("Yes he learnt Vedas")


class Child(Father):
    def __init__(self):
        super().__init__()

    def learnt_vedas(self):
        super().learnt_vedas()
        print("Learnt Smartha also")

    def learnt_computer(self):
        print("Yes he learnt Computers")

child = Child()

child.learnt_vedas()