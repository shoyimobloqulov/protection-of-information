def circular_left_shift(value, shift, bit_width):
    """
    Perform a circular left bit shift.
    
    :param value: The integer value to shift.
    :param shift: The number of positions to shift.
    :param bit_width: The bit width of the value.
    :return: The result of the circular left shift.
    """
    shift %= bit_width
    return ((value << shift) & ((1 << bit_width) - 1)) | (value >> (bit_width - shift))

def circular_right_shift(value, shift, bit_width):
    """
    Perform a circular right bit shift.
    
    :param value: The integer value to shift.
    :param shift: The number of positions to shift.
    :param bit_width: The bit width of the value.
    :return: The result of the circular right shift.
    """
    shift %= bit_width
    return (value >> shift) | ((value << (bit_width - shift)) & ((1 << bit_width) - 1))

bit_width = 8 
value = 0b10110011 

left_shifted_value = circular_left_shift(value, 3, bit_width)
print(f"Circular Left Shifted Value: {left_shifted_value:0{bit_width}b}")

right_shifted_value = circular_right_shift(value, 3, bit_width)
print(f"Circular Right Shifted Value: {right_shifted_value:0{bit_width}b}")
