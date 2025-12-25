# ️ NumPy Project: 2D Data Slicing & Trimming

## Overview
In this project, I demonstrate how to efficiently "trim" a dataset using 
NumPy slicing. I simulated a surveillance system where each row represents 
a camera and each column represents a time frame.

## The Logic: `[start : stop]`
The most important lesson learned here is the **Exclusive Stop Rule**:
- To grab columns 1, 2, and 3, I used the slice `1:4`. 
- Even though I wanted index 3, I had to stop at **4** because the stop 
index is not included.

## Data Operation
- **Input:** A `(4, 5)` matrix of sensor readings.
- **Action:** Extracted the middle 3 frames across all cameras using 
`floor_data[:, 1:4]`.
- **Output:** A compact `(4, 3)` matrix ready for analysis.

---
*Part of my journey to mastering NumPy multidimensional arrays.*
