#!/usr/bin/python3

Seq1 = "ATGTTATAG"

for i in range(0,len(Seq1),3):
    #print(Seq1[i])
    print(Seq1[i:i+3])


print(Seq1[::-1])

