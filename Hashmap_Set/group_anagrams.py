# 49 Group  Anagrams, Hashmap

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        h = {}
        l = []

        for s in strs:
            sorted_text = "".join(sorted(s))

            if sorted_text in h:
                h[sorted_text].append(s)
            else:
                h[sorted_text] = [s]

        for value in h.values():
            l.append(value)
            
        return l