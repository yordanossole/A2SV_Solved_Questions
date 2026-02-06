# leetcode
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        temp = []
        block_flag = False
        l_com, b_com = float('inf'), float('inf')

        for line in source:
            l_com = line.find("//")
            b_com = line.find("/*")
            if not block_flag and l_com == -1 and b_com == -1:
                result.append(line)
                l_com = b_com = float('inf')
                continue
        
            if not block_flag and l_com != -1:
                code = line[:l_com]
                if code:
                    result.append(code)
                    l_com = b_com = float('inf')
                    continue
            
            if b_com != -1:
                # if the line has non-comment code we append non-comment code on temp
                code = line[:b_com]
                if code:
                    temp.append(code)

                # check "*/" on the line
                b_close = line.find("*/")
                if b_close == -1:
                    # turn on block_flag if "*/" not found
                    block_flag = True
                else:
                    # turn off block_flag if "*/" found
                    block_flag = False
                    code = line[b_close+2:]
                    if code:
                        temp.append(code)
                # append remaining code from temp if block comment end
                if not block_flag and temp:
                    result.append("".join(temp))
                    temp = []
        return result
                
