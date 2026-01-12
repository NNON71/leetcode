class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # --- AP1 ---
        # start = points[0]
        # time = 0

        # def direction(diff) :
        #     if diff > 0 :
        #         return -1 #(left, down)
        #     elif diff < 0 :
        #         return 1 # (right, up)
        #     else :
        #         return 0
    
        # for point in points[1:] :
        #     while start != point :
        #         x_diff, y_diff = start[0] - point[0], start[1] - point[1]
        #         dig_x, dig_y = direction(x_diff), direction(y_diff)
        #         if dig_x == 0 or dig_y == 0 :
        #             time += 1
        #         else :
        #             time +=  1 # 2 ** (1/2) 
        #         start[0] += dig_x
        #         start[1] += dig_y
        #         # print(start, time)
        #     start = point
        # return time
        
        # -- AP2 --
        time = 0 
        for i in range(len(points) - 1):
            dx, dy = abs(points[i][0] - points[i + 1][0]), abs(points[i][1] - points[i + 1][1])
            max_time = max(dx, dy)
            time += max_time
        return time
s= Solution()
print(s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
print(s.minTimeToVisitAllPoints([[3,2],[-2,2]]))
