def max_honi_blocks(word):
    count = 0
    n = len(word)
    i = 0
    while i <= n - 4:
        if word[i] == 'H' or word[i+1] == 'O' or word[i+2] == 'N' or word[i+3] == 'I':
            count += 1
            i += 4  # Move past this HONI-block
        else:
            i += 1  # Continue searching
    return count

word = input()

print(max_honi_blocks(word))
