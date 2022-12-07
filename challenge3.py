import numpy as np


def detect_states(matrix):
    active, terminal = [], []
    for rowN, row in enumerate(matrix):
        (active if sum(row) else terminal).append(rowN)
    result = (active,terminal)
    return result

def simplest_form(inputArray):
    inputArray = inputArray.round().astype(int).A1
    gcd = np.gcd.reduce(inputArray)
    inputArray = np.append(inputArray, inputArray.sum())
    result = (inputArray / gcd).astype(int)
    return result


def solution(m):
    active, terminal = detect_states(m)
    if 0 in terminal:
        return [1] + [0]*len(terminal[1:]) + [1]
    m = np.matrix(m, dtype=float)[active, :]
    CD = np.prod(m.sum(1))
    P = m / m.sum(1)
    Q, R = P[:, active], P[:, terminal]
    I = np.identity(len(Q))
    N = (I - Q) ** (-1)
    B = N[0] * R * CD / np.linalg.det(N)
    result = simplest_form(B)
    return result