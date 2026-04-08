class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        num_left = 0  # Start at 0 for cleaner logic
        num_right = 0
        ans = []

        def dfs(current_string, left_count, right_count):
            # Base case: string is full length
            if len(current_string) == 2 * n:
                ans.append(current_string)
                return
            
            # If we can still add a left paren
            if left_count < n:
                dfs(current_string + '(', left_count + 1, right_count)
            
            # If we can add a right paren (must have an open left one to close)
            if right_count < left_count:
                dfs(current_string + ')', left_count, right_count + 1)

        dfs("", 0, 0)
        return ans