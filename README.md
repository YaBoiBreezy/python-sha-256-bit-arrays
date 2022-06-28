# python-sha-256-bit-arrays
SHA-256 implemented in python using arrays of integers representing individual bits
The purpose of this project is to implement SHA-256 in a way that allows people to actually interact with it. When implemented with bitwise operations it is difficult to visualize and alter. This project uses an integer in an array for each individual bit.

I intend to use it to calculate probabilities of an end bit being changed given an input bit being changed, in terms of an actual value (e.g. 0.42). This cannot be done when you are using individual bits (0|1). I couldn't find any such project, so I am making one here.
