import re

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_content = dict()
        dup_files = []
        
        for path in paths:
            root = path.split()[0]
            
            for data in path.split()[1:]:
                result = re.match(r'(.+)\((.+)\)', data)
                if result:
                    filename = result.group(1)
                    content = result.group(2)
                    full_path = f'{root}/{filename}'
                    if content not in file_content.keys():
                        file_content[content] = []
                    file_content[content].append(full_path)
        
        for files in file_content.values():
            if len(files) > 1:
                dup_files.append(files)
                    
        return dup_files
                
                    
        