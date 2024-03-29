PK     �fU�V�(�
  �
  	   count.txt{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf130
{\fonttbl\f0\fswiss\fcharset0 ArialMT;\f1\fnil\fcharset0 HelveticaNeue;\f2\fnil\fcharset0 Monaco;
}
{\colortbl;\red255\green255\blue255;\red58\green58\blue58;\red254\green254\blue254;\red243\green245\blue246;
\red19\green87\blue199;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}.}{\leveltext\leveltemplateid1\'02\'00.;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid1}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}}
\margl1440\margr1440\vieww14360\viewh11020\viewkind0
\deftab720
\pard\pardeftab720\sl512\sa520\partightenfactor0

\f0\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 In my previous refreshers, which you can access from the series navigation links at the top of this article, I talked about two important Python concepts you need to grasp in order to move forward in your Python learning journey.\'a0\
This tutorial is a continuation of the Python refresher series, and today I will be talking about 
\i Tuples
\i0 .
\b \'a0
\b0 That way, you will have three important concepts in your pocket and will be ready to dig deeper in the Python language.\cb1 \uc0\u8232 \cb3 \
So, let's go ahead and move directly to this interesting topic of 
\i Tuples
\i0 .\
\pard\pardeftab720\sl624\sa520\partightenfactor0

\f1\b\fs52 \cf2 What About Tuples?\
\pard\pardeftab720\sl512\sa520\partightenfactor0

\f0\b0\fs32 \cf2 If you understood 
\i Lists
\i0 , Tuples will be very simple to grasp, because they are similar to Lists except for two main differences:\'a0\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl512\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	1.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Tuples are immutable, so once you create a Tuple, you cannot change its content or even its size, unless you make a copy of that Tuple.\cb1 \
\ls1\ilvl0\cb3 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	2.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 They are written in parentheses 
\f2\fs28 \cb4 ( )
\f0\fs32 \cb3  rather than in square brackets 
\f2\fs28 \cb4 [ ]
\f0\fs32 \cb3 .\'a0\cb1 \
\pard\pardeftab720\sl512\sa520\partightenfactor0
\cf2 \cb3 Thus, as you can guess, Tuples consist of a set of ordered objects which can be of any type (i.e. Strings, Lists, Dictionaries, Tuples, etc.), and are accessed by an 
\i index
\i0 (offset), as opposed to \cf5 \strokec5 Dictionaries\cf2 \strokec2 \'a0where items are accessed by 
\i key
\i0 . It is important to note here that Tuples store 
\i references
\i0  to the objects they contain.}