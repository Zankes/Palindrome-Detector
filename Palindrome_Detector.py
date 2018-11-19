string = "a but tuba"

def p_s(str):
  new_str = str.replace(" ", "")
  if len(new_str) == 1 or len(new_str) == 0:
    return True
  if new_str[0] == new_str[-1]:
    return p_s(new_str[1:-1])
  else:
    return False

print(p_s(string))