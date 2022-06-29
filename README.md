# python SHA256 with arrays of ints

SHA-256 implemented in python using arrays of integers representing individual bits <br/>
The purpose of this project is to implement SHA-256 in a way that allows people to actually interact with it <br/>
When implemented with bitwise operations it is difficult to visualize and alter <br/>
This project uses an integer in an array for each individual bit, allowing all the data and logic to be clearly seen

## Getting Started

There are 2 files:<br/>
SHA-256.py takes a formatted input (array of length 512, containing only 1 and 0), which should be sufficient for cryptocurrency applications.<br/>
SHA-256-LARGE.py takes a string input and runs a compression loop on it like normal SHA256.

### Prerequisites

There are no dependencies. It works on windows.<br/>

## Built With

notepad and powershell

## Contributing

It's basically done, if you want to help feel free to do whatever

## Authors

* **Alexander Breeze** - *Everything* - [YaBoiBreezy](https://github.com/YaBoiBreezy)

## License

Anyone can use it

## Acknowledgments

Big thanks to this blog for giving a setp by step runthrough, troubleshooting would have been even more horrible without it
https://blog.boot.dev/cryptography/how-sha-2-works-step-by-step-sha-256/
