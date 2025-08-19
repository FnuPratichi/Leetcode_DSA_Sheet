import sys
import threading
import heapq

def main():
    import sys
    sys.setrecursionlimit(1 << 25)

    INF = 1 << 60

    n, q, s = map(int, sys.stdin.readline().split())
    s -= 1

    size = 1
    while size < n:
        size <<= 1

    offset1 = n
    offset2 = offset1 + 2 * size
    V = offset2 + 2 * size

    adj = [[] for _ in range(V)]

    def build_tree(v, lx, rx, rev, base):
        if rx - lx == 1:
            if not rev:
                adj[base + v].append((lx, 0))
            else:
                adj[lx].append((base + v, 0))
            return
        m = (lx + rx) // 2
        build_tree(2 * v, lx, m, rev, base)
        build_tree(2 * v + 1, m, rx, rev, base)
        if not rev:
            adj[base + v].append((base + 2 * v, 0))
            adj[base + v].append((base + 2 * v + 1, 0))
        else:
            adj[base + 2 * v].append((base + v, 0))
            adj[base + 2 * v + 1].append((base + v, 0))

    def add_edge_from(v, ql, qr, w, x, lx, rx, base):
        if rx <= ql or lx >= qr:
            return
        if lx >= ql and rx <= qr:
            adj[v].append((base + x, w))
            return
        m = (lx + rx) // 2
        add_edge_from(v, ql, qr, w, 2 * x, lx, m, base)
        add_edge_from(v, ql, qr, w, 2 * x + 1, m, rx, base)

    def add_edge_to(ql, qr, v, w, x, lx, rx, base):
        if rx <= ql or lx >= qr:
            return
        if lx >= ql and rx <= qr:
            adj[base + x].append((v, w))
            return
        m = (lx + rx) // 2
        add_edge_to(ql, qr, v, w, 2 * x, lx, m, base)
        add_edge_to(ql, qr, v, w, 2 * x + 1, m, rx, base)

    build_tree(1, 0, size, False, offset1)
    build_tree(1, 0, size, True, offset2)

    for _ in range(q):
        parts = list(map(int, sys.stdin.readline().split()))
        t = parts[0]
        if t == 1:
            _, v, u, w = parts
            v -= 1
            u -= 1
            adj[v].append((u, w))
        elif t == 2:
            _, v, l, r, w = parts
            v -= 1
            l -= 1
            add_edge_from(v, l, r, w, 1, 0, size, offset1)
        else:
            _, v, l, r, w = parts
            v -= 1
            l -= 1
            add_edge_to(l, r, v, w, 1, 0, size, offset2)

    dist = [INF] * V
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))

    print(' '.join(str(-1 if dist[i] == INF else dist[i]) for i in range(n)))


if __name__ == "__main__":
    threading.Thread(target=main).start()
