class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letrasS = {}
        letrasT = {}
        if len(s) != len(t):
            return False
        for x in range(len(s)):
            if s[x] in letrasS:
                letrasS[s[x]] = letrasS[s[x]] + 1
            else:
                letrasS[s[x]] = 1
            if t[x] in letrasT:
                letrasT[t[x]] = letrasT[t[x]] + 1
            else:
                letrasT[t[x]] = 1
        for letra in letrasS:
            if letra not in letrasT:
                return False

            if letrasS[letra] != letrasT[letra]:
                return False
        return True