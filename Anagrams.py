import time

def read_file(path):
  with open(path) as f:
    for l in f:
      Check(l.rstrip("\n"))

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

if __name__ == "__main__":
  start_time = time.time()
  read_file("wordlist.txt")

  result = ""

  for key, value in dic.items():
    if len(value) > 1:
      result += str(value) + "\n"

print(result)
end_time = time.time()
print(end_time - start_time)
