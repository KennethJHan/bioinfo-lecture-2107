Seq1 = "ATGTTATAG"
Seq2 = ""

for s in Seq1:
    if s == "A":
        Seq2 += "T"
    elif s == "C":
        Seq2 += "G"
    elif s == "G":
        Seq2 += "C"
    elif s == "T":
        Seq2 += "A"

print(Seq1)
print(Seq2)

