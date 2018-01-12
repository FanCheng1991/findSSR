# findSSR
find SSR element in genomic sequence

SSR element is defined as a string with more than 6 characters,
  which is composed of several repeatitive units.

A unit is composed of equal or less than 6 character, and all legal letters allowd are A, T, C, G.

Some example:

'AT' is the unit for string 'ATATATAT' with the appearance for four times.
  
'TAG' is the unit for string 'TAGTAGTAG' with the appearance for three times.

findSSR wants to give a solution to tell how many SSR in a given genomic sequence, where are they, what is the unit of each and how many times each unit repeats.
Some optimization in speed may also wish to be achieved.

This repo is dedicated to Xiaoxue Jiang and Yongjian Zhang. Never will I forget those days spent with you in Novogene.