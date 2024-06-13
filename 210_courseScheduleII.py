from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # O(p + n) aka O(e + v) prereq p are edges and number of courses n is the vertices
        res = []
        #build adjacency list
        pre_map ={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        """
course has 3 possible state:
1. visited -> crs has been added to output
2. visiting -> crs not added to output but added to cycle
3. unvisited - crs not added to output or cycle
        """
        visited, cycle = set(), set()
        print(pre_map)
        def dfs(crs):
            print(f'course: {crs}, res: {res}, cycle: {cycle}, visited: {visited}')
            """
- cycle stores if a cycle has actually been found, so we store the current path, and 
if the same vertex comes into the path again it means that it is a cycle
- on the other hand visited means that the current node has already been visited, and 
so far there were no complications, only if therewere no complications will we append to the set. 
therefore it returns true
            """
            if crs in cycle: return False
            #if  visited return avoiding duplicate visitation
            if crs in visited:
                return True 
            
            cycle.add(crs)
            
            for course in pre_map[crs]:
                #if cycle detected
                if not dfs(course): return False
            """ 
we remove from the cycle because the current dfs tree recursion tree is over, 
and we add to visited because this course has already been explored, all the prereq checked, 
would have been added in the recursion tree, now we can add it to output to manitain the order
            """
            cycle.remove(crs) # remove coz no longer at the path
            # remove after visiting
            visited.add(crs)
            #all pre completed
            res.append(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs): return []
        
        return res

if __name__=="__main__":
    s = Solution()
    print(s.findOrder(2, [[1,0]])) # [0,1]