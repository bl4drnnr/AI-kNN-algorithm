# AI-kNN-algorithm

### Toolbox

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### Description
Implementation of kNN algorithm.

### Status

11.05.2022
- Basic working version.

### Analysis of an unknown object using the kNN method

- all distances between the classified (unknown) object and all known objects from the training set should be determined. By distance, we understand the distance between the points `X (x1, x2 ... xn)` and `Z (z1, z2 ... zn)` representing objects in `n`-multidimensional space, which can be defined by the formulas presented in Chap. 3

- rank the cases from the training set according to the calculated value of the distance to the unknown object, in the order from the smallest to the largest

- choose a certain number of `k` (the number `k` is an odd integer) of the objects closest to the unknown case

- assign to the unknown object the class that is most frequently represented among the `k` nearest neighbors using a vote

### Example of working

All you need to do is just put your JSON data in `inputdata` in `input.json` file.

There is only **one** condition for the correct operation of the algorithm.

- Decision parameter needs to be placed on last place of every input record in `JSON`.

As a result you will get **9** tables - for **3** metrics - `Euklid`, `City block` and `Minkowski`, and for 3 types of elections - `Normal elections`, `Summary distance elections` and `Summary of reciprocal squares`

**3** columns if for **3** `n` nearest neighbors.
```
Type of metric: Euklid
Election method: Normal elections
n = 1		n = 3		n = 5
1			1			1
1			1			1
1			1			1
1			1			1
1			1			1
0			0			0
1			1			1
1			1			1
1			1			1
0			0			0
80.0			80.0			80.0	    
```
