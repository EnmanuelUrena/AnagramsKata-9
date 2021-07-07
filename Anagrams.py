def Sanitize(word):
  return str(sorted(word))

dic = {}

def Check(word):
  key = Sanitize(word)
  match = key in dic
  if not match:
    dic.setdefault(key, [])
  dic[key].append(word)
  return match


def count():
    count = 0
    for key, value in dic.items():
        if len(value) > 1:
            count += 1
    return count
