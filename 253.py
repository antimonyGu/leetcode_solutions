class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        h = []
        sorted_i = sorted(intervals)
        for i in sorted_i:
            if h == [] or h[0] > i[0]:
                heapq.heappush(h, i[1])
            else:
                heapq.heapreplace(h, i[1])
        
        return len(h)