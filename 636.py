class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans, stack, prev_time = [0] * n, deque(),0

        for log in logs:
            id, action, timestamp = log.split(":")
            id, timestamp = int(id), int(timestamp)

            if action == 'start':
                # new function call to interupt prev one
                if stack:
                    # update prev function call's duration
                    ans[stack[-1]] += timestamp - prev_time
                
                stack.append(id)
                prev_time = timestamp
            else:
                ans[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
        
        return ans