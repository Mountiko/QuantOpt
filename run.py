import header as h
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Omega = np.linspace(0, 1, 101)
N = len(Omega)
h = (Omega[-1] - Omega[0]) / (N-1)


#x = Omega[50]
def opt_for_2(Omega):
    N = len(Omega)
    h = (Omega[-1] - Omega[0]) / (N-1)

    B = []
    A = []
    for A_pos in Omega:
        B_pos1 = np.arange(0, A_pos, h)
        if len(B_pos1) == 0:
            B_pos_max1 = A_pos
            B_range_max1 = 0
        else:
            B_range1 = (B_pos1 + A_pos) / 2
            B_pos_max1 = B_pos1[np.where(max(B_range1))]
            B_range_max1 = max(B_range1)

        B_pos2 = np.arange(A_pos+h, 1+h, h)
        if len(B_pos2) == 0:
            B_pos_max2 = A_pos
            B_range_max2 = 0
        else:
            B_range2 = 1 - ((B_pos2 + A_pos) / 2)
            B_pos_max2 = B_pos2[np.where(max(B_range2))]
            B_range_max2 = max(B_range2)

        if B_range_max1 < B_range_max2:
            B_range_max = B_range_max2
            B_pos_max = B_pos_max2
        else:
            B_range_max = B_range_max1
            B_pos_max = B_pos_max1
        B.append([B_pos_max, B_range_max])

        A_range = 1 - B_range_max
        A.append([A_pos, A_range])
    A = np.array(A)
    B = np.array(B)
    return A, B

A_pos_all = []
B_pos_all = []
C_pos_all = []

A_range = []
B_range = []
C_range = []

for A_pos in Omega:
    for B_pos in Omega:
        if A_pos == B_pos:
            pass
        else:
            for C_pos in Omega:
                if C_pos == A_pos or C_pos == B_pos:
                    pass
                else:
                    A_pos_all.append(A_pos)
                    B_pos_all.append(B_pos)
                    C_pos_all.append(C_pos)
                    
                    if A_pos < B_pos < C_pos:
                        A_range.append((A_pos + B_pos) * 0.5)
                        B_range.append(((B_pos + C_pos) * 0.5) - ((A_pos + B_pos) * 0.5))
                        C_range.append(1 - ((B_pos + C_pos) * 0.5))
                    elif A_pos < C_pos < B_pos:
                        A_range.append((A_pos + C_pos) * 0.5)
                        C_range.append(((C_pos + B_pos) * 0.5) - ((A_pos + C_pos) * 0.5))
                        B_range.append(1 - ((C_pos + B_pos) * 0.5))
                    elif B_pos < A_pos < C_pos:
                        B_range.append((B_pos + A_pos) * 0.5)
                        A_range.append(((A_pos + C_pos) * 0.5) - ((B_pos + A_pos) * 0.5))
                        C_range.append(1 - ((A_pos + C_pos) * 0.5))
                    elif B_pos < C_pos < A_pos:
                        B_range.append((B_pos + C_pos) * 0.5)
                        C_range.append(((C_pos + A_pos) * 0.5) - ((B_pos + C_pos) * 0.5))
                        A_range.append(1 - ((C_pos + A_pos) * 0.5))
                    elif C_pos < A_pos < B_pos:
                        C_range.append((C_pos + A_pos) * 0.5)
                        A_range.append(((A_pos + B_pos) * 0.5) - ((C_pos + A_pos) * 0.5))
                        B_range.append(1 - ((A_pos + B_pos) * 0.5))
                    elif C_pos < B_pos < A_pos:
                        C_range.append((C_pos + B_pos) * 0.5)
                        B_range.append(((B_pos + A_pos) * 0.5) - ((C_pos + B_pos) * 0.5))
                        A_range.append(1 - ((B_pos + A_pos) * 0.5))
pos_range_df = pd.DataFrame({
                            'A position': A_pos_all, 'B position': B_pos_all,
                            'C position': C_pos_all, 'A range': A_range,
                            'B range': B_range, 'C range': C_range
                            })
pos_range_arr = np.array(pos_range_df)


'''
A, B = opt_for_2(Omega)

fig = plt.figure(figsize=(7,7))
plt.plot(Omega, A[:, 1], label='A range')
plt.plot(Omega, B[:, 1], label='B range')
plt.legend()
plt.grid()
plt.show()'''