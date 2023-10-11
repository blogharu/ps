class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        results = {t:[0]*len(votes[0]) for t in votes[0]}
        for vote in votes:
            for i, t in enumerate(vote):
                results[t][i] -= 1
        results = sorted((*result, t) for t, result in results.items())
        return "".join(result[-1] for result in results)