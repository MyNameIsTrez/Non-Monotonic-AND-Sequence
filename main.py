def get_non_monotonic_strings():
	non_monotonic_strings = []

	for i in range(10):
		for j in range(10):
			for k in range(10):
				if (i < j > k):
					non_monotonic_strings.append(f"{i}{j}{k}")

	return non_monotonic_strings


def main():
	non_monotonic_strings = get_non_monotonic_strings()
	print(len(non_monotonic_strings))


if __name__ == "__main__":
	main()