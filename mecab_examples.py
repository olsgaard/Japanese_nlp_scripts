# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 15:46:44 2014

@author: Mads Olsgaard, 2014

Released under BSD License

This script is a reference for mecab python bindings usage.

* For installing mecab python bindings, see https://github.com/SamuraiT/mecab-python3
* For using MeCab, see http://mecab.googlecode.com/svn/trunk/mecab/doc/index.html

"""

import MeCab as mecab # I prefer to work with lower-case
text ="窓際のトットちゃん。Chapter1: 自由が丘の駅で、大井町線から降りると、ママは、トットちゃんの手を引っ張って、改札口を出ようとした。トットちゃんは、それまで、あまり電車に乗ったことがなかったから、大切に握っていた切符をあげちゃうのは、もったいないなと思った。"
print("Original text:", text)
print('-'*40)

print("Convert readings to katakana")

m = mecab.Tagger("-Oyomi")
print("\nParsing with -Oyomi")
print( m.parse(text))


print("POS tagging")

m = mecab.Tagger("-Ochasen")
print("\nParsing with -Ochasen")
print( m.parse(text))


print("Tokenize text")

m = mecab.Tagger("-O wakati")
print("\nParsing with -O wakati")
print( m.parse(text))
