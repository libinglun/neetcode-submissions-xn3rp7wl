class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use tuple as key of a dictionary
        output = {}
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            if tuple(count) not in output:
                output[tuple(count)] = []
            output[tuple(count)].append(string)

        return list(output.values())