from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #graph node: [child1, child2] for len of num course
        pre_map = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)
        
        visited = set()
        def dfs(course):
            #return false if cyclic
            if course in visited: return False
            #premap[course] == []
            if not pre_map[course]: return True
            visited.add(course)
            for courses in pre_map[course]:
                #if dfs(courses) returns false
                if not dfs(courses): return False
            #remove last element to explore other dfs paths
            #and no longer visiting already visited 
            visited.remove(course)
            # once visited make it empty so that it doesnt repeat the dfs
            pre_map[course] = []
            #if it reaches here then its not cyclic
            return True
        #for graph if not fully connected 
        #ex: 1 -> 2, 3-> 4
        for course in range(numCourses):
            if not dfs(course): return False
        #if it reaches here then can finish all courses
        return True

if __name__=="__main__":
    numCourses = 6
    prerequisites = [[1,0],[1,2],[1,3],[2,4],[3,5],[5,3]]
    sol = Solution()
    print(sol.canFinish(numCourses, prerequisites)) #False


        