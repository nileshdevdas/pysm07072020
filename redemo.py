import re
essay = """
i like  are cookies and cookies are mad up of flour and 
cookies taste good and cookies deliver value to calories and quick 
energy
"""
print(re.sub("cookies", "monkeys", essay))
print(re.findall("cookies", essay))