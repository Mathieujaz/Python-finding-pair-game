# To run the program, write: python game.py <grid size> in the terminal

import os
import random
import time

class Grid:
    def __init__(self, grid_size=4):
        self.grid_size = grid_size
        self.pair_count = (grid_size ** 2) // 2
        self.grid = {}
        self.hidden_grid = {}
        self.guess = 0
        self.pairs_found = 0
        self.Uncover_count = 0
        self.cheat = False  
        self.initialize_grid()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def initialize_grid(self):
        numbers = list(range(self.pair_count)) * 2
        random.shuffle(numbers)
        self.hidden_grid = {f"{chr(65 + col)}{row}": numbers.pop() 
                            for row in range(self.grid_size) 
                            for col in range(self.grid_size)}
        self.grid = {key: 'X' for key in self.hidden_grid}
        self.guess = 0
        self.pairs_found = 0
        self.Uncover_count = 0
        self.cheat = False  

    def display(self):
        self.clear_screen()
        print("----------------------")
        print("|    Brain Buster    |")
        print("----------------------")

        header = " ".join([f"[{chr(65 + i)}]" for i in range(self.grid_size)])
        print(f"\n       {header}")
        
        for row in range(self.grid_size):
            row_display = f"[{row}]   "
            for column in range(self.grid_size):
                cell = f"{chr(65 + column)}{row}"
                row_display += f" {self.grid[cell]:^4}" 
            print(row_display)
        print("\n1. Let me select two elements")
        print("2. Uncover one element for me")
        print("3. I give up - reveal the grid")
        print("4. New game")
        print("5. Exit")

    def reveal_grid(self):
        for key in self.hidden_grid:
            self.grid[key] = self.hidden_grid[key]
        self.display()

    def calculate_score(self):
        min_guesses = self.pair_count
        if self.guess == 0:
            return 0
        score = (min_guesses / self.guess) * 100
        return max(score, 0)

    def select_elements(self, cell1, cell2):
        if cell1 == cell2 or cell1 not in self.grid or cell2 not in self.grid:
            print("You chose the same coordinates twice. Try again.")
            return False

        self.grid[cell1] = self.hidden_grid[cell1]
        self.grid[cell2] = self.hidden_grid[cell2]
        self.display()
        time.sleep(2)
        self.guess += 1

        if self.hidden_grid[cell1] == self.hidden_grid[cell2]:
            self.pairs_found += 1
            print("The numbers are the same. Well done!")
        else:
            print("The numbers are not the same.")
            self.grid[cell1], self.grid[cell2] = 'X', 'X'

        if self.pairs_found == self.pair_count:
            score = self.calculate_score()
            print(f"Oh Happy Day. You've won!! Your score is: {score:.2f}")
            return True
        return False

    def uncover_element(self, cell):
        if cell in self.grid and self.grid[cell] == 'X':
            self.grid[cell] = self.hidden_grid[cell]
            self.display()
            self.guess += 2
            self.Uncover_count += 1

            if self.Uncover_count == self.grid_size * self.grid_size:
                print("You cheated - Loser! Your score is 0!")
                self.cheat = True 
                return True  
        else:
            print("Invalid choice. Try again.")
        return False
    
    def play_again(self):
        if not self.cheat and self.pairs_found < self.pair_count:
            self.reveal_grid()
            print("Game over. You did not win.")

        choice = input("Do you want to play again? (y/n): ").strip().lower()
        if choice == 'y':
            self.initialize_grid()
            return True
        else:
            print("Thank you for playing. Goodbye.")
            self.clear_screen()
            return False
