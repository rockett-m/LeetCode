class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        my_dict = OrderedDict()
        for cpd in cpdomains:
            num, domain = cpd.split(' ')
            num = int(num)
            fields = domain.split('.')
            for idx, field in enumerate(fields):
                
                key = '.'.join(fields[idx:])
                if key in my_dict.keys():
                    my_dict[key] += num
                
                else:
                    my_dict[key] = num


        print(my_dict.items())
        out = []
        for k,v in my_dict.items():
            item = f'{v} {k}'
            out.append(item)
        return out