# L=Left, R=Right, B=Bottom, T=Top
def rectOverlapArea(R1,L1,B1,T1,R2,L2,B2,T2):
    # calculates the overlapping area of two rectangles
    R = min(R1,R2)
    L = max(L1,L2)
    B = max(B1,B2)
    T = min(T1,T2)
    return max((R-L),0)*max((T-B),0)

print(rectOverlapArea(2,0,0,2,3,1,1,3))
print(rectOverlapArea(1,-3.5,1,4,1,-2.5,-1,3.5))
print(rectOverlapArea(-0.5,-4,-0.5,4,3.5,0.5,1,3))
