class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        node_to_routes = {}
        route_to_nodes = {}
        for i, route in enumerate(routes):
            node_to_routes[i] = set(route)
            for r in route:
                if r not in route_to_nodes:
                    route_to_nodes[r] = set()
                route_to_nodes[r].add(i)

        answer = 1
        nodes = {node for node in route_to_nodes[source]}
        next_nodes = set()
        done = {}

        while nodes:
            node = nodes.pop()
            if node not in done:
                done[node] = answer
                routes = node_to_routes[node]
                if target in routes:
                    return answer
                for route in routes:
                    for next_node in route_to_nodes[route]:
                        next_nodes.add(next_node)
            if not nodes:
                nodes = next_nodes
                next_nodes = set()
                answer += 1
        return -1
        