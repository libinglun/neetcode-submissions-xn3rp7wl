class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visiting = set()
        visited = set()

        ans = []

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)

            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            ans.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans

