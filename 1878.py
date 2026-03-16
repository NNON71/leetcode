#1878. Get Biggest Three Rhombus Sums in a Grid
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        st = set()

        for i in range(m):
            for j in range(n):
                st.add(grid[i][j])

                k = 1
                while True:
                    b = i + 2*k
                    l = j - k
                    r = j + k

                    if b >= m or l < 0 or r >= n: break

                    _sum = 0
                    x, y = i, j

                    for t in range(k):
                        _sum += grid[x + t][y + t]
                        _sum += grid[x + k + t][y + k - t]
                        _sum += grid[x + 2*k - t][y - t]
                        _sum += grid[x + k - t][y - k + t]

                    k += 1
                    st.add(_sum)
        
        return sorted(list(st))[:-4:-1]
  