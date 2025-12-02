## Shut the Box

Use scissors to cut away one or more **orthogonally connected** groups of cells (squares) from the grid above.  
Each removed group must have **at least one cell touching the outer boundary** of the grid.  
The **remaining cells** must be orthogonally connected and contain **no holes**.

It must be possible to **fold along grid lines** so that the remaining cells form the **six walls of a rectangular solid** (the “box”).  
No cells may overlap when the box is assembled.

### Special Cell Types

- **Arrow cells**  
  These cells are *not* part of the box. Each arrow points toward the nearest box cell(s) in that arrow’s row or column.

- **Numbered cells**  
  These *are* part of the box.  
  A number tells you how many cells **within one king’s move** (including diagonals, and including itself) are part of the box.

### Additional Constraints

- Each **grey circle** must be directly *opposite* another grey circle when the box is assembled.  
- Each **grey square** must be **orthogonally adjacent** to another grey square *on the same face*.

### Final Step

Once the box is assembled, compute **on each face** the sum of its numbered cells.  
The **answer to the puzzle** is the **product of the six face-sums**.
