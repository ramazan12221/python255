import re
s = "В июле 2021 год, 02.06.2021, 05.06.2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков"
reg = r''
print(re.findall(reg, s))