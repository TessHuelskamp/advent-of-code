import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()


graph=dict()
for line in lines:
    left, right= line.strip().split("-")

    if left not in graph:
        graph[left]=list()
    if right not in graph:
        graph[right]=list()

    graph[left].append(right)
    graph[right].append(left)

def isSmall(name):
    for c in name:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return False
    return True

assert isSmall("abcd")
assert not isSmall("ABC")

from copy import copy

def visit(node, state):
    state.append(node)

    if node == "end":
        results=list()
        results.append(copy(state))
        return results

    results=list()
    for neigh in graph[node]:
        if isSmall(neigh) and neigh in state:
            pass
        else:
            routes = visit(neigh, copy(state))
            for route in routes:
                results.append(copy(route))

    return results

from collections import Counter

def visit2(node, state):
    state.append(node)

    if node == "end":
        results=list()
        results.append(copy(state))
        return results

    counts=Counter(filter(isSmall, state))
    canExtraVisit=True
    for value in counts.values():
        if value >=2:
            canExtraVisit=False

    toVisit=list()
    for neigh in graph[node]:
        if neigh=="start":
            pass
        elif isSmall(neigh):
            c = counts.get(neigh,0)
            if c == 0:
                toVisit.append(neigh)
            elif c == 1 and canExtraVisit:
                toVisit.append(neigh)
        else:
            toVisit.append(neigh)

    results=list()
    for n in toVisit:
        routes = visit2(n, copy(state))
        for route in routes:
            results.append(copy(route))

    return results

results = visit("start", list())
print(len(results))
r2 = visit2("start", list())
print(len(r2))
