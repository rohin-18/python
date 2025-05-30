class Solution(object):
    def balancedStringSplit(self, s):
        w_count = l_count = r_count = 0
        for ch in s:
            if ch == "L":
                l_count += 1
            else:
                r_count += 1
            if l_count == r_count:
                w_count += 1
        return w_count
