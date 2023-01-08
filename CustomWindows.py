from interfaces import Window
import tkinter as tk


class ChangeWindow(Window):

    def init_window(self):
        # Что-то взятое с интеренто, но работающее. Мб поменяю потом
        self.title("Ввод матрицы")
        self.geometry("650x500+120+120")
        self.configure(bg='bisque2')
        self.resizable(False, False)

        text_var = []
        entries = []

        # callback function to get your StringVars
        def get_mat():
            matrix = []
            for row in range(rows):
                matrix.append([])
                for col in range(cols):
                    matrix[row].append(text_var[row][col].get())
            self._window_subject.matrix = matrix

        tk.Label(self, text="Ввод матрицы :", font=('arial', 10, 'bold'),
                 bg="bisque2").place(x=20, y=20)

        x2 = 0
        y2 = 0
        rows, cols = (5, 5)
        for i in range(rows):
            # append an empty list to your two arrays
            # so you can append to those later
            text_var.append([])
            entries.append([])
            for j in range(cols):
                # append your StringVar and Entry
                text_var[i].append(tk.StringVar())
                entries[i].append(tk.Entry(self, textvariable=text_var[i][j], width=3))
                entries[i][j].place(x=60 + x2, y=50 + y2)
                x2 += 30

            y2 += 30
            x2 = 0
        button = tk.Button(self, text="Сохранить", bg='bisque3', width=15, command=get_mat)
        button.pack(side='bottom')
        
    def update(self) -> None:
        pass


class ShowMatrixWindow(Window):
    matrix: list

    def init_window(self) -> None:
        self.matrix = self._window_subject.matrix
        self.title("Релузьтат")
        self.geometry("650x500+120+120")
        self.configure(bg='bisque2')
        self.resizable(False, False)
        for i in range(5):
            for j in range(5):
                self.e = tk.Entry(self, width=3)
                self.e.grid(row=i, column=j)
                self.e.insert(tk.END, self.matrix[i][j])

    def update(self) -> None:
        pass
