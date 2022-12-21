import sys, re, math, functools

def floyd_warshall(graph):
    distances = {node: {node: 0} for node in graph}
    for node in graph:
        for link in graph[node][1]:
            distances[node][link] = 1
    for r in graph:
        for p in graph:
            for q in graph:
                distancepq = distances[p].get(q, math.inf)
                distancepr = distances[p].get(r, math.inf)
                distancerq = distances[r].get(q, math.inf)
                distances[p][q] = min(distancepq, distancepr + distancerq)
    return distances

def part1(room_graph):
    positive_flow_nodes = [node for node, (flow, _) in room_graph.items() if flow > 0]
    distances = floyd_warshall(room_graph)
    @functools.lru_cache(None)
    def _traverse_positive_flow(node, time, visited):
        best = 0
        for i, link in enumerate(positive_flow_nodes):
            if visited & (1<<i) == 0 and time > distances[node][link]:
                time_remaining = time - distances[node][link] - 1
                leaked = time_remaining * room_graph[link][0]
                best = max(best, leaked + _traverse_positive_flow(link, time_remaining, visited | (1<<i)))
        return best
    return _traverse_positive_flow('AA', 30, 0)

def part2(room_graph):
    positive_flow_nodes = [node for node, (flow, _) in room_graph.items() if flow > 0]
    distances = floyd_warshall(room_graph)
    @functools.lru_cache(None)
    def _traverse_positive_flow(node1, node2, time1, time2, visited):
        best = 0
        for i, link in enumerate(positive_flow_nodes):
            if visited & (1<<i) == 0:
                if time1 > distances[node1][link]:
                    time_remaining = time1 - distances[node1][link] - 1
                    leaked = time_remaining * room_graph[link][0]
                    best = max(best, leaked + _traverse_positive_flow(link, node2, time_remaining, time2, visited | (1<<i)))
                if time2 > distances[node2][link]:
                    time_remaining = time2 - distances[node2][link] - 1
                    leaked = time_remaining * room_graph[link][0]
                    best = max(best, leaked + _traverse_positive_flow(node1, link, time1, time_remaining, visited | (1<<i)))
        return best
    return _traverse_positive_flow('AA', 'AA', 26, 26, 0)

room_graph = {}
for line in sys.stdin.read().splitlines():
    re_match = re.match('Valve (.{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)', line)
    room, flow, links = re_match.groups()
    flow, links = int(flow), list(map(lambda x: x.strip(), links.split(',')))
    room_graph[room] = (flow, links)

print(f'Part 1: {part1(room_graph)}, Part 2: {part2(room_graph)}')