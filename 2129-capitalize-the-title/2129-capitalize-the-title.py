class Solution:
    def capitalizeTitle(self, title: str) -> str:
        fields = title.split(' ')
        out = []
        for field in fields:
            if len(field) < 3:
                out.append(field.lower())
            else:
                res = field[0].upper() + field[1:].lower()
                out.append(res)

        return ' '.join(out)