import tkinter as tk


class TowerOfHanoi:
    def _init_(self, num_disks, root):
        self.num_disks = num_disks
        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack()

        self.peg1 = []
        self.peg2 = []
        self.peg3 = []

        # Create the disks and place them on peg1
        for i in range(num_disks, 0, -1):
            disk = self.canvas.create_rectangle(
                50*i, 50, 50*(i+1), 40, fill='red')
            self.peg1.append(disk)

        # Draw the pegs
        self.canvas.create_line(100, 300, 100, 0, fill='black', width=5)
        self.canvas.create_line(200, 300, 200, 0, fill='black', width=5)
        self.canvas.create_line(300, 300, 300, 0, fill='black', width=5)

        self.move_disk(self.num_disks, 1, 3, 2)

    def move_disk(self, n, from_peg, to_peg, aux_peg):
        if n == 1:
            # Move the top disk from the from_peg to the to_peg
            disk = self.peg1.pop() if from_peg == 1 else self.peg2.pop(
            ) if from_peg == 2 else self.peg3.pop()
            if to_peg == 1:
                self.peg1.append(disk)
            elif to_peg == 2:
                self.peg2.append(disk)
            else:
                self.peg3.append(disk)
            self.canvas.move(disk, (to_peg-1)*100, 0)
        else:
            self.move_disk(n-1, from_peg, aux_peg, to_peg)
            self.move_disk(1, from_peg, to_peg, aux_peg)
            self.move_disk(n-1, aux_peg, to_peg, from_peg)


root = tk.Tk()
move_disk(3, root)
root.mainloop()
