import numpy as np
n=int(input())
# n,m=map(int,input().split()) 
a=list(map(int,input().split()))
a.sort()
b=[0 for _ in range(a[-1]+1)]
for i in a:
    b[i]=1
f = np.array(b)
g = np.array(b)
fft_len = 1  # |f|+|g|-1 以上の2の冪数
while fft_len<len(f)+len(g)-1:
    fft_len*=2


# f,gをフーリエ変換
Ff = np.fft.rfft(f, fft_len)
Fg = np.fft.rfft(g, fft_len)
 
# 各要素について掛け合わせる
Ffg = Ff * Fg
 
# 逆変換後、整数に丸める
fg = np.fft.irfft(Ffg, fft_len)
fg = np.rint(fg)


ans=0
for i in a:
    ans+=(fg[2*i]-1)//2
print(int(ans))