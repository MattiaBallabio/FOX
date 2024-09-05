import tkinter as tk
from fox import fox

#Set up window
root = tk.Tk()
root.title("Find the word \"FOX\"")
root.geometry("400x300")

columnsLabel = tk.Label(root, font=("Helvetica", 14), text="Columns")
columnsLabel.place(relx=0.16, rely=0.6, anchor="s")
columnsEntry = tk.Entry(root, font=("Helvetica", 14))
columnsEntry.place(relx=0.35, rely=0.7, anchor="s")

rowsLabel = tk.Label(root, font=("Helvetica", 14), text="Rows")
rowsLabel.place(relx=0.13, rely=0.8, anchor="s")
rowsEntry = tk.Entry(root, font=("Helvetica", 14))
rowsEntry.place(relx=0.35, rely=0.9, anchor="s")

resultsLabel = tk.Label(root, font=("Helvetica", 14))

#Activates when user clicks submit
def get_input():
    columns = columnsEntry.get()
    rows = rowsEntry.get()

    #Removing everything on screen
    columnsLabel.place_forget()
    columnsEntry.place_forget()
    rowsLabel.place_forget()
    rowsEntry.place_forget()
    submit_button.place_forget()

    print(columns, rows)
    word_finder = fox(columns, rows)
    word_finder.showResults()
    resultsLabel.place(relx=0.5, rely=0.5, anchor="center")
    results = word_finder.showResults()
    print(results)
    resultsLabel.config(text=results)
    

submit_button = tk.Button(root, text="Submit", command=get_input, font=("Helvetica", 14))
submit_button.place(relx=0.9, rely=.9, anchor="se")


root.mainloop()