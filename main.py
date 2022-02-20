import operator


def main(binary_fn):
	non_monotonic_strings = get_non_monotonic_strings()

	print(f"binary function: {binary_fn}\n")

	right = 0
	while True:
		sequence = get_sequence(right, binary_fn)
		if is_monotonic(sequence, non_monotonic_strings):
			print(f"right: {right}, monotonic sequence: {sequence}\n")
		right += 1


def get_non_monotonic_strings():
	non_monotonic_strings = []

	for i in range(10):
		for j in range(10):
			for k in range(10):
				if (i < j > k):
					non_monotonic_strings.append(f"{i}{j}{k}")

	return non_monotonic_strings


def get_sequence(right, binary_fn):
	"""
	The sequence lengths. See the README for the full sequences.
	1 -> 0b001 -> 2 ** (0 + 1) -> 2
	2 -> 0b010 -> 2 ** (1 + 1) -> 4
	3 -> 0b011 -> 2 ** (1 + 1) -> 4
	4 -> 0b100 -> 2 ** (2 + 1) -> 8
	"""
	x = []

	for left in range(2 ** (get_most_significant_bit_index(right) + 1)):
		x.append(str(binary_fn(left, right)))

	return "".join(x)


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


def is_monotonic(sequence, non_monotonic_strings):
	for non_monotonic_string in non_monotonic_strings:
		if non_monotonic_string in sequence:
			return False
	return True


if __name__ == "__main__":
	binary_fn = operator.and_
	# binary_fn = operator.or_
	# binary_fn = operator.xor

	main(binary_fn)