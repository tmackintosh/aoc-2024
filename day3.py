import re

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
cond_pattern = r"(do\(\)|don't\(\))"

with open('day3.txt', 'r') as file:
    input_string = file.read()

def validate(str):
    return sum(int(x) * int(y) for x, y in re.findall(mul_pattern, str))

print('total:', validate(input_string))

matches = re.finditer(cond_pattern, input_string)

total = 0
skip_mode = False
last_position = 0

for match in matches:
    segment = input_string[last_position:match.start()].strip()
    if segment and not skip_mode:
        total += sum(validate(item.strip()) for item in segment.split(', '))
    skip_mode = (match.group() == "don't()")
    last_position = match.end()

# the last segment isn't included in the substrings
remaining_segment = input_string[last_position:].strip()
if remaining_segment and not skip_mode:
    total += sum(validate(item.strip()) for item in remaining_segment.split(', '))

print('conditional total:', total)