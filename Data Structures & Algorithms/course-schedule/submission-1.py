class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visiting = set()
        visited = set()

        def dfs(course):
            # hit a loop in current prerequisite path
            if course in visiting:
                return False

            # hit a safe path, early return
            if course in visited:
                return True

            visiting.add(course)
            pres = pre_map[course]
            for pre in pres:
                if not dfs(pre):
                    return False

            # backtrack on the path
            visiting.remove(course)
            visited.add(course)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

