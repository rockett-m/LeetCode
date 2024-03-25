class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        fields = sentence.split()
        ans = []
        for field in fields:
            result = re.match('(^\$[0-9]+)$', field)
            if result:
                # print(int(field[1:]))
                # print(round(int(field[1:]) * discount / 100), 4)
                if discount == 100:
                    ans.append('$0.00')
                elif discount == 0:
                    if '.' not in field:
                        ans.append(f'{field}.00')
                else:
                    price = int(field[1:])
                    disc = round((price * discount / 100), 2)
                    subt = round(price - disc, 2)
                    # print(subt)

                    end = str(subt).split('.')[1]
                    if len(end) < 2:
                        temp = f'${subt}0'
                        ans.append(temp)
                    else:
                        temp = f'${subt}'
                        ans.append(temp)

            else:
                ans.append(field)
            
        return ' '.join(ans)