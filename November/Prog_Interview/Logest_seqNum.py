def longest_subsequence(a, n):
    ans = 0

    # Traverse every element to check if any
    # increasing subsequence starts from this index
    for i in range(n):
        # Initialize cnt variable as 1, which defines
        # the current length of the increasing subsequence
        cnt = 1
        for j in range(i + 1, n):
            if a[j] == (a[i] + cnt):
                cnt += 1

        # Update the answer if the current length is
        # greater than the already found length
        ans = max(ans, cnt)

    return ans


if __name__ == "__main__":
    a = [3, 10, 3, 11, 4, 5, 6, 7, 8, 12]
    n = len(a)
    print(longest_subsequence(a, n))

