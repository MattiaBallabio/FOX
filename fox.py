import random as r

class fox:
    def __init__(self, columns, rows):
        self.columns = int(columns)
        self.rows = int(rows)
        self.results = ""
        self.rowList = []
        self.letters = ["F", "O", "X"]
    
    def nextLetter(self, row):
        for i in range(self.columns):
            #Use row and column index with random choice to vary letters
            if (row + i) % 2 == 0:
                self.rowList.append(r.choice(["F", "O"]))
            elif (row + i) % 3 == 0:
                self.rowList.append(r.choice(["O", "X"]))
            else:
                self.rowList.append(r.choice(["F", "X"]))

    def showResults(self):
        for row in range(self.rows):
            self.rowList.clear()
            self.nextLetter(row)

            self.results += ''.join(self.rowList) + "\n"

        return self.results