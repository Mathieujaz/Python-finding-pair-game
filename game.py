#to run the program write: python game.py  <grid size>  in the terminal

import sys
from grid import Grid

def play_game(grid_size):
    game_grid = Grid(grid_size)
    while True:
        game_grid.display()
        choice = input("Select: ").strip()
        
        if choice == '1':
            cell1 = input("Enter cell coordinates (e.g., a0): ").upper()
            cell2 = input("Enter cell coordinates (e.g., b1): ").upper()
            if game_grid.select_elements(cell1, cell2):
                if not game_grid.play_again():
                    break
        elif choice == '2':
            cell = input("Enter cell coordinates (e.g., a0): ").upper()
            if game_grid.uncover_element(cell):
                if not game_grid.play_again():
                    break
        elif choice == '3':
            game_grid.reveal_grid()
            print("Game over. Would you like to play again?")
            if not game_grid.play_again(): 
                break
        elif choice == '4':
            game_grid.initialize_grid()
        elif choice == '5':
            print("Thank you for playing. Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ('2', '4', '6'):
        print("Usage: python game.py <grid_size>")
        print("The grid_size must be 2, 4, or 6.")
    else:
        grid_size = int(sys.argv[1])
        play_game(grid_size)
