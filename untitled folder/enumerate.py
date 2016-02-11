# -*- coding: utf-8 -*-
import sys
import urllib2, json, sys

def plusOne(strList,n):
    if len(strList) - 1 < n:
        return "0"
    char = strList[n]
    if char == "z":
        strList[n] = "a"
        return plusOne(strList,n+1)
    strList[n] = chr(ord(char) + 1)
    return strList

def next(strList):
    return plusOne(strList,0)

# 英単語を受け取って、日本語訳を並べた文字列を返す関数
def translate(phrase):
    # Glosbe API により、引数に与えられた単語の翻訳を取得
    # set URL
    from_lang = "en"# English
    dest_lang = "ja"# Japanese
    url = "https://glosbe.com/gapi/translate?from=" \
        + from_lang + "&dest=" + dest_lang \
        + "&format=json&phrase=" + phrase + "&pretty=true"
    response = urllib2.urlopen(url)
    json_data = response.read()
    json_dict = json.loads(json_data)

    return_txt = "" # これを返り値にする
    tuc = json_dict["tuc"]# tuc: list
    for i in range(len(tuc)):
        if u"phrase" in tuc[i].keys():
            return_txt += tuc[i]["phrase"]["text"] + "\n"
    return return_txt

# Main関数
if __name__ == '__main__':
    argvs = sys.argv
    num = int(argvs[1])

    strList = ["a"]
    for i in range(num - 1):
        strList.append("a")

    for i in range(pow(26,num)):
        strForPrint = reversed(strList)
        str = "".join(strForPrint)
        translated = translate(str)
        if translated:
            print str
        strList = next(strList)
        if strList == "0":
            break



