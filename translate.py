#!/usr/bin/python
# coding: utf8
import codecs
from googletrans import Translator

translator = Translator()
d = translator.detect('Wie geht es Ihnen?')

print "이 문장은 한글로 쓰여졌습니"
print d.lang,
translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
for translation in translations:
	print(translation.origin, ' -> ', translation.text.encode('UTF-8'))

a = 'ð€œłĸªßð'
print a
print a.__repr__()
l = [a, a]
print l