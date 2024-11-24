# Time: O(n)
# Space: O(n)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            while s and s[-1] > 0 and a < 0:
                # left asteroid explode
                if s[-1] + a < 0: s.pop()
                # right asteroid explode
                elif s[-1] + a > 0: break  
                # two euqal asteroid, both explode
                else: s.pop(); break
            else: s.append(a)        
        return s