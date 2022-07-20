This attempt was using a search algorithm with a probabilistic SHA-256 algorithm, allowing it to change less than 1 bit at a time (e.g. change 1 to 0.98 instead of 0)
Sadly it didn't work, as repeated probabilistic and/xor/plus (plus especially) tended the values to 0.5, so by round 6/64 no algorithm could do better than 128/256 because every input resulted in [0.5, 0.5, 0.5, ...]
I think I might give up now, I gave it my best shot and am out of ideas. Also this is almost def. impossible, so I'm wasting my time.
