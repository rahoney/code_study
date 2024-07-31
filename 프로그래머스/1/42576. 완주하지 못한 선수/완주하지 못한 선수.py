def solution(participant, completion):
    answer = []
    hash_map = {}
    for p in participant:
        if p in hash_map:
            hash_map[p] += 1
        else:
            hash_map[p] = 1
    #print(hash_map)
    for c in completion:
        if c in hash_map:
            hash_map[c] -= 1
            #print(hash_map)
            if hash_map[c] == 0:
                del hash_map[c]
            #print(hash_map)
    answer = list(hash_map.keys())[0]
    return answer
    #print(answer)
        #completion
    # for p in participant:
    #     hash_map[p] = hash_map.get(p, 0) + 1
    # for c in completion:
    #     hash_map[c] -= 1
    # for p in hash_map:
    #     if hash_map[p] > 0:
    #         return p