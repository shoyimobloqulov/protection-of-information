# Define two binary numbers
a = 0b1010  # 10 in decimal
b = 0b1100  # 12 in decimal

# Bitwise AND
and_result = a & b
print(f"Bitwise AND: {a:b} & {b:b} = {and_result:b} ({and_result})")

# Bitwise OR
or_result = a | b
print(f"Bitwise OR: {a:b} | {b:b} = {or_result:b} ({or_result})")

# Bitwise XOR
xor_result = a ^ b
print(f"Bitwise XOR: {a:b} ^ {b:b} = {xor_result:b} ({xor_result})")

# Bitwise NOT
not_result = ~a
print(f"Bitwise NOT: ~{a:b} = {not_result:b} ({not_result})")

# Left Shift
left_shift_result = a << 2
print(f"Left Shift: {a:b} << 2 = {left_shift_result:b} ({left_shift_result})")

# Right Shift
right_shift_result = a >> 2
print(f"Right Shift: {a:b} >> 2 = {right_shift_result:b} ({right_shift_result})")
