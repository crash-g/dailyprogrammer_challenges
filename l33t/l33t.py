import re

class l33t:
    # static constructor
    l33tDict = {"A" : "4",
            "B" : "6",
            "E" : "3",
            "I" : "1",
            "L" : "1",
            "M" : "(V)",
            "N" : "(\)",
            "O" : "0",
            "S" : "5",
            "T" : "7",
            "V" : "\/",
            "W" : "`//"}
    englishDict = {re.escape(v): k for k, v in l33tDict.items()}
    l33tPattern = re.compile(r'(' + '|'.join(l33tDict.keys()) + r')', flags=re.I)
    englishPattern = re.compile(r'(' + '|'.join(englishDict.keys()) + r')', flags=re.I)
    # written dict as regexp OR

    @staticmethod
    def toL33t(s):
        return l33t.l33tPattern.sub(lambda x:l33t.l33tDict[x.group().upper()], s)

    @staticmethod
    def fromL33t(s):
        return l33t.englishPattern.sub(lambda x:l33t.englishDict[re.escape(x.group()).upper()], s)

with open("english.txt", "r") as lines:
    for line in lines:
        l = line.strip()
        print(l + " --> " + l33t.toL33t(l))

with open("l33t.txt", "r") as lines:
    for line in lines:
        l = line.strip()
        print(l + " --> " + l33t.fromL33t(l))
