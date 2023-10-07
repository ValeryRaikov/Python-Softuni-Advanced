longest_intersection = set()

for _ in range(int(input())):
    first, second = [list(map(int, el.split(",")))for el in input().split("-")]

    first_range = set(range(first[0], first[1] + 1))
    second_range = set(range(second[0], second[1] + 1))

    intersection = first_range.intersection(second_range)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(
    f"Longest intersection is [{', '.join(str(num) for num in longest_intersection)}] with length {len(longest_intersection)}"
)
