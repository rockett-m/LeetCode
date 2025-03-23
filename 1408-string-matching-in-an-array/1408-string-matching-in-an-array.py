class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        out = set()
        for idx, word in enumerate(words):
            for ix, w in enumerate(words):
                if idx == ix: continue
                if w in word:
                # if re.search(w, word):
                    out.add(w)

        return list(out)