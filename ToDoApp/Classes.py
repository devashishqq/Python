class Todo:
    def __init__(self, name):
        self.name = name
        print(self.name)
        self.d = {}

    def create(self, sno, note, time):
        self.d[int(sno)] = [note, time]
        for key,values in self.d.items():
            print(f"{key}: {values[0]} at {values[1]}")

    def delete(self, sno):
        self.d.pop(int(sno), None)
        print(self.d)

    def showtodo(self):
        for key, value in self.d.items():
            print(key, value[0], value[1])