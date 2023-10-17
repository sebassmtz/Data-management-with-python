#create an array numpy 2D 6x6 with borders of 1 and 0 inside.
#111111
#100001
#100001
#100001
#100001
#111111

import numpy as np

# Create a 6x6 array filled with ones
arr = np.ones((6, 6), dtype=int)

# Set the borders (excluding corners) to zero
arr[1:-1, 1] = 0  # Left border
arr[1:-1, -2] = 0  # Right border
arr[1, 1:-1] = 0  # Top border
arr[-2, 1:-1] = 0  # Bottom border

# Print the resulting array
for row in arr:
    print(''.join(map(str, row)))

# To display the entire array
print("\nFull 2D array:")
print(arr)