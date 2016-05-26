''' This is a quick script to make good hiragana <-> katakana transliteration in just
	4 lines of python.

	If you don't need romaji translitteration and want to lower your scripts dependencies you can
	forgo pip installing some surprisingly large libraries just to convert from hiraganan to katakana
	and simply copy paste the below 4 lines (and preferrably a link to my homepage or github) and you
	are good to go.

	Tested in Python 3.x, doesn't seem to work in Python 2.7

	Copyright (c) 2016, Mads Sørensen Ølsgaard, olsgaard.dk

	All rights reserved.
	Released under BSD3 License, see http://opensource.org/licenses/BSD-3-Clause or license.txt '''


#################################################
## Make hiragana<->katakana translation tables ##
#################################################

# These lists don't contain all legal hiragana and katakana characters (as defined in unicode), 
# but only the once we want to translate between. Characters that don't have a 1-1 transliteration are simply skipped

katakana_chart = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"
hiragana_chart = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ"
hir2kat = str.maketrans(hiragana_chart, katakana_chart)
kat2hir  =str.maketrans(katakana_chart, hiragana_chart)

####################
##### Examples #####
####################

# With the 4 lines defining our translations tables we can now easily translate between hiragana and katakana
mixed = 'きゃりーぱみゅぱみゅは日本の歌手です。'
print(mixed.translate(hir2kat))
# out: キャリーパミュパミュハ日本ノ歌手デス。

# translating back to hiragana gives us the expected result, because we didn't add every katakana and hiragana code block to the translation charts
print(mixed.translate(hir2kat).translate(kat2hir))
# out: きゃりーぱみゅぱみゅは日本の歌手です。