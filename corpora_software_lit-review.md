# Software

## MeCab

MeCab [1] is a part-of-speech and morphological analyzer for Japanese, development is maintained by *Kyoto University's Department of Information Science* in collaboration with *NTT Basic Sciences Research Department *[2], developed primarily by Taku Kudo [3] who is also responsible for the (active) github repository.

It appears to be mainly a faster version of Chasen, with some sources (none that are quotable!) saying the project started its life as a fork (or at least under a name containing) chasen.

MeCab is a open source command-line application with bindings to popular languages such as perl and python. It is written in C/C++.

### links:

1. [https://github.com/taku910/mecab](https://github.com/taku910/mecab) / [http://taku910.github.io/mecab/](http://taku910.github.io/mecab/) 
(old: [http://mecab.googlecode.com/svn/trunk/mecab/doc/index.html](http://mecab.googlecode.com/svn/trunk/mecab/doc/index.html))

2. [http://nlp.ist.i.kyoto-u.ac.jp/kuntt](http://nlp.ist.i.kyoto-u.ac.jp/kuntt/)

3. [http://chasen.org/~taku](http://chasen.org/~taku/)

### Related papers:

* Applying Conditional Random Fields to Japanese Morphological Analysis [[PDF](http://chasen.org/%7Etaku/publications/emnlp2004-2.pdf)] [[PPT (slide)](http://chasen.org/%7Etaku/publications/emnlp2004-2-slide.ppt)] 
Notes from slides:

    * "Standard testbed corpus used for Japanese morphological analysis" [??]

    * Chinese segmentation and new word detection using conditional random fields [[pdf]](http://dl.acm.org/citation.cfm?id=1220436)

### Software comparison

<table>
  <tr>
    <td></td>
    <td>MeCab</td>
    <td>ChaSen</td>
    <td>JUMAN</td>
    <td>KAKASI</td>
  </tr>
  <tr>
    <td>Analysis model</td>
    <td>bi-gram Markov model</td>
    <td>Variable length Markov model</td>
    <td>bi-gram Markov model</td>
    <td>Longest match</td>
  </tr>
  <tr>
    <td>Cost Estimation</td>
    <td>Learning from the corpus</td>
    <td>Learning from the corpus</td>
    <td>Manpower</td>
    <td>No concept of cost</td>
  </tr>
  <tr>
    <td>Learning model</td>
    <td>CRF (identification model)</td>
    <td>HMM (generation model)</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Dictionary lookup algorithm</td>
    <td>Double Array</td>
    <td>Double Array</td>
    <td>Patricia tree</td>
    <td>Hash?</td>
  </tr>
  <tr>
    <td>Solution search algorithm</td>
    <td>Viterbi</td>
    <td>Viterbi</td>
    <td>Viterbi</td>
    <td>Decisive?</td>
  </tr>
  <tr>
    <td>Implementation of the connecting table</td>
    <td>Two-dimensional Table</td>
    <td>Automaton</td>
    <td>Two-dimensional Table?</td>
    <td>Without connecting table?</td>
  </tr>
  <tr>
    <td>Hierarchy of the part of speech</td>
    <td>Unlimited multi-tier part of speech</td>
    <td>Unlimited multi-tier part of speech</td>
    <td>Two-stage fixed</td>
    <td>No concept of part of speech?</td>
  </tr>
  <tr>
    <td>Unknown word processing</td>
    <td>Character types (can change the behavior definition)</td>
    <td>Character types (unmodifiable)</td>
    <td>Character types (unmodifiable)</td>
    <td></td>
  </tr>
  <tr>
    <td>Constrained analysis</td>
    <td>Possible</td>
    <td>2.4.0 possible</td>
    <td>Impossible</td>
    <td>Impossible</td>
  </tr>
  <tr>
    <td>N-best solution</td>
    <td>Possible</td>
    <td>Impossible</td>
    <td>Impossible</td>
    <td>Impossible</td>
  </tr>
</table>


## KyTea

KyTea (pronounced Cutie) is a Morphological Analyser developed by Kyoto University in 2009, it uses a pointwise classifier-based (SVM or logistic regression) approach, allowing for training on partially annotated training data. Main developer is Graham Neubig [[website](http://www.phontron.com/index.php)]

### links:

* [http://www.phontron.com/kytea/](http://www.phontron.com/kytea/) 

* [https://github.com/neubig/kytea](https://github.com/neubig/kytea) 

### Related papers:

* Graham Neubig, Yosuke Nakata, Shinsuke Mori, [Pointwise Prediction for Robust, Adaptable Japanese Morphological Analysis,](http://www.phontron.com/paper/neubig11aclshort.pdf) The 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies (ACL-HLT). Portland, Oregon, USA. June 2011

* Graham Neubig, Shinsuke Mori. [Word-based Partial Annotation for Efficient Corpus Construction,](http://www.phontron.com/paper/neubig-lrec2010.pdf) The seventh international conference on Language Resources and Evaluation (LREC 2010). Malta. May 2010.

* Mori, Shinsuke, et al. "*Pointwise Prediction and Sequence-based Reranking for Adaptable Part-of-Speech Tagging.*" ( Pacific Association for Computational Linguistics 2015).[[pdf](http://plata.ar.media.kyoto-u.ac.jp/mori/research/public/PACLING15.pdf)]

    * Claims to beat both Chasen (referred to only as HMM) and MeCab (referred to by name and CRF approaches)

    * Uses partial annotated and fully annotated corpora

    * Annotated corpora is BCCWJ, with the Yahoo section as test and rest as training

    * Uses only 21 "coarse" tags (universal pos tagset?)

        * This will give it an edge over vanilla MeCab, which uses over 50)

    * First paper (or place) I've seen mention KyTea, a newer-than-MeCab morphology analyser.

### Dictionaries / models

* Main distribution uses BCCWJ and Unidic, but can be extended with several others listed on the website. [http://www.phontron.com/kytea/train.html](http://www.phontron.com/kytea/train.html) 

## Kurumoji

[Kagome](https://github.com/ikawaha/kagome) appears to be a Go version of Kurumoji.

Java program licensed under Apache and compatible with MeCab dictionaries maintained by Atilika. Optimized for searching. A bit unclear which algorithm it use, but appears to be an FST.

It is used in a sizeable amount of research, though I can't find any papers detailing its approach, nor comparing its performance with other models.

### links:

* [http://atilika.com/en/](http://atilika.com/en/)

* [http://atilika.com/en/products/kuromoji.html](http://atilika.com/en/products/kuromoji.html) 

* [https://github.com/atilika/kuromoji](https://github.com/atilika/kuromoji) 

# Dictionaries

MeCab can be compiled using 1 of 3 freely (as in beer) dictionaries. These dictionaries are already compiled and consist of 1 or more .csv files with word and morpheme definitions as well as between 7-9 .def files containing large numerical matrix (matrix.def) or rewrite rules or other seemingly grammatical rules.

There exist a host of other online available MeCab formatted dictionaries and most modern JMA are compatible with MeCab dictionaries.

## Tagsets and other related resources

Resources related to tagsets

* List of postags generated by Juman and Chasen

    * [http://www.unixuser.org/~euske/doc/postag/](http://www.unixuser.org/~euske/doc/postag/)

* VE - Ruby library that can re-segment Japanese into more "normal" segmentations

    * [https://github.com/Kimtaro/ve/blob/master/lib/providers/mecab_ipadic.rb#L118](https://github.com/Kimtaro/ve/blob/master/lib/providers/mecab_ipadic.rb#L118) 

* Python parser for EDICT files (unmaintained)

    * [http://repo.or.cz/w/jbparse.git/blame/8e42831ca5f721c0320b27d7d83cb553d6e9c68f:/jbparse/edict.py](http://repo.or.cz/w/jbparse.git/blame/8e42831ca5f721c0320b27d7d83cb553d6e9c68f:/jbparse/edict.py) 

## IPA dictionary (mecab-ipadic-2.7.0-20070801.tar.gz)

* IPA dictionary, based on the IPA corpus[ ](https://translate.googleusercontent.com/translate_c?act=url&depth=1&hl=ja&ie=UTF8&prev=_t&rurl=translate.google.com&sl=ja&tl=en&u=http://www.cis.upenn.edu/%7Epereira/papers/crf.pdf&usg=ALkJrhgWgNFYYCokxikFqW2acMCzLH6siw)**(Recommended)**[ Download](https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM)

* **Authors:** 	Taku Kudo <[taku@chasen.org](mailto:taku@chasen.org)> [chasen@is.aist-nara.ac.jp](mailto:chasen@is.aist-nara.ac.jp)

Masayuki Asahara:[masayu-a@is.aist-nara.ac.jp](mailto:masayu-a@is.aist-nara.ac.jp)

Yuji Matsumoto:[matsu@is.aist-nara.ac.jp](mailto:matsu@is.aist-nara.ac.jp) 

### About IPA Dictionary

* **Maintainer**: The Information-technology Promotion Agency of Japan ([IPA](https://www.ipa.go.jp/index-e.html))

* **Papers**:

    * ipadic version 2.7.0 Userâ€™s Manual [[pdf](https://osdn.jp/projects/ipadic/docs/ipadic-2.7.0-manual-en.pdf/en/1/ipadic-2.7.0-manual-en.pdf.pdf)] (for chuman)

IPAdic is the recommended dictionary for MeCab. While the IPA are credited with the source of this dictionary, their website indicates absolutely no relevance to NLP in any form. It also appears (according to the manual, linked above) that the original MeCab used a different (and equally elusive) source, the [RWCP](http://keima.la.coocan.jp/rwcp/10years/index.html) as well as the Kyoto Corpus (Juman, below), that uses Mainichi Shinbun as the text corpora, which is available for ~100-200.000 yen.

## Juman dictionary (mecab-jumandic-7.0-20130310.tar.gz)

* Juman dictionary, based on the Kyoto corpus.[ Download](https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7X2pESGlLREpxdXM)

* **Author:** Taku Kudo <[taku@chasen.org](mailto:taku@chasen.org)>

### About the Kyoto Corpus

* **Maintainer: **[http://nlp.ist.i.kyoto-u.ac.jp/EN/index.php?Kyoto%20University%20Text%20Corpus](http://nlp.ist.i.kyoto-u.ac.jp/EN/index.php?Kyoto%20University%20Text%20Corpus) 

* **Papers**:

    * Building a Japanese parsed corpus while improving the parsing system [[pdf]](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.55.4086&rep=rep1&type=pdf)

The annotations from the Kyoto Corpus are available freely from the above link, the actual text is not, and must be purchased from [Mainichi Shinbun for ~100-200.000 yen](http://www.nichigai.co.jp/sales/mainichi/mainichi-data.html)

## Unidic dictionary (unidic-mecab-2.1.2_src.zip or unidic-MLJ_14.zip)

* Unidic dictionary, based on the BCCWJ corpus.

    * [Download unidic-mecab-2.1.2_src.zip](http://sourceforge.jp/frs/redir.php?m=iij&f=%2Funidic%2F58338%2Funidic-mecab-2.1.2_src.zip) (via [y-ken](http://qiita.com/y-ken/items/ca3a6f7d7c79fdbe703e)) 

    * [Download unidic-MLJ_14.zip](http://www2.ninjal.ac.jp/lrc/index.php?UniDic%2F%B6%E1%C2%E5%CA%B8%B8%ECUniDic#gacaeebe) (via ninjal (seemingly official))

* **Author: **The UniDic Consortium 

    * [https://osdn.jp/projects/unidic/](https://osdn.jp/projects/unidic/)

    * [http://www2.ninjal.ac.jp/lrc/index.php?UniDic](http://www2.ninjal.ac.jp/lrc/index.php?UniDic) (seems to be more organizational )

### About the Balanced Corpus of Contemporary Written Japanese (BCCWJ)

* **Maintainer**: The National Institute for Japanese Language ([NINJAL](http://www.ninjal.ac.jp/english/products/bccwj/))

    * [http://pj.ninjal.ac.jp/corpus_center/](http://pj.ninjal.ac.jp/corpus_center/) Center for Corpus Development, NINJAL.  Appears to be the home of all corpus, including UniDic and BCCWJ and several other corpora.

* **Papers**:

    * NINJAL publications: [[link]](http://www.ninjal.ac.jp/english/publication/papers/)

    * KOTONOHA and BCCWJ: Development of a Balanced Corpus of Contemporary Written Japanese, 2007 [[PDF]](http://www.researchgate.net/profile/Kikuo_Maekawa/publication/228882062_KOTONOHA_and_BCCWJ_Development_of_a_Balanced_Corpus_of_Contemporary_Written_Japanese/links/53f6ed240cf2888a749757e2.pdf)

    * Design of a balanced corpus of contemporary written Japanese, 2007 [[pdf]](http://www2.ninjal.ac.jp/kikuo/LKR2007KM.pdf)

    * UniDic for Early Middle Japanese: a Dictionary for Morphological Analysis of Classical Japanese, 2012.[ [pdf]](http://www.researchgate.net/profile/Yasuharu_Den/publication/237145429_UniDic_for_Early_Middle_Japanese_a_Dictionary_for_Morphological_Analysis_of_Classical_Japanese/links/00b7d51b92a5b7fabd000000.pdf)

    * Corpus-based Japanese morphological analysis (unidic; doctor's thesis), 2003[ [pdf]](http://www.researchgate.net/profile/Masayuki_Asahara/publication/26982976_Corpus-based_Japanese_morphological_analysis/links/5440f2000cf251bced61581d.pdf)

    * A Proper Approach to Japanese Morphological Analysis: Dictionary, Model, and Evaluation (UniDic), 2008.[ [pdf]](http://lrec-conf.org/proceedings/lrec2008/pdf/258_paper.pdf)

    * Balanced Corpus of contemporary written Japanese (the BCCWJ paper?), 2008. [[pdf](http://download.springer.com/static/pdf/23/art%253A10.1007%252Fs10579-013-9261-0.pdf?originUrl=http%3A%2F%2Flink.springer.com%2Farticle%2F10.1007%2Fs10579-013-9261-0&token2=exp=1440673974~acl=%2Fstatic%2Fpdf%2F23%2Fart%25253A10.1007%25252Fs10579-013-9261-0.pdf%3ForiginUrl%3Dhttp%253A%252F%252Flink.springer.com%252Farticle%252F10.1007%252Fs10579-013-9261-0*~hmac=9d1355bc95a6c66d37b431cbc38a81e7988a83a8e2cf6f6d0b19fdf835c92701)]

* **Links**

    * **[http://pj.ninjal.ac.jp/corpus_center/bccwj/en**/](http://pj.ninjal.ac.jp/corpus_center/bccwj/en/)

The BCCWJ Corpus is available for purchase for between [50.000 - 400.000 yen for a yearly license](http://pj.ninjal.ac.jp/corpus_center/bccwj/subscription.html).

It is fully annotated and contains a mix of newspaper, journal and internet articles.

The corpus can be manually queried free of charge via either the *Shonagon* or *Chunagon* (registration required) service. There doesn't appear to exist an API.

* Shonagon: [http://www.kotonoha.gr.jp/shonagon/](http://www.kotonoha.gr.jp/shonagon/) 

* Chunagon: [https://chunagon.ninjal.ac.jp/](https://chunagon.ninjal.ac.jp/) 

## Other corpora

* EDR Electronic Dictionary Technical Guide (1993) , Japan Electronic Dictionary Research Institute, Ltd [[1995 version; ACM link](http://dl.acm.org/citation.cfm?id=219752)][[pdf](https://drive.google.com/open?id=0B6Lm5plY0ct0QUU5RUQ5ZEJ0dnc)]

    * Via Mori et. al 2015 [[pdf](http://plata.ar.media.kyoto-u.ac.jp/mori/research/public/PACLING15.pdf)] "*... many fully annotated corpora, in which the sentences are divided into words completely and all the words are annotated with POSs, are available. Almost all annotated corpora produced through corpus annotation research [EDR], [17] fall in this category.*"

    * Large Japanese/English word-sense dictionary combined with Japanese and English corpora.

* Tsukuba Web Corpus (online only)

    * [http://nlt.tsukuba.lagoinst.info/search/](http://nlt.tsukuba.lagoinst.info/search/) 

* Neologd - Neogolism Dictionary for ipadic

    * An extension to IPAdic which includes many neologisms (new word), that have been extracted from "many language resources on the Web". Exact method is a bit uncertain.

    * Has monthly updates.

    * [https://github.com/neologd/mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd) 

# Other papers / approaches:

* Yasuharu Den, Toshinobu Ogiso, Hideki Ogura, Atsushi Yamada, Nobuaki Minematsu, Kiyotaka Uchimoto, and Hanae Koiso. 2007. *The development of an electronic dictionary for morphological analysis and its application to Japanese corpus linguistics* (in Japanese). Japanese Linguistics, 22:101â€“123 (via A proper approach to Japanese morphological analysis: Dictionary, model, and evaluation)

* Santos, Cicero D., and Bianca Zadrozny. "Learning character-level representations for part-of-speech tagging." *Proceedings of the 31st International Conference on Machine Learning (ICML-14)*. 2014. [[pdf](http://machinelearning.wustl.edu/mlpapers/paper_files/icml2014c2_santos14.pdf)]

* Accurate Word Segmentation and POS Tagging for Japanese Microblogs: Corpus Annotation and Joint Modeling with Lexical Normalization, 2014 [[pdf](http://emnlp2014.org/papers/pdf/EMNLP2014011.pdf)]

    * POS tagging twitter

    * build a twitter corpus of 1000 posts, 1831 sentences all manually segmented and annotated with POS.

## Problem with dictionaries - compiling from source

It is unclear how *any* of these dictionaries are compiled. They are all compiled for MeCab, and they seemingly contain a lot of statistical information (particularly matrix.def, but all .csv files contain 3 large numbers per entry) and without a way to recompile dictionaries from source, there seems to be little chance at improving on MeCab.

It does however appear that unidic is the most open of the 3.

One can ask for source dictionary by email to [kindai-corpus@ninjal.ac.jp](mailto:kindai-corpus@ninjal.ac.jp) 
