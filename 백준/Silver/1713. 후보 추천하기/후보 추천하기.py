N = int(input())
total_voted = int(input())
voted = list(map(int, input().split()))

candidates = {}
for i in range(total_voted):
    
    if candidates.get(voted[i]):
        candidates[voted[i]] += 1
    
    else:
        
        if len(candidates) == N:
            min = total_voted
        
            for idx in candidates:
                if candidates[idx] < min:
                    min = candidates[idx]
                    remove = idx
        
                elif candidates[idx] == min:
         
                    for j in range(i):
         
                        if voted[j] == remove:
                            break
        
                        if voted[j] == idx:
                            min = candidates[idx]
                            remove = idx
                            break
        
            for _ in range(min):
                voted[voted.index(remove)] = -1
            
            del (candidates[remove])
        
        candidates[voted[i]] = 1

ans = sorted(candidates)
print(*ans)