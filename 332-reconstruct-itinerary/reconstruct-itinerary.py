from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ts = {}
        for start, end in tickets:
            if start not in ts:
                ts[start] = defaultdict(int)
            ts[start][end]+=1
        for start in ts:
            ts[start][0] = sorted(ts[start])
        answer = ["JFK"]
        def dfs(i, start):
            if i == len(tickets):
                return True
            if start in ts:
                for end in ts[start][0]:
                    if ts[start][end]:
                        ts[start][end] -= 1
                        answer.append(end)
                        if dfs(i+1, end):
                            return True
                        answer.pop()
                        ts[start][end] += 1            
        dfs(0, "JFK")
        return answer 
        