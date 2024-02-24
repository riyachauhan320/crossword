import random

def generate_crossword(words):
    # Create an empty grid
    grid = [[' ' for _ in range(10)] for _ in range(10)]
    
    # Place the words horizontally or vertically
    for word in words:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            x = random.randint(0, 10 - len(word))
            y = random.randint(0, 9)
            for i, letter in enumerate(word):
                grid[y][x + i] = letter
        else:
            x = random.randint(0, 9)
            y = random.randint(0, 10 - len(word))
            for i, letter in enumerate(word):
                grid[y + i][x] = letter
    
    # Fill the remaining empty spaces with random letters
    for i in range(10):
        for j in range(10):
            if grid[i][j] == ' ':
                grid[i][j] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    # Print the crossword puzzle
    for row in grid:
        print(' '.join(row))

# Take user input for words
num_words = int(input("Enter the number of words: "))
words = []
for i in range(num_words):
    word = input(f"Enter word {i+1}: ")
    words.append(word.upper())

# Generate the crossword puzzle
generate_crossword(words)