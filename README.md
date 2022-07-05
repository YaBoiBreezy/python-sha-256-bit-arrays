# SHA-256 in python with arrays of ints

SHA-256 implemented in python using arrays of integers representing individual bits [1,0,0,1,1,0,0,0]<br/>
When implemented with bitwise operations, SHA-256 is difficult to visualize and alter <br/>
The purpose of this project was to implement SHA-256 in a way that allows people to actually interact with it <br/>
This project uses an integer in an array for each individual bit, allowing all the data and logic to be clearly seen

## Getting Started
There are 3 files:<br/>
<ul>
<li>
SHA-256.py takes a formatted input (array of length 512, containing only 1 and 0), which should be sufficient for cryptocurrency applications.</li>
<li>SHA-256-LARGE.py takes a string input and runs a compression loop on it before parsing, like normal SHA-256.</li>
<li>SHA-256-PROBABILITIES.py is like SHA-256.py, but runs probabilistically, so bits can have partial values such as 0.67, aka "67% chance of being 1". Sadly its intended purpose (a method of breaking SHA-256 by predicting hashes to efficiently search inputs and tend towards a collision) doesn't work, so it is effectively just a slightly slower version of SHA-256.py</li>

### Prerequisites

There are no dependencies. It works on windows.<br/>

## Built With

notepad and powershell 😎 <br/>
I'm not kidding. Thanks university for teaching me good habits

## Contributing

It's basically done, if you want to help feel free to push whatever

## Authors

* **Alexander Breeze** - *Everything* - [YaBoiBreezy](https://github.com/YaBoiBreezy)

## License

Anyone can use it

## Acknowledgments

Big thanks to this blog for giving a step by step walkthrough, troubleshooting would have been even more horrible without it: <br/>
https://blog.boot.dev/cryptography/how-sha-2-works-step-by-step-sha-256/
