file = open("11.txt","r")
length = sum(1 for line in file)
file.seek(0)
grid = []
maxValues = []
for i in range(length):
    grid.append(file.readline().strip().split())

horizontal_max_product = max(int(grid[i][j])*int(grid[i][j+1])*int(grid[i][j+2])*int(grid[i][j+3]) for i in range(20) for j in range(17))
vertical_max_product = max(int(grid[i][j])*int(grid[i+1][j])*int(grid[i+2][j])*int(grid[i+3][j]) for i in range(17) for j in range(20))
diagonal1_max_product = max(int(grid[i][j])*int(grid[i+1][j+1])*int(grid[i+2][j+2])*int(grid[i+3][j+3]) for i in range(17) for j in range(17))
diagonal2_max_product = max(int(grid[i][j])*int(grid[i-1][j+1])*int(grid[i-2][j+2])*int(grid[i-3][j+3]) for i in range(3,20) for j in range(17))
max_of_products = max(horizontal_max_product, vertical_max_product, diagonal1_max_product, diagonal2_max_product)
print(max_of_products)
