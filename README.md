# Reduction function analysis

## Description reduction function:
* Xorshit
```
> Dividing the 64 bits hash into 4 15 bits parts
> The remaining bits (+ the step) is xored with the fourth hash part 
> (XorShift on the 4 parts) % Possibilities
```
* End Hash
```
> Keeping only the last 15 bits of the hash
> 15 bits hash(+ step) % Possibilities
```
* CharInHash
```
> take the n char of the hash xor it with the step and add the n+11 char in hash
>  % len charset
```
The purpose of this analysis is to find the most efficient reduction function (unique passwords created/ time). And also to find the optimal length of the rainbow table.

## Best reduction function:
To find the best reduction function, we can prioritise 2 variables:
* Low collisions rate
* Low execution time

Based on those 2 variables we can create this plot.

![plot](/uniquePasswords_time.png)

The EndHash reduction seems to have the same number of unique passwords generated than the XorShift reduction but take less time to generate.

Even if the charInHash reduction is the fastest one, the collisions rate make this reduction function pointless to use.

## Achieving 50% of cracked passwords

In order to find the number of possibilities needed by the rainbow table to achieve cracking half of passwords on average, a sample of 100 000 random passwords was used.

![plot](/percentagePasswordsCracked_Coverage.png)

As we can see, to achieve craking half the passwords in entry on average, a rainbow table have to contains half of the possibilities.

## Finding the best length for the Rainbow table
We need to crack half the rainbow table.

For a 4 char passwords, P = 62^4 =  14.776.336 possible passwords.
To achieve to crack 50% of passwords on average, the RT needs to contain P/2 unique passwords. 
![plot](/uniquePasswords_totalPasswords.png)
To get 7.3M unique passwords, we need to generate 1.1M passwords.
The more passwords in the RT, the higher the chance of collisions for the next passwords generated.

### Minimizing the number of collisions in the RT
2 ways possibles:
* Finding a better reduction function

One of the flaw of those reduction function comes from the fact that if the 2 same passwords occurs on the same column, all the next passwords on those lines will be the same. Changing it can be easy, adding a variable for the line. By doing this, we decrease the number of collisions by 10% for a complete table. Unfortunately, this will make the complexity of the search far too high to be used.

The only possibility is to have a better reduction function (better entropy ?, better distribution ?).
That was the purpose of the Xorshift reduction function, more operation on the hash, using all the bits of it but as we can see the collisions rate from the endHash function and the XorShift one is almost the same. I think that this collisions rate come from the modulo and it will be very difficult to get better results.

* Aiming for less cracking in average

The collisions rate seems to be exponential after generating 0.7*P. One way to limit the RT size is to generate around 0.65P. This will not lead to a 50% cracked password on average, but it will be close enough.

![plot](/collisionsrate_lengthRt.png)