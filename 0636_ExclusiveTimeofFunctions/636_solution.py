class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0 for _ in range(n)]
        stack = []
        for log in logs:
            i, status, time = log.split(':')
            i, time = int(i), int(time)
            if status == 'end':
                time += 1
            
            if not stack:
                stack.append([i, status, time])
            
            elif stack and stack[-1][0] == i and stack[-1][1] == 'start' and status == 'end':
                # end a task
                res[i] += time - stack[-1][2]
                stack.pop()
                if stack:
                    stack[-1][2] = time
            
            else:
                # start a task
                res[stack[-1][0]] += time - stack[-1][2]
                stack.append([i, status, time])
                
        return res
                
                
            