class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        fields = sentence.split()
        ans = []
        for field in fields:
            result = re.match('(^\$[0-9]+)$', field)
            if result:
                if discount == 100:
                    ans.append('$0.00')
                elif discount == 0:
                    if '.' not in field:
                        ans.append(f'{field}.00')
                else:
                    price = int(field[1:])
                    disc = round((price * discount / 100), 2)
                    subt = round(price - disc, 2)

                    end = str(subt).split('.')[1]
                    if len(end) < 2:
                        ans.append(f'${subt}0')
                    else:
                        ans.append(f'${subt}')

            else:
                ans.append(field)
            
        return ' '.join(ans)