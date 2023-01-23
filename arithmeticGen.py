from math import prod


def cumulative_freq(freq_dict):
  cumul_freq_dict = {}
  cumul_freq = 0
  for letter, frequency in freq_dict.items():
    cumul_freq_dict[letter] = cumul_freq
    cumul_freq += frequency
  return cumul_freq_dict

msg = input("Enter message: ")
message = "".join(sorted(list(msg)))

freq_dict = {}
for letter in msg:
  if letter not in freq_dict:
    freq_dict[letter] = 1
  else:
    freq_dict[letter] += 1


cumfreq = cumulative_freq(freq_dict)




def encodeGen(msg, cumfreq, freq_dict):
  radix = len(msg)
  power = len(msg)

  lowerbound = 0
  prevused = []

  for letter in msg:
    number = cumfreq[letter]
    numberfreq = freq_dict[letter]
    lowerbound += prod(prevused) * (number * (radix**(power - 1)))
    prevused.append(numberfreq)
    power -= 1

  upperbound = lowerbound + prod(prevused)

  lower = str(lowerbound)
  upper = str(upperbound)
  upperlist = list(upper)
  for i in range(len(upper)):
    if upper[i] != lower[i]:
      n = i
      numzeros = 1
      while n != len(upper):
        upperlist[n] = "0"
        n += 1
        numzeros += 1
      break
    else:
      pass

  upper = "".join(map(str, upperlist))
  upper = upper.rstrip("0")

  binary = bin(int(upper))[2:]
  zeros = bin(int(numzeros))[2:]
  zeros = '0' * (10 - len(str(zeros))) + str(zeros)
  binary += zeros


  return binary