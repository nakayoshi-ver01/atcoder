n=input()
#n,m=map(int,input().split())
#a=list(map(int,input().split()))
s=[['tourist', 3858],
['ksun48', 3679],
['Benq', 3658],
['Um_nik', 3648],
['apiad', 3638],
['Stonefeang', 3630],
['ecnerwala', 3613],
['mnbvmar', 3555],
['newbiedmy', 3516],
['semiexp', 3481]
]
p=['tourist','ksun48','Benq','Um_nik','apiad','Stonefeang','ecnerwala',
   'mnbvmar','newbiedmy','semiexp']
k=p.index(n)
print(s[k][1])