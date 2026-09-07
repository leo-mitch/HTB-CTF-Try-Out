import numpy as np
from pwn import *

# connect to the server, kinda like doing 'nc ip port'
host = '154.57.164.73'
port = 31102
r = remote(host, port)



def get_grid():
    grid_size = challenge_line.split() 
    numbers_str = r.recvuntil(b'\n').decode().split()
    grid = np.array(numbers_str, dtype=int).reshape(-1, int(grid_size[1])).tolist()
    print(f"Grid: {grid}")
    return grid

def min_path_sum(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    dp = [0] * cols
    dp[0] = grid[0][0]

    for j in range(1, cols):
        dp[j] = dp[j - 1] + grid[0][j]

    for i in range(1, rows):
        dp[0] += grid[i][0]

        for j in range(1, cols):
            dp[j] = grid[i][j] + min(dp[j], dp[j - 1])

    print(f"Min path Sum: {dp[-1]}")
    return dp[-1]


#grid = str(get_grid())

for i in range(1, 101):

    prompt = r.recvuntil(b'/100\n')
    print(prompt.decode())


    challenge_line = r.recvline().decode().strip()
    print(f"Challenge received: {challenge_line}")
    result = str(min_path_sum(get_grid()))
    r.sendline(result.encode())
    
print(r.recvall().decode())


