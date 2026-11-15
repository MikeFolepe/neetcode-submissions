class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}
        for i in range(len(s1)):
            counts1[s1[i]] = counts1.get(s1[i], 0) + 1

        need = len(counts1)

        for i in range(len(s2)):
            count2, curr = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = count2.get(s2[j], 0) + 1

                if counts1.get(s2[j], 0) < count2.get(s2[j], 0):
                    break
                
                if counts1.get(s2[j], 0) == count2.get(s2[j], 0):
                    curr += 1
                
                if curr == need:
                    return True
        return False


        