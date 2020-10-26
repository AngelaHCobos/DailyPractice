class Solution(object):
    def compress(self, chars):
        result = []
        counter = 0
        last_char = chars[0]
        for c in chars:
            if c == last_char:
                counter += 1
            else:
                result.append(last_char)
                if counter > 1:
                    result.append(counter)
                counter = 0
                last_char = c 
        result.append(last_char)
        if counter > 1:
            result.append(counter)
        return result


print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))
# ['a', '2', 'b', 'c', '3']