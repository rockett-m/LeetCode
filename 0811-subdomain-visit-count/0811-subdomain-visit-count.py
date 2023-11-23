class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        my_dict = OrderedDict()
        for cpd in cpdomains:
            num, domain = cpd.split(' ')
            fields = domain.split('.')
            for idx, field in enumerate(fields):
                
                key = '.'.join(fields[idx:])
                if key in my_dict.keys():
                    my_dict[key] += int(num)
                else:
                    my_dict[key] = int(num)

        out = []
        for k,v in my_dict.items():
            out.append(f'{v} {k}')
        return out