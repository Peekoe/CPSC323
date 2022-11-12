KEYWORDS = set(['while', 'if', 'else', 'int', 'float', 'char', 'double', 'return', 'void', 'main'])
SYMBOLS = set([';', ','])
OPERATORS = set(['+', '-', '*', '/', '=', '<', '>'])
SEPARATORS = set(['(', ')'])


def main():
  with open('input_scode.txt', 'r') as f:
    code = f.read()

  current = ''

  for char in code:
    if is_not_special(char):
      current += char
      continue
    
    if len(current) > 0:
      if is_keyword(current):
        print_token('keyword', current)
      elif is_int(current):
        print_token('int', current)
      elif is_float(current):
        print_token('float', current)
      else:
        print_token('id', current)

      if is_operator(char):
        print_token('operator', char)
      elif is_separator(current):
        print_token('separator', char)
      else:
        print_token('symbol', char)
      current = ''


def print_token(type, current):
  print(f'{type.strip():<10} | {current.strip():<10}')


def is_not_special(char: str) -> bool:
  return char.strip() not in (SYMBOLS.union(SEPARATORS).union(OPERATORS))


def is_keyword(token: str) -> bool:
  return token.strip() in KEYWORDS


def is_operator(token: str) -> bool:
  return token.strip() in OPERATORS


def is_separator(token: str) -> bool:
  return token.strip() in SEPARATORS


def is_int(token: str) -> bool:
  d = set([0,1,2,3,4,5,6,7,8,9])
  # 1 is any int, 2 is strictly 0
  acceptingStates = [1, 2]
  state = 0

  if token[0] == 0:
    state = 2

  for char in token[1:]:
    if char in d:
      # self loop
      state = 1
    else:
      # if input is not num, send to dead state
      state = -1

  return state in acceptingStates


def is_float(token: str) -> bool:
  try:
    float(token)
    return True
  except ValueError:
    return False


if __name__ == '__main__':
  main()
