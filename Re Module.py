string = "hilarious"
print(string[0:4])
print(string[0:])
print(string[4:])

import re
print(dir(re))

string = "The night was cold and dark"
p = re.search("cold", string)
print(p)
start = p.start()
end = start + 4
print(start)
print(end)
print(string[start:end])

string2 = "asclsakdfhkjsadfhwkjadhfas Cheese caskdjalksdj aksdj Cakejakshdkasjhd akjch Pizza"
n = re.search("Cheese", string2)
print(n.start())
print(n.end())
print(string2[n.start():n.end()])

