

x = 12.23456
commaposition = 4
cut_var, _ = str(x).split(".")
cut_var_length = len(cut_var)

print(cut_var_length)

x = float(str(x)[:commaposition + cut_var_length + 1])

print(x)