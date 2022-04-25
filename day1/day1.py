def read_data(lines: list[str]) -> list[int]:
    return list(map(int, lines))

def count_increases(depths: list[int]):
    depths_next = depths[1:]
    increased = [value-next_value for value, next_value in zip(depths, depths_next) if value < next_value]
    return len(increased)

def count_sliding_window(depths: list[int]):
    depths2 = depths[1:]
    depths3 = depths[2:]
    sliding_window = [value+value2+value3 for value, value2, value3 in zip(depths, depths2, depths3)]
    return sliding_window

if __name__ == "__main__":
    # Read in data
    file = open("test.txt", "r").readlines()
    depths = read_data(file)

    # Part 1
    print(count_increases(depths))

    # Part 2
    three_measurements = count_sliding_window(depths)
    print(count_increases(three_measurements))