from random import random
trials = 10000
gain = 0
for i in range(trials):
    gain += 20 if random() >= 0.5 else 5
print(gain/trials)