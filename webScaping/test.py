import re

texte = "/watch?v=c65bbIz4FtE&pp=sAQA"


s = '/watch?v=c65bbIz4FtE&pp=sAQA'
result = s[s.find('v=')+2:s.find('&pp')]
print(result)