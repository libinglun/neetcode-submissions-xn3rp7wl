class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        encoded_str += str(len(strs)) + '#'
        for string in strs:
            length = len(string)
            encoded_str += str(length) + '#' + string

        return encoded_str

    def decode(self, s: str) -> List[str]:
        index = 0
        num_delimiter = s.find('#')
        num_strings = int(s[:num_delimiter])
        index = num_delimiter + 1
        decoded_str = []
        for i in range(num_strings):
            len_delimiter = s.find('#', index)
            length = int(s[index:len_delimiter])
            index = len_delimiter + 1
            string = s[index:index+length]
            index += length
            decoded_str.append(string)

        return decoded_str

