parsingTable = {
  'E': { 'a': 'TQ', '(': 'TQ' },
  'Q': { '+': '+TQ', '-': '-TQ', ')': '', '$': '' },
  'T': { 'a': 'FR', '(': 'FR' },
  'R': {
    '+': '',
    '-': '',
    '*': '*FR',
    '/': '/FR',
    ')': '',
    '$': ''
  },
  'F': { 'a': 'a', '(': '(E)' }
}


def main(string):
  stack = "E$"

  if string[0] != "a" and string[0] != "(":
    print("Stack:", str(list(stack[::-1])))
    print('Output: String is not accepted/invalid.')
    return

  while len(stack) > 1:
    print(f'Input: {string}')
    print("Stack:", str(list(stack[::-1])))
    if stack[0] == string[0]:
      string = string[1:]
      stack = stack[1:]
    else:
      # replace top of stack with production rule
      first = parsingTable.get(stack[0], None)
      second = first.get(string[0], None)

      if second is not None:
        stack = second + stack[1:]
      else:
        print('Output: String is not accepted/invalid.')
        return

  if string == stack:
    print(f"Input: {string}")
    print("Stack:", str(list(stack[::-1])))
    print('Output: String is accepted.')
  
if __name__ == "__main__":
  test_cases = ["(a+a)*a$", "a*(a/a)$", "a(a+a)$"]
  for test_case in test_cases:
    main(test_case)
    print("\n\n")
