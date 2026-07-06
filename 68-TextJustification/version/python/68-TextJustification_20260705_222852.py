# Last updated: 7/5/2026, 10:28:52 PM
1class Solution:
2    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
3        # implementation simulation heavy question involving arrays and strings and addition. 
4        ans = []
5        currlinelength = 0 # of a line
6        linewords = []
7        sentence = ""
8        for i in range(len(words)):
9            print(words[i], linewords, ans)
10
11            # if one word but too long
12            if currlinelength + len(words[i]) + len(linewords) > maxWidth and len(linewords) == 1:
13                sentence = linewords[0] + " " * (maxWidth - len(linewords[0]))
14                ans.append(sentence)
15                linewords = []
16                currlinelength = 0
17            
18            # if in middle and not last and more than oen word
19            elif len(linewords) > 1 and currlinelength + len(linewords) + len(words[i])> maxWidth:
20                amountofwords = len(linewords)
21                spacesinbetween = (maxWidth - currlinelength) // (amountofwords-1)
22                extraspace = (maxWidth - currlinelength) % (amountofwords-1)
23                sentence = ""
24                for j in range(len(linewords)):
25                    sentence += linewords[j]
26                    if j != len(linewords) - 1:
27                        sentence += " "  * spacesinbetween
28                        if extraspace > 0:
29                            extraspace -= 1
30                            sentence += " "
31                ans.append(sentence)
32                linewords = []
33                currlinelength = 0
34
35
36            currlinelength += len(words[i])
37            linewords.append(words[i])
38            
39        
40        # if last line, then left justify
41        if i == len(words) - 1:
42            amountofwords = len(linewords)
43            sentence = ""
44            for i in range(amountofwords):
45                sentence += linewords[i]
46                if i != len(linewords) - 1:
47                    sentence += " "
48            sentence += " " * (maxWidth - len(sentence))
49            ans.append(sentence)
50            sentence = ""
51            currlinelength = 0
52            linewords = []
53
54        
55        return ans