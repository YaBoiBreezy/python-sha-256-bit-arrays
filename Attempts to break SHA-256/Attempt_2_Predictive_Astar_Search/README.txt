SHA-256-PROBABILITIES:
SHA-256 basic, last 3 operation functions altered to handle probabilities instead of binaries (0.56=56% chance of being 1, 44% change of being 0)
Main function generates diff of [0.5,...,0.5] arr with bit x being 0 and 1 respectively, then saves to json file
Also has code for changing 2, 3 bits at a time. JSON file not included due to size.
For use, run SHA-256-PROBABILISTIC, then AstarProbabilisticL1 or L1Stats. Alternatively, uncomment the 2 part (NOT THE 3 PART) in main, lines 227-251, then you can run the L2 script after a couple hours
WARNING: 2 bits takes 2 hours to run, 3 bits takes 30 days

The resulting JSON is used by the other scripts

A* search for SHA-256, but instead of hashing for all 512 or 512^2 possible bitflips, uses
pregenerated expected result (see SHA-256-PROBABILITIES), then ranks based on that.
This lets it has once per generation, not 512 or 512^2 times.

These A* searches weren't performing well, so L1Stats tracks their progress. 
As can be seen from running this program (Basically L1 with extra data logging),
The average searched value "newVal" has score 128, aka exactly 50%, aka equal to 
random guessing, despite the expected average (based on the predictive data) being 153. 
This proves my entire method is faulty. Again. Sad