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
