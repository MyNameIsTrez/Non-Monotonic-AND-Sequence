import operator


def main(binary_fn):
	print(f"binary function: {binary_fn}\n")

	right = 0
	while True:
		sequence = get_sequence(right, binary_fn)

		if is_monotonic(sequence):
			print(f"right: {right}, monotonic sequence: {sequence}\n")

		right += 1

		# if right % 1000 == 0:
		# 	print(right)


def get_sequence(right, binary_fn):
	"""
	The sequence lengths. See the README for the full sequences.
	1 -> 0b001 -> 2 ** (0 + 1) -> 2
	2 -> 0b010 -> 2 ** (1 + 1) -> 4
	3 -> 0b011 -> 2 ** (1 + 1) -> 4
	4 -> 0b100 -> 2 ** (2 + 1) -> 8
	"""
	sequence_parts = []

	for left in range(2 ** (get_most_significant_bit_index(right) + 1)):
		sequence_parts.append(str(binary_fn(left, right)))

	return "".join(sequence_parts)


def get_most_significant_bit_index(n):
	"""
	See https://stackoverflow.com/a/4970859/13279557
	"""
	i = 0

	n >>= 1
	while (n > 0):
		i += 1
		n >>= 1

	return i


def is_monotonic(sequence):
	sequence_len = len(sequence)

	if sequence_len <= 1:
		return True

	start_slope_direction = None

	for i in range(0, sequence_len - 1):
		slope_direction = get_slope_direction(sequence[i], sequence[i + 1])

		if start_slope_direction == None and slope_direction != 0:
			start_slope_direction = slope_direction
		elif slope_direction == -1 and start_slope_direction == 1:
			return False
		elif slope_direction == 1 and start_slope_direction == -1:
			return False

	return True


def get_slope_direction(a, b):
	n = int(b) - int(a)

	if n > 0:
		return 1
	elif n == 0:
		return 0
	else:
		return -1


if __name__ == "__main__":
	binary_fn = operator.and_
	# binary_fn = operator.or_
	# binary_fn = operator.xor

	main(binary_fn)