import math

A = float(input("Enter the A: "))
B = float(input("Enter the B: "))
C = float(input("Enter the C: "))

def Up_plus():
    L1 = B * -1
    L2 = math.pow(B, 2) - 4 * A * C
    if L2 < 0 :
        print("Unreal Number")
    else:
        L2_S = math.sqrt(L2)
        return L2_S + L1

def Up_mince():
    L1 = B * -1
    L2 = math.pow(B, 2) - 4 * A * C
    if L2 < 0:
        print("Unreal Number")
    else:
        L2_S = math.sqrt(L2)
        return L1 - L2_S

def down():
    DW = A * 2
    return DW

X1 = Up_plus()/down()
X2 = Up_mince()/down()

print(f"X1 = {X1}")
print(f"X2 = {X2}")