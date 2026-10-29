
def lcs_algo():
    S1 = "PRESIDENT"
    S2 = "PROVIDENCE"

    m = len(S1)
    n = len(S2)

    # Create LCS table filled with zeros
    LCS_table = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the table using Dynamic Programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S1[i - 1] == S2[j - 1]:
                LCS_table[i][j] = LCS_table[i - 1][j - 1] + 1

            elif LCS_table[i - 1][j] >= LCS_table[i][j - 1]:
                LCS_table[i][j] = LCS_table[i - 1][j]

            else:
                LCS_table[i][j] = LCS_table[i][j - 1]

    # Find the LCS length
    index = LCS_table[m][n]
    lcs = [""] * index

    # Backtracking to find the LCS
    i = m
    j = n

    while i > 0 and j > 0:
        if S1[i - 1] == S2[j - 1]:
            lcs[index - 1] = S1[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif LCS_table[i - 1][j] > LCS_table[i][j - 1]:
            i -= 1

        else:
            j -= 1

    lcs = "".join(lcs)

    # Print the result
    print("S1:", S1)
    print("S2:", S2)
    print("LCS length:", len(lcs), "and LCS is:", lcs)


lcs_algo()
