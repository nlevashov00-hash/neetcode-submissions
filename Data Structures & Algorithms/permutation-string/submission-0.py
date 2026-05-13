class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_1 = collections.defaultdict(int)
        count_2 = collections.defaultdict(int)

        l, r = 0, len(s1) - 1

        for ch in s1:
            count_1[ch] += 1

        for c in s2[:len(s1)]:
            count_2[c] += 1
        
        if count_1 == count_2:
            return True
        else:

            while r < len(s2) - 1:
                count_2[s2[l]] -= 1
                if count_2[s2[l]] == 0:
                    del count_2[s2[l]]
                r += 1
                l += 1
                count_2[s2[r]] += 1

                if count_1 == count_2:
                    return True

        return False