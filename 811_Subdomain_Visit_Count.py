# leetcode
from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_counter = defaultdict(int)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)
            sub_domains = domain.split(".")
            i = 0
            while i < len(sub_domains):
                sub_domain = ".".join(sub_domains[i:])
                domain_counter[sub_domain] += count
                i += 1

        return [" ".join([str(count), sub_domain]) for sub_domain, count in domain_counter.items()]
        