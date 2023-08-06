class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        done = set()
        nodes = {0}
        while nodes:
            node = nodes.pop()
            if node not in done:
                done.add(node)
                for next_node in rooms[node]:
                    nodes.add(next_node)
        return len(done) == len(rooms)