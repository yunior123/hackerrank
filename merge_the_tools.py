def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        sub = string[i:i+k]
        seen = set()
        for letter in sub:
            if letter not in seen:
                print(letter, end='')
                seen.add(letter)
        print()
