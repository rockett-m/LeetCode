class Solution:
    def validStrings(self, n: int) -> List[str]:

        def generate_bins(bny: str):

            # done
            if len(bny) >= n:
                bins.append(bny)
                return 

            # '1' always safe
            generate_bins(f'{bny}1')

            # '0' if empty str or prev == '1'
            if len(bny) == 0:
                generate_bins(f'{bny}0')
            elif len(bny) > 0 and bny[-1] == '1':
                generate_bins(f'{bny}0')

        bins = []
        generate_bins(bny='')
        return bins
