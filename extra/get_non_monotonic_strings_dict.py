import pprint


def main():
	non_monotonic_strings_dict = get_non_monotonic_strings_dict()
	# This can be piped to a file for easier viewing.
	pprint.pprint(non_monotonic_strings_dict, width=160)


def get_non_monotonic_strings_dict():
	non_monotonic_strings_dict = {}

	for i in range(10):
		for j in range(10):
			for k in range(10):
				if (i < j > k):
					if i not in non_monotonic_strings_dict:
						non_monotonic_strings_dict[i] = {}
					if j not in non_monotonic_strings_dict[i]:
						non_monotonic_strings_dict[i][j] = {}
					non_monotonic_strings_dict[i][j][k] = f"{i}{j}{k}"

	return non_monotonic_strings_dict


if __name__ == "__main__":
	main()