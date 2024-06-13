# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = int(input())
bc = int(input())



theta = math.atan2(ab , bc)
ro = round(math.degrees(theta))
print(f"{(ro)}"+f"\xb0")
