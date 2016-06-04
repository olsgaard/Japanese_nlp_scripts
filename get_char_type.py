#	Function to determine the character class of a single character in a Japanes text.
#	Distinguishes between 6 classes, OTHER, ROMAJI, HIRAGANA, KATAKANA, DIGIT, KANJI
#
#	These classes can be useful as features in a machine learning classifier.
#	 
#
#	* Copyright (c) 2016, Mads Sørensen Ølsgaard
#	* All rights reserved.
#
#	* Adapted from KyTea, https://github.com/neubig/kytea/blob/master/src/lib/string-util.cpp
#	* Copyright 2009, KyTea Development Team
#	* 
#	* Licensed under the Apache License, Version 2.0 (the "License");
#	* you may not use this file except in compliance with the License.
#	* You may obtain a copy of the License at
#	* 
#	*	http://www.apache.org/licenses/LICENSE-2.0

def get_char_type(c):
	# find the type of a unicode character
	# Adapted from KyTea

	OTHER, ROMAJI, HIRAGANA, KATAKANA, DIGIT, KANJI = 'O', 'R', 'H', 'K', 'D', 'k'
	
	if(len(c) == 0):
		return OTHER;
	val = ord(c)

	# Basic latin uppercase, basic latin lowercase
	# Full width uppercase, full width lowercase
	if (0x41 <= val <= 0x5A) or (0x61 <= val <= 0x7A) or (0xFF21 <= val <= 0xFF3A) or (0xFF41 < val < 0xFF5A):
		return ROMAJI;

	# hiragana (exclude repetition characters)
	if (0x3040 <= val <= 0x3096):
		return HIRAGANA

	# full width (exclude center dot), half width
	if (0x30A0 <= val <= 0x30FF and val != 0x30FB) or (0xFF66 <= val <= 0xFF9F):
		return KATAKANA

	# basic latin digits
	if (0x30 <= val <= 0x39) or (0xFF10 <= val <= 0xFF19):
		return DIGIT;

	# CJK Unified Ideographs
	if ((0x3400 <= val <= 0x4DBF)  # CJK Unified Ideographs Extension A
		   or (0x4E00 <= val <= 0x9FFF) # CJK Unified Ideographs
		   or (0xF900 <= val <= 0xFAFF) # CJK Compatibility Ideographs
			#|| (0x1F200 <= val <= 0x1F2FF) # Enclosed Ideographic Supplement
		   or (0x20000 <= val <= 0x2A6DF) # CJK Unified Ideographs Extension B
		   or (0x2A700 <= val <= 0x2B73F) # CJK Unified Ideographs Extension C
		   or (0x2B740 <= val <= 0x2B81F) # CJK Unified Ideographs Extension D
		   or (0x2F800 <= val <= 0x2FA1F)): # CJK Compatibility Ideographs Supplement
		return KANJI
	return OTHER

if __name__=="__main__":
	text = '初めての駅 自由が丘の駅で、大井町線から降りると、ママは、トットちゃんの手を引っ張って、改札口を出ようとした。'
	print('original text:\t', text)
	print('character classes:\t', ''.join([get_char_type(c) for c in text]))