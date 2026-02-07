# leetcode
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_sys = defaultdict(list)
        for path in paths:
            folder = path.split(" ")
            directory = folder[0]
            files = folder[1:]
            for f in files:
                index = f.find("(")
                # only to check the index is correct (content found)
                if index != -1:
                    content = f[index:]
                # assume all files has contents
                full_path = directory + "/" + f[:index]
                file_sys[content].append(full_path)
        result = []
        for c, p in file_sys.items():
            if len(p) > 1:
                result.append(p)
        return result