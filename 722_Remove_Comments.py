# leetcode
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        buffer = []
        in_block = False

        for line in source:
            i = 0
            while i < len(line):
                if not in_block:
                    # line comment
                    if i+1 < len(line) and line[i:i+2] == "//":
                        break
                    # block comment
                    elif i+1 < len(line) and line[i:i+2] == "/*":
                        in_block = True
                        i += 2
                        continue
                    # non-comment
                    else:
                        buffer.append(line[i])
                        i += 1

                else:
                    # check */
                    if i+1 < len(line) and line[i:i+2] == "*/":
                        in_block = False
                        i += 2
                    else:
                        i += 1

            if not in_block and buffer:
                result.append("".join(buffer))
                buffer = []

        return result
