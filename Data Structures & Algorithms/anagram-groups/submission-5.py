from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupos = {}

        for palabra in strs:
            clave = tuple(sorted(palabra))

            if clave not in grupos:
                grupos[clave] = []

            grupos[clave].append(palabra)

        return list(grupos.values())