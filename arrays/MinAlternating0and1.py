"""
Minimum number of flips to get alternating number of 0's and 1's

Eg [0, 1, 1, 1] returns 1 since the third value has to be flipped to give
[0, 1, 0, 1]
"""

"""
- i % 2 for i, n in enumerate(bits) and (i + 1) % 2 for i, n in enumerate(bits)
  gives the two alternating strings
- Checking for equality for each of the bits in the string with each bit in the
  alternating strings gives the number of differences
- The lowest number of differences with the two alternating strings gives the
  answer
  - For each index, the comparison gives True if a bit is in the correct
    position, and False if it is not
  - The sum of the booleans gives the total number of bits in the correct
    position (for each of the possible alternating sequences)
  - Returing the min of the sums therefore gives the number of bits in
    incorrect positions, which gives the answer
    - Eg [1, 1, 1, 0, 0, 0] has 4 bits in the correct position when compared
      with [1, 0, 1, 0, 1, 0] but only 2 bits in the correct position when
      compared with [0, 1, 0, 1, 0, 1]
      - If it has 2 bits in the correct position for the second possible
        correct sequence, then you must be able to flip two bits for it to
        match the first sequence (since the first and second possible
        alternating sequences are different in all six indexes)
"""
def min_flips(bits):
    return min(
        sum(n == i % 2 for i, n in enumerate(bits)),
        sum(n == (i + 1) % 2 for i, n in enumerate(bits))
    )


if __name__ == "__main__":
    print(min_flips([1, 1, 0, 1, 1]))
    print(min_flips([1, 1, 1, 0, 0, 0]))
