import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

decimal_sum = 0
for l in f:
  value = l.strip()
  curr = 0
  place = 1
  for d in reversed(value):
    if d.isnumeric():
      curr += place * int(d)
    elif d == '-':
      curr -= place
    else:
      curr -= place * 2
    place *= 5
  decimal_sum += curr

snafu_number = ""
while decimal_sum:
  decimal_sum, remainder = divmod(decimal_sum, 5)
  if remainder == 0:
    snafu_number += '0'
  elif remainder == 1:
    snafu_number += '1'
  elif remainder == 2:
    snafu_number += '2'
  elif remainder == 3:
    snafu_number += '='
    decimal_sum += 1
  else:
    snafu_number += '-'
    decimal_sum += 1

# answer: 2==221=-002=0-02-000
print(''.join(reversed(snafu_number)))
