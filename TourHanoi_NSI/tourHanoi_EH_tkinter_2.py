import tkinter as tk


class TowerOfHanoi:
    def _init_(self, num_disks, root):
        self.num_disks = num_disks
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        # Create the buttons
        self.start_button = tk.Button(
            root, text='Start', command=self.start_game)
        self.start_button.pack()

        self.reset_button = tk.Button(
            root, text='Reset', command=self.reset_game)
        self.reset_button.pack()

        # Create the counter
        self.counter = tk.Label(root, text='Moves: 0')
        self.counter.pack()

        self.peg1 = []
        self.peg2 = []
        self.peg3 = []

        # Create the disks and place them on peg1
        for i in range(num_disks, 0, -1):
            disk = self.canvas.create_rectangle(
                50*i, 50, 50*(i+1), 40, fill='red')
            self.peg1.append(disk)

        # Draw the pegs
        self.canvas.create_rectangle(80, 300, 120, 50, fill='grey')
        self.canvas.create_line(100, 300, 100, 0, fill='black', width=5)
        self.canvas.create_rectangle(180, 300, 220, 50, fill='grey')
        self.canvas.create_line(200, 300, 200, 0, fill='black', width=5)
        self.canvas.create_rectangle(280, 300, 320, 50, fill='grey')
        self.canvas.create_line(300, 300, 300, 0, fill='black', width=5)

    def start_game(self):
        # Reset the counter
        self.counter['text'] = 'Moves: 0'

        # Start the game by moving the disks from peg1 to peg3
        self.move_disk(self.num_disks, 1, 3, 2)

    def reset_game(self):
        # Reset the game by moving all the disks back to peg1
        self.move_disk(self.num_disks, 3, 1, 2)

        # Reset the counter
        self.counter['text'] = 'Moves: 0'

    def move_disk(self, n, from_peg, to_peg, aux_peg):
        if n == 0:
            return

        if n == 1:
            # Move the top disk from the from_peg to the to_peg
            disk = self.peg1.pop() if from_peg == 1 else self.peg2.pop(
            ) if from_peg == 2 else self.peg3.pop()
            if to_peg == 1:
                self.peg1.pop()


root = tk.Tk()
num_disks = 3
root.mainloop()
