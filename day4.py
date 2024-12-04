with open('day4.txt', 'r') as file:
    grid = [list(line.strip()) for line in file]

rows, cols = len(grid), len(grid[0])
directions = [
    (0, 1),  # Right
    (0, -1),  # Left
    (1, 0),  # Down
    (-1, 0),  # Up
    (1, 1),  # Down-Right
    (1, -1),  # Down-Left
    (-1, 1),  # Up-Right
    (-1, -1)  # Up-Left
]

def search_word(x, y, word, direction):
    dx, dy = direction
    return all(
        0 <= (nx := x + i * dx) < rows and
        0 <= (ny := y + i * dy) < cols and
        grid[nx][ny] == char
        for i, char in enumerate(word)
    )

count = sum(
    search_word(x, y, 'XMAS', direction)
    for x in range(rows)
    for y in range(cols)
    if grid[x][y] == 'X'
    for direction in directions
)

print('XMAS:', count)

diagonal_offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

def search_x_shape(x, y):
    if grid[x][y] != 'A':
        return False

    valid_patterns = {
        ('M', 'M', 'S', 'S'),
        ('M', 'S', 'M', 'S'),
        ('S', 'M', 'S', 'M'),
        ('S', 'S', 'M', 'M')
    }

    diagonal_chars = [
        grid[x + dx][y + dy]
        for dx, dy in diagonal_offsets
    ]

    return tuple(diagonal_chars) in valid_patterns

count = sum(
    search_x_shape(x, y)
    for x in range(1, rows - 1)
    for y in range(1, cols - 1)
)

print('X-MAS:', count)