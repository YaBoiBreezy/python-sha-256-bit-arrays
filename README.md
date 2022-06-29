# python-sha-256-bit-arrays

SHA-256 implemented in python using arrays of integers representing individual bits
The purpose of this project is to implement SHA-256 in a way that allows people to actually interact with it. When implemented with bitwise operations it is difficult to visualize and alter. This project uses an integer in an array for each individual bit, allowing all the data and logic to be clearly seen.

There are 2 files:
SHA-256.py takes a formatted input (array of length 512, containing only 1 and 0), which should be sufficient for cryptocurrency applications.
SHA-256-LARGE.py takes a string input and runs a compression loop on it like normal SHA256.
