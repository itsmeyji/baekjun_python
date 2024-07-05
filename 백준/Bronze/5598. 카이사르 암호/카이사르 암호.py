CYP = input()

PLAIN = ""
CYlen = len(CYP)

for i in range(CYlen):
    if CYP[i] not in ('A', 'B', 'C'):
        PLAIN_CHAR = ord(CYP[i]) - 3
        PLAIN += chr(PLAIN_CHAR)
    else:
        PLAIN_CHAR = ord(CYP[i]) + 23
        PLAIN += chr(PLAIN_CHAR)

print(PLAIN)
