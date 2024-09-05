import random as r

class fox:
    def __init__(self, columns, rows):
        self.columns = int(columns)
        self.rows = int(rows)
        self.results = ""
        self.rowList = []
        self.letters = ["F", "O", "X"]
    
    def nextLetter(self):
        for i in range(self.columns):
            match i:
                case 0:
                    self.rowList.append(r.choice(self.letters))
                case _:
                    match self.rowList[i-1]:
                        case "F":
                            self.rowList.append(r.choice(["O", "X"]))
                        case "O":
                            self.rowList.append(r.choice(["F", "X"]))
                        case "X":
                            self.rowList.append(r.choice(["F", "O"]))

    def showResults(self):
        for x in range(self.rows):
            self.rowList.clear()
            self.nextLetter()

            for i in self.rowList:
                self.results += i
            self.results += "\n"

        return self.results