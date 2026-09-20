"""AHC069 入出力確認用の簡易インタラクティブジャッジ（公式ツールではない）"""
import subprocess
import sys
from pathlib import Path

SOLVER = Path(__file__).with_name("ahc69-a.py")

# 小さめのダミー入力（入出力確認専用）
N = 8
M = 3
R = 0.01
GRID = [
    "........",
    "........",
    "..##....",
    "..##....",
    "........",
    "........",
    "........",
    "........",
]
# i S T P V
GROUPS = [
    (0, 0, 10, 4, 100),
    (1, 5, 20, 4, 100),
    (2, 15, 30, 9, 200),
]


def main():
    proc = subprocess.Popen(
        [sys.executable, "-u", str(SOLVER)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )

    def send(line=""):
        proc.stdin.write(line + "\n")
        proc.stdin.flush()

    def recv():
        line = proc.stdout.readline()
        if line == "":
            err = proc.stderr.read()
            raise RuntimeError(f"solver closed unexpectedly\nstderr:\n{err}")
        return line.rstrip("\n")

    send(f"{N} {M} {R}")
    for row in GRID:
        send(row)

    occupied = [[-1] * N for _ in range(N)]
    active = {}

    for gi, (i, S, T, P, V) in enumerate(GROUPS):
        for gid in [gid for gid, (t, _) in active.items() if t < S]:
            _, cells = active.pop(gid)
            for x, y in cells:
                occupied[x][y] = -1

        send(f"{i} {S} {T} {P} {V}")
        print(f"[judge] group {i} sent", flush=True)

        a = int(recv())
        print(f"[judge] A={a}", flush=True)
        if a < 0 or a > len(active):
            raise RuntimeError(f"invalid A={a}")
        for _ in range(a):
            j = int(recv())
            cells = []
            # Pj unknown here easily; read until we have Pj from active
            pj = len(active[j][1]) if j in active else None
            if pj is None:
                raise RuntimeError(f"move unknown group {j}")
            for __ in range(pj):
                x, y = map(int, recv().split())
                cells.append((x, y))
            print(f"[judge] move {j} -> {cells}", flush=True)

        verdict = recv()
        print(f"[judge] {verdict}", flush=True)
        if verdict == "No":
            continue
        if verdict != "Yes":
            raise RuntimeError(f"expected Yes/No, got {verdict!r}")

        cells = []
        for _ in range(P):
            x, y = map(int, recv().split())
            cells.append((x, y))
            if not (0 <= x < N and 0 <= y < N):
                raise RuntimeError(f"out of range {(x,y)}")
            if GRID[x][y] == "#":
                raise RuntimeError(f"pond {(x,y)}")
            if occupied[x][y] >= 0:
                raise RuntimeError(f"overlap {(x,y)}")

        # connectivity check
        s = set(cells)
        if len(s) != P:
            raise RuntimeError("duplicate cells")
        from collections import deque
        q = deque([cells[0]])
        seen = {cells[0]}
        while q:
            x, y = q.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nxt = (x + dx, y + dy)
                if nxt in s and nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
        if len(seen) != P:
            raise RuntimeError("not connected")

        for x, y in cells:
            occupied[x][y] = i
        active[i] = (T, cells)
        print(f"[judge] accepted {cells}", flush=True)

    proc.stdin.close()
    ret = proc.wait(timeout=5)
    err = proc.stderr.read()
    if ret != 0:
        raise RuntimeError(f"solver exit {ret}\nstderr:\n{err}")
    print("[judge] I/O OK", flush=True)


if __name__ == "__main__":
    main()
