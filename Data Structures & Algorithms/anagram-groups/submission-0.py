class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def is_same(count1: Dict[int], count2: Dict[int]):
            if len(count1) != len(count2):
                return False

            for char, cnt in count1.items():
                if char not in count2:
                    return False
                if count2[char] != cnt:
                    return False
            
            return True

        output = []
        anagram_dict = {}
        
        for string in strs:
            count = {}
            # compute each anagram of each string
            for char in string:
                if char not in count:
                    count[char] = 0
                count[char] += 1

            contained = False
            # check if a new anagram is found, if so, put in the string
            for index, anagram in anagram_dict.items():
                if is_same(count, anagram):
                    output[index].append(string)
                    contained = True
                    break
                
            if not contained: 
            # put the string in the output list if no anagram
                output.append([string])
                anagram_dict[len(output) - 1] = count

        return output
        