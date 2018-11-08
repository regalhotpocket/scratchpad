#- Let's say I offer to play a game with you, where you take an unbiased coin, flip it a thousand times, then we take the number of heads (H) and subtract it from the number of tails (T), and I pay you $|(H-T)|. So if there are 520 heads and 480 tails, I'll owe you $40, but if it were reversed, you'd owe me nothing. How much would you be willing to pay to play this game with me, i.e. what’s the expected value of this game?
# formal simulation O(flips * tries)
#
# https://news.ycombinator.com/item?id=18361299
#
from random import randint, randrange
  
numDraws = 1000
numFlips = 1000
totalPayoff = 0
for i in range(numDraws):
    totalPayoff += abs(sum(pow(-1, randint(0,1)) for _ in range(numFlips)))

print('$' + str(round(totalPayoff / numDraws, 2))) # around $2

#Monty Carlo Markov Chain O(numSteps)
numSteps = 1000 * 30
numFlips = 1000
totalPayoff = 0

coins = [pow(-1, randint(0,1)) for x in range(numFlips)]
currentTotal = sum(coins)
totalPayoff = 0
for i in range(numSteps):
    coinToFlip = randrange(numFlips)
    coins[coinToFlip] *= -1
    currentTotal += 2 if (coins[coinToFlip] is 1) else -2
    totalPayoff += abs(currentTotal)

print('$' + str(round(totalPayoff / numSteps, 2))) # Also ~$24