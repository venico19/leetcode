class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        distances = []
        distances.append(self.distance(p1, p2))
        distances.append(self.distance(p1, p3))
        distances.append(self.distance(p1, p4))
        distances.append(self.distance(p2, p3))
        distances.append(self.distance(p2, p4))
        distances.append(self.distance(p3, p4))
        
        distances.sort()

        if distances[0] == 0:
            return False
        if not distances[0] == distances[1] == distances[2] == distances[3]:
            return False
        return True
        
    def distance(self, p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
