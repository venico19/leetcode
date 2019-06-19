class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key = lambda x: x[1])
        heap = []
        time = 0
        for t, end in courses:
            time += t
            heapq.heappush(heap, -t)
            while time > end:
                time += heapq.heappop(heap)
                
        return len(heap)
                