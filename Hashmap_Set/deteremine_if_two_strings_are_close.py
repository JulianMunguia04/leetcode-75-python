# 1657 Determine if Two Strings are Close, Hashmap

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        dict1 = {}
        dict2 = {}
        frequency1 = []
        frequency2 = []
        chars1 = set()
        chars2 = set()

        if len(word1) != len(word2):
            return False

        for i in range(len(word1)):
            if word1[i] in dict1:
                dict1[word1[i]] += 1
            else:
                dict1[word1[i]] = 1
                chars1.add(word1[i])

            if word2[i] in dict2:
                dict2[word2[i]] += 1
            else:
                dict2[word2[i]] = 1
                chars2.add(word2[i])

        print(dict1, dict2)


        if dict1 == dict2:
            return True

        for key, value in dict1.items():
            frequency1.append(value)
            frequency1.sort()

        for key, value in dict2.items():
            frequency2.append(value)
            frequency2.sort()

        print(dict1, dict2, frequency1, frequency2)
        
        return frequency1 == frequency2 and chars1 == chars2
            
