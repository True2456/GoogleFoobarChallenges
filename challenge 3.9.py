def solution(bricks):
    # convert inputs into integers
    bricks = int(bricks)
    # DP Table with two states, 1 for the number of bricks, 1 for the step
    DpTable = [[0 for x in range(bricks + 5)] for y in range(bricks + 5)]

    # Initialize all elements of the DP table to 0
    for i in range(bricks + 1):
        for step in range(bricks + 1):
            DpTable[i][step] = 0
    # Base case
    DpTable[3][2] = DpTable[4][2] = 1

    for i in range(5, bricks + 1):
        for step in range(2, i + 1):
            # If step is equal to two
            if (step == 2):
                DpTable[i][step] = DpTable[i - step][step] + 1
            # Else if step is greater than two
            else:
                DpTable[i][step] = (DpTable[i - step][step] +
                                 DpTable[i - step][step - 1])
    # Count the total amount of all the staircases possible from the steps
    answer = 0
    for i in range(1, bricks + 1):
        answer = answer + DpTable[bricks][i]

    return answer


def test():
    print("test1")
    assert solution(3) == 1
    print("test2")
    assert solution(4) == 1
    print("tests complete")


