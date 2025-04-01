pattern = '{3:d}  Model: {1:8s}  MPG: {0:4.1f}   Rate: ${2:.2f}'
print(pattern.format(224/7, 'Echo', 45.6789, 1997))
print(pattern.format(137/14, 'Escalade', 99.1234, 2005))