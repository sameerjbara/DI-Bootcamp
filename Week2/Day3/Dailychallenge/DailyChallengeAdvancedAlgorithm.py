import random

# Given starter code
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

# Find all pairs that sum to target_number
counts = {}
pairs = set()  # store unique pairs as (small, big)

for x in list_of_numbers:
    need = target_number - x

    # If we've seen the needed number before, we can form pairs with all its occurrences
    if need in counts:
        # Add the pair once (unique by value)
        a, b = (need, x) if need <= x else (x, need)
        pairs.add((a, b))

    # Count current number
    counts[x] = counts.get(x, 0) + 1

# Print results
if not pairs:
    print("No pairs found.")
else:
    for a, b in sorted(pairs):
        print(f"{a} and {b} sums to the target_number {target_number}")
