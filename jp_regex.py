# -*- coding: utf-8 -*-
import re

''' This is a library of functions and variables that are helpful to have handy 
	when manipulating Japanese text in python.
	This is optimized for Python 3.x, and takes advantage of the fact that all strings are unicode.

	Copyright (c) 2014-2015, Mads Sørensen Ølsgaard
	All rights reserved.
	Released under BSD3 License, see http://opensource.org/licenses/BSD-3-Clause or license.txt '''




## UNICODE BLOCKS ##

# Regular expression unicode blocks collected from 
# http://www.localizingjapan.com/blog/2012/01/20/regular-expressions-for-japanese-text/

hiragana_full = r'[ぁ-ゟ]'
katakana_full = r'[゠-ヿ]'
kanji = r'[㐀-䶵一-鿋豈-頻]'
radicals = r'[⺀-⿕]'
katakana_half_width = r'[｟-ﾟ]'
alphanum_full = r'[！-～]'
symbols_punct = r'[、-〿]'
misc_symbols = r'[ㇰ-ㇿ㈠-㉃㊀-㋾㌀-㍿]'
ascii_char = r'[ -~]'

## FUNCTIONS ##

def extract_unicode_block(unicode_block, string):
	''' extracts and returns all texts from a unicode block from string argument.
		Note that you must use the unicode blocks defined above, or patterns of similar form '''
	return re.findall( unicode_block, string)

def remove_unicode_block(unicode_block, string):
	''' removes all chaacters from a unicode block and returns all remaining texts from string argument.
		Note that you must use the unicode blocks defined above, or patterns of similar form '''
	return re.sub( unicode_block, '', string)

## EXAMPLES ## 

text = '初めての駅 自由が丘の駅で、大井町線から降りると、ママは、トットちゃんの手を引っ張って、改札口を出ようとした。ぁゟ゠ヿ㐀䶵一鿋豈頻⺀⿕｟ﾟabc！～、〿ㇰㇿ㈠㉃㊀㋾㌀㍿'

print('Original text string:', text, '\n')
print('All kanji removed:', remove_unicode_block(kanji, text))
print('All hiragana in text:', ''.join(extract_unicode_block(hiragana_full, text)))





