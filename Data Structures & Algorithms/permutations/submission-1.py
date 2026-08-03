class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        def dfs(visited):
            # Base case: current path has used all numbers
            if len(perm) == len(nums):
                res.append(perm[:])  # Make a copy of path
                return

            for num in nums:
                if num in visited:
                    continue

                perm.append(num)
                visited.add(num)

                dfs(visited)

                perm.pop()
                visited.remove(num)

        dfs(set())
        return res

        '''
        def dfs(i):
            if i == len(nums):
                res.append(nums[:])
                return 
            print(i)
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                print(nums[0: i+1], nums[i+1:])
                dfs(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        dfs(0)
        return res
        '''
                