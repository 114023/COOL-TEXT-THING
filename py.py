def generate_combinations(prefix, target_char):
    if target_char.isalpha():
        start_char = 'a' if target_char.islower() else 'A'
        end_char = target_char
    elif target_char.isdigit():
        start_char = '0'
        end_char = target_char
    else:
        start_char = target_char
        end_char = target_char

    for j in range(ord(start_char), ord(end_char) + 1):
        yield prefix + chr(j)

def main():
    user_input = input("Enter a string (with letters, numbers, symbols, and spaces): ").strip()

    prefix = ''
    for i, target_char in enumerate(user_input):
        combinations = generate_combinations(prefix, target_char)
        for combination in combinations:
            print(combination)
            if combination.startswith(user_input[:i + 1]):
                prefix = user_input[:i + 1]

if __name__ == "__main__":
    main()
