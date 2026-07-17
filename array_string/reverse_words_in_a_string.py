# 151 Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        
        word = ""
        words= []
        reversed_string = ""

        s+= " "
        
        for char in s:
            print(char)
            if char == " ":
                if not word == "":
                    words.append(word)
                word = ""
            else:
                word += char

        print(words)
        
        i = 0
        length = len(words)-1
        
        for item in reversed(words):
            
            reversed_string += item
            if not i == length:
                reversed_string += " "
            i += 1

        return reversed_string
        
# 