#!pip install jieba
import pandas as pd
import jieba
import re
import os
import datetime
import pandas as pd
#from emotion import emotion_main
#清除雜訊
def clean_text(text):
    text=text.replace("\n"," ")
    text=re.sub(r"-"," ",text)
    text=re.sub(r"\d+/\d+/\d+","",text)
    text=re.sub(r"[0-2]?[0-9]:[0-6][0-9]","",text)
    text=re.sub(r"[\w]+@[\.\w]+","",text)
    text=re.sub(r"[a-zA-Z]*[:\//\]*[A-Za-z0-9\- ]+\.+[A-Za-z0-9\.\/%&=\?\- ]+/i","",text)
    text=re.sub(r"[a-zA-Z]+","",text)
    pure_text=''
    for letter in text:
        if letter.isalpha() or letter==' ':
            pure_text+=letter
    text=' '.join(word for word in pure_text.split() if len(word)>1)
    return text

#停用詞
def stopWord_clean():
    stop=[]
    file_stop = r'stopwords_new.txt'
    with open(file_stop,'r',encoding='utf-8-sig') as f :
        lines = f.readlines()  # lines是list类型
        for line in lines:
            lline  = line.strip()     # line 是str类型,strip 去掉\n换行符
            stop.append(lline)
    return stop

#回傳情緒表格
def get_sentment(sentment_table,jie_words):
    return sentment_table[sentment_table.word.isin(jie_words)]

#除了計算情緒分數，同時也將pos,mid,neg進行加總
#由於可能備註文本內容過少，導致分數加總無辨識度，所以附加正向、中立、負向字詞的頻次加總
def emotion_main(txt):
    
    columns = ['word','score','pos','mid','neg','None','notWord']
    table = pd.read_csv('opinion_word_utf8.csv',names=columns)
    for i in list(table.word):
        jieba.add_word(i)

    stop=stopWord_clean()#停用詞列表
    txt=clean_text(txt)#clean noise
    t=jieba.lcut(txt)#分詞
    t=[i for i in t if i not in stop ]#remove stop words
    tmp=get_sentment(table,t)#caculate
    tmp1=tmp.copy()
    for i in ['pos','mid','neg']:
        tmp1.loc[:,i]=tmp1.loc[:,i].apply(lambda x : 1 if x>0 else 0)
    table1=tmp1[['pos','mid','neg']].sum()
    posi_score=table1.pos
    mid_score=table1.mid
    neg_score=table1.neg
    emo_score=tmp.score.sum()#score
    return posi_score,mid_score,neg_score,round(emo_score,2)



def emotion_update():
    table=pd.read_csv('maindata.csv')
    data=[]
    for txt in table['備註'].values:
        if type(txt)!=str:
            data.append((0,0,0,0))
        else:
            data.append(emotion_main(txt))
    #做表
    table['日期']=pd.to_datetime(table['日期'])
    table_f=pd.DataFrame(data=data,columns=['正向','中立','負向','情緒分數'],index=table['日期'])
    table_f.to_csv('emotion.csv')
    print("update emotion'score finish....")
