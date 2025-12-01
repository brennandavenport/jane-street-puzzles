from typing import List, Tuple
from itertools import permutations


def _is_valid(i, j, k, valid_dims):
    perm = permutations([i, j, k])
    return not any((a, b, c) in valid_dims for a, b, c in perm)


def generate(max_width: int, max_length: int, max_height: int, surface_area: int) -> List[Tuple[int]]:
    valid_dims = set()
    for i in range(1, max_width):
        for j in range(1, max_length):
            for k in range(1, max_height):
                # SA = 2(wl + lh + wh)
                if (
                    surface_area == 2 * i * j + 2 * j * k + 2 * i * k
                    and _is_valid(i, j, k, valid_dims)
                ):
                    valid_dims.add((i, j, k))

    return list(valid_dims)

def main():
    valid_dimensions = generate(max_width=140, max_length=140, max_height=140, surface_area=132)

    # clean tuple(int) -> string
    valid_dimensions = sorted([f"{width}, {length}, {height}" for width, length, height in valid_dimensions])

    try:
        with open("output.txt", "w") as fptr:
            for line in valid_dimensions:
                fptr.write(line)
                fptr.write("\n")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()