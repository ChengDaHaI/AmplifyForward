#coding=utf-8 
from sage.all import *
import math
import numpy

#信道维度
L=2
M=2
#两跳信道矩阵
is_set_H=True
if is_set_H == True:
    Ha = matrix(RR, M, L, [[0.979236523248108, -0.129396925980777], [0.594475351529458, 0.666023537533719]])
    Hb = matrix(RR, M, L, [[ 0.806026835557602,-0.267139360752616], [0.455755216914796, 0.590419325969173]])
else:
    Ha = matrix.random(RR, M, L, distribution=RealDistribution('gaussian', 1))
    Hb = matrix.random(RR, M, L, distribution=RealDistribution('gaussian', 1))

#对信道矩阵H进行SVD分解，
#并返回按从大到小排列的奇异值数组S
def Compute_SVD(H):
    U,S,V=numpy.linalg.svd(H)
    return S

#计算AmplifyForward系统速率
#即等效MIMO信道速率
def Compute_sum_rate(Ps,Pr,L,M,Ha,Hb):
    '''
    if len(Pt)!=L:
        raise Exception('error: the length of P_t do not equal L!')
    #计算等效信道H奇异值
    '''
    P=[]#存储信号功率
    N=[]#存储噪声功率
    rate1,rate2=[],[]#存储速率
    H=[]#存储等效信道矩阵
    for i in range(L):
        temp=Hb.row(i)*math.sqrt(Pr/(Ha.row(i).norm()**2*Ps+1))
        h=temp*Ha
        H.append(h)
        #P[i]=(Hb.row(i)*math.sqrt(Pr*Ps/(Ha.row(i).norm()**2*Ps+1))*Ha).norm()**2
        P.append((h*math.sqrt(Ps)).norm()**2)
        N.append(temp.norm()**2+1)
        r=log((1+(P[i]/N[i])),2)
        rate1.append(r)
    capacity=sum(rate1)#传输速率之和
    return capacity
    '''
    lamada=Compute_SVD(H)
    k=0
    for i in range(min(L,M)):
        if lamada[i]!=0:
            k+=1
    capacity=k*log((Ps/),2)
    '''

if __name__=="__main__" :
    Ps=100
    Pr=100
    print Compute_sum_rate(Ps, Pr, L, M, Ha, Hb)