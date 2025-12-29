from collections import defaultdict
N = int(input())
col = []
dic = defaultdict(list)
for _ in range(N):
    x,c = map(int,input().split())
    if c not in dic:
        col.append(c)
        dic[c] = [x,x]
    else:
        dic[c][0] = min(dic[c][0],x)
        dic[c][1] = max(dic[c][1],x)

col.sort()
left = 0
right = 0
leftans = 0
rightans = 0

for c in col:
    _min,_max = dic[c]
    nxtleftans = 10**30
    nxtrightans = 10**30
    if left <= _min:
        nxtleftans = min(nxtleftans,leftans + 2 * _max  - _min - left )
        nxtrightans = min(nxtrightans, leftans + _max - left )
    elif left >= _max:
        nxtleftans = min(nxtleftans, leftans + left - _min )
        nxtrightans = min(nxtrightans,leftans + left  + _max - 2*_min)
    else:
        nxtleftans = min(nxtleftans,leftans + 2 * _max - _min - left)
        nxtrightans = min(nxtrightans, leftans + left + _max - 2*_min)
    if right <= _min:
        nxtleftans = min(nxtleftans,rightans + 2*_max - right - _min)
        nxtrightans = min(nxtrightans,rightans + _max - right)
    elif right >= _max:
        nxtleftans = min(nxtleftans,rightans + right - _min)
        nxtrightans = min(nxtrightans,rightans + right + _max - 2*_min)
    else:
        nxtleftans = min(nxtleftans,rightans + 2* _max - right - _min)
        nxtrightans = min(nxtrightans,rightans + _max + right - 2 * _min)
    
    leftans = nxtleftans
    rightans = nxtrightans
    left = _min
    right = _max
    
print(min(leftans + abs(left),rightans + abs(right)))

            
        
