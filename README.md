# Voronoi Diagrams

This program creates a voronoi diagram from a given set of input sites in a bounded rectangle.

Currently, the algorithm implementation is the inefficient O(n^2) brute-force approach. Soon, I plan to implement fortune's algorithm. Unique to my implementation, however, is the ability to utilize an arbitrary distance metric. Specifically, the distance function is set up for the Minkowski p-metric.

Usage:
```
python voronoi.py
```

Running this program will output progress information (unless toggled off) and then automatically run the appropriate command to view the processed image.

N.B. This automatic command assumes "mpv" as a dependency, but can be easily altered to utilize whatever image viewer program is desired.

# Example 1 (p = 1)
![alt text](Images/1000x1000n20p1.png?raw=true)

# Example 2 (p = 2)
![alt text](Images/1000x1000n20p2.png?raw=true)

# Example 3 (p = 3)
![alt text](Images/1000x1000n20p3.png?raw=true)