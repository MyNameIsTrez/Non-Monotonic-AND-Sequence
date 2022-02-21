def main():
	non_monotonic_strings_count = calculate_non_monotonic_strings_count()
	print(non_monotonic_strings_count)


def calculate_non_monotonic_strings_count():
	n = 0

	for start in range(1, 10):
		for i in range(start, 10):
			n += i

	return n


if __name__ == "__main__":
	main()