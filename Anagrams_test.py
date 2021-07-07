import pytest
import Anagrams as Anagram

def test_GetSanitized():
  word = "hola"
  result = "['a', 'h', 'l', 'o']"
  assert Anagram.Sanitize(word) == result

def test_GetSanitizedTest2():
  word = "coro"
  result = "['c', 'o', 'o', 'r']"
  assert Anagram.Sanitize(word) == result