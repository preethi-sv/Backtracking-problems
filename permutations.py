def permute(string, start, end):
    if start == end:
        print(''.join(string))
    else:
        for i in range(start, end + 1):
            string[start], string[i] = string[i], string[start]  # swap
            # print('Swaps ' + string[i] +' with ' + string[start] + '==' + str(string))
            permute(string, start + 1, end)
            string[start], string[i] = string[i], string[start]  # backtrack
            # print('Swaps back ' + string[i] +' with ' + string[start] + '==' + str(string))


if __name__ == "__main__":
    string = "ABC"
    n = len(string)
    a = list(string)
    permute(a, 0, n - 1)
