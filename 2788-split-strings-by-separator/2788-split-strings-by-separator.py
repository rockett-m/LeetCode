class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        out = []
        for w in words:
            fields = w.split(separator)
            out += fields
        return list(filter(None, out))