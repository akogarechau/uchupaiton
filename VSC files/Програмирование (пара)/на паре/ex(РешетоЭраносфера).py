def eratosthenes(N):
    sequence = [x for x in range(2, N+1)]
            
    for k in sequence:
        for mult in range(2, N):
            p = k * mult
            if p in sequence:
                sequence.remove(p)
    
    return sequence

print(eratosthenes(51))