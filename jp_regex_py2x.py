# -*- coding: utf-8 -*-
import re

''' This is a library of functions and variables that are helpful to have handy 
	when manipulating Japanese text in python.

	Copyright (c) 2014, Mads Sørensen Ølsgaard
	All rights reserved.
	Released under BSD3 License, see http://opensource.org/licenses/BSD-3-Clause or license.txt '''




# Regular expression unicode blocks collected from http://www.localizingjapan.com/blog/2012/01/20/regular-expressions-for-japanese-text/

hiragana_full = ur'[\u3041-\u3096]'
katakana_full = ur'[\u30A0-\u30FF]'
kanji = ur'[\u3400-\u4DB5\u4E00-\u9FCB\uF900-\uFA6A]'
radicals = ur'[\u2E80-\u2FD5]'
half_width = ur'[\uFF5F-\uFF9F]'
alphanum_full = ur'[\uFF01-\uFF5E]'
symbols_punct = ur'[\x3000-\x303F]'
misc_symbols = ur'[\x31F0-\x31FF\x3220-\x3243\x3280-\x337F]'

def extract_text(unicode_block, string):
	''' extracts and returns all texts from a unicode block from string argument.
		Note that you must use the unicode blocks defined above, or patterns of similar form '''
	return re.sub(ur'[^'+unicode_block[1:], '', string)
