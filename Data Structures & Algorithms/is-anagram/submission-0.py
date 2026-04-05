class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
                word1 = {}
                word2 = {}
                for i in range (len(s)):
                    if word1.get(s[i]):
                        word1[s[i]]+=1 
                    else:
                        word1[s[i]] = 1
                for i in range (len(t)):
                    if word2.get(t[i]):
                        word2[t[i]]+=1 
                    else:
                        word2[t[i]] = 1

                if word1 == word2:
                    return True
                else:
                    return False