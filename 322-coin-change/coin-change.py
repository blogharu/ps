
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = set(coin for coin in coins if coin <= 10000)
        done = {0: 0}
        count = 1
        nodes = set(coins)
        next_nodes = set()
        while nodes:
            node = nodes.pop()
            if node not in done:
                done[node] = count
                for coin in coins:
                    if node+coin <= 10000:
                        next_nodes.add(node + coin)
            if not nodes:
                nodes = next_nodes
                next_nodes = set()
                count += 1
        return done.get(amount, -1)


        