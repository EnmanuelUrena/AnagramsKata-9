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

def test_AreAnagrams_ReturnTrue():
  word1 = "romo"
  word2 = "moro"
  Anagram.Check(word1)
  assert Anagram.Check(word2) == True

def test_AreNotAnagrams_ReturnFalse():
  word1 = "pedro"
  word2 = "papa"
  Anagram.Check(word1)
  assert Anagram.Check(word2) == False
