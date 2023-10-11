from collections import defaultdict

class Solution:
    def trap(self, height: List[int]) -> int:
        def get_answer(start, end):
            answer = 0
            max_val = min(height[start], height[end])
            for i in range(start+1, end):
                answer += max_val - height[i]
            return answer
        answer = 0
        heights = defaultdict(list)
        searched = None
        for i, h in enumerate(height):
            if h > 0:
                if len(heights[h]) == 2:
                    heights[h][1] = i
                else:
                    heights[h].append(i)
        heights_keys = sorted(heights.keys())        
        if heights_keys:
            searched = [heights[heights_keys[-1]].pop()] * 2
            while heights_keys:
                h = heights_keys.pop()
                hs = heights[h]
                if len(hs) == 2:
                    if hs[1] < searched[0]:
                        hs.pop()
                    elif hs[0] > searched[1]:
                        hs = [hs[1]]
                for i in hs:
                    if i < searched[0]:
                        answer += get_answer(i, searched[0])
                        searched[0] = i
                    elif i > searched[1]:
                        answer += get_answer(searched[1], i)
                        searched[1] = i
        return answer
