class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        answer = [-1, -1]        
        ones = [i for i, val in enumerate(arr) if val == 1]
        if len(ones) % 3 == 0:
            if ones:
                size = len(ones) // 3
                sums = [sum(ones[size*i:size*(i+1)])for i in range(3)]
                sums[0] -= ones[0] * size
                sums[1] -= ones[size] * size
                sums[2] -= ones[size*2] * size
                if sums[0] == sums[1] == sums[2]:
                    num_zeros = len(arr) - ones[-1] - 1
                    if ones[size]-ones[size-1]-1 >= num_zeros and ones[size*2]-ones[size*2-1]-1 >= num_zeros :
                        answer = [ones[size-1]+num_zeros, ones[size*2-1]+num_zeros+1]
            else:
                answer = [0, len(arr)-1]
        return answer