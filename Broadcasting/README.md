## Project 3: NumPy Broadcasting Lab
In this project, I mastered the concept of **Broadcasting**, which is 
NumPy's ability to perform arithmetic on arrays with different shapes. 
This is a critical skill for scaling data efficiently without using manual 
loops.

### Key Concepts Applied:
- **Vector Stretching:** Understanding how NumPy "stretches" dimensions of 
size 1 to match larger arrays.
- **Matrix Generation:** Creating a 10x10 multiplication table by 
broadcasting a column vector `(10, 1)` against a row vector `(1, 10)`.
- **Dimension Manipulation:** Using `.reshape()` to explicitly define 
array geometry for broadcasting.
- **Practical Application:** Adjusting a multi-camera security feed `(3, 
4)` using a specific sensitivity vector `(3, 1)`.

### Why it Matters:
Broadcasting allows for cleaner, faster code that uses less memory. 
Instead of creating a massive 3x4 array of sensitivities, I used a single 
3x1 column, letting NumPy handle the heavy lifting internally.
