class ToDo:
    def __init__(self):
        pass

    def create(self, note, time):
        self.note = note
        self.time = time
        l = []
        l.append(self.note)
        l.append(self.time)
        print(l)