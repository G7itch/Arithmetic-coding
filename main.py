from decimal import getcontext, Decimal

#def write_bitstream(bits):
#  sio = StringIO(bits)
#  filename = input("Enter filename to save to: ")
#  with open(filename, 'wb') as f:
#    while 1:
#      b = sio.read(8)
#      if not b:
#        break
#      if len(b) < 8:
#        b = b + '0' * (8 - len(b))
#      i = int(b, 2)
#      f.write(i.to_bytes(1, byteorder='big'))


def find_between_bounds(lower, upper):
  lower, upper = Decimal(lower), Decimal(upper)
  n = 1
  total = Decimal(0)
  sequence = []
  while total <= upper:
    c = Decimal(1 / (2**n))
    if lower <= total <= upper:
      break

    if (total + c) <= upper:
      total += c
      sequence.append(1)
    else:
      sequence.append(0)

    n += 1
  return total, sequence


getcontext().prec = 1500

msg = input("Enter message: ")

freq_dict = {}
for letter in msg:
  if letter not in freq_dict:
    freq_dict[letter] = 1
  else:
    freq_dict[letter] += 1

prob_dict = {
  key: float(value) / sum(freq_dict.values())
  for (key, value) in freq_dict.items()
}

newprob = {}

last_value = 0
for key, value in prob_dict.items():
  value = value
  newprob[key] = [last_value, last_value + value]
  last_value = last_value + value

lower = Decimal(0)
upper = Decimal(1)
for letter in msg:
  currentrange = Decimal(upper - lower)
  upper = lower + (currentrange * Decimal(newprob[letter][1]))
  lower = lower + (currentrange * Decimal(newprob[letter][0]))

lower = Decimal(lower)
upper = Decimal(upper)

result = find_between_bounds(lower, upper)
sequence = "".join([str(i) for i in result[1]])
print(sequence)

decodedstring = ""
encodedval = (find_between_bounds(lower, upper)[0])
letters_left = len(msg)
while letters_left >= 1:
  for (key, values) in newprob.items():
    values[0] = Decimal(values[0])
    values[1] = Decimal(values[1])
    if values[0] < encodedval <= values[1]:
      decodedstring += key
      currentrange = Decimal(values[1] - values[0])
      encodedval = (encodedval - values[0]) / currentrange
      letters_left -= 1

print(decodedstring)
