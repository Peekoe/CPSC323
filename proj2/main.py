from enum import Enum

with open('input.txt') as f:
  lines = f.readlines()

class State(Enum):
  # Fail
  Z = -1
  # Start
  S = 0
  E = 1
  Q = 2
  T = 3
  R = 4
  F = 5

#make a list of operators
ops = ['+', '-', '*', '/']

def determine_state(next: str):
  if next in ops[:2]:
    return State.Q
  elif next in ops[2:]:
    return State.R
  elif next in ['a', '(']:
    return State.F
  else:
    return State.E

def invalid(stack):
  print(f'Stack: {stack}')
  print('Output: String is not accepted/invalid.')

def op_state(char):
  if char in ops[:2]:
    return State.E
  elif char in ops[2:]:
    return State.T
  else:
    return State.Z

def is_valid(l: str):
  print(f'Input: {l}')
  if l[0] != '(' or l[0] != 'a':
    print('Stack:[$]')
    print('Output: String is not accepted/invalid.')
    return
  
  stack = []
  state = State.S

  # determine initial state
  if state == State.S:
    if l[0] == '(':
      # go to (E)
      state = State.F
      # remove first paren
      l = l[1:]
    elif l[0] == 'a':
      state = op_state(l[0])
      l = l[1:]
    else:
      invalid(stack)
      return

  stack.push(state)

  for i, char in enumerate(l):
    if char not in ['a', '(', ')', '$'] + ops:
      invalid(stack)
      break

    if state == State.E or state == State.T:
      if char in ops:
        continue

      if char == 'a':
        state.push(state)
        state = op_state()
      elif char == '(':
        state = State.F
      else:

    elif state == State.F:
      stack.push(state)
      state = op_state(state)
    
    if state == State.Z:
      invalid(stack)
      break
  
  print(f'Stack: {stack}')
  print('Output: String is accepted.')


  




for line in lines:
  is_valid(line)
