#!/usr/bin/python3
print(''.join('{}'.format(chr(x)) for x in range(97, 123)
              if x not in (101, 113)), end="")
