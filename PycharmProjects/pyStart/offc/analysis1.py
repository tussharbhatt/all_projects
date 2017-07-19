import nltk,os,re
from nltk.corpus import stopwords
replace_text='[^a-zA-Z0-9\s]'
reg_exp=re.compile(replace_text)
rep_num='[0-9]'
rep_num_rx=re.compile(rep_num)
file_path="C:\\Users\\tushar.bhatt\\Desktop\\offc\\tick_desc_jpn.txt"
temp=[]
cleaned_txt=open('C:\\Users\\tushar.bhatt\\Desktop\\offc\\tick_desc_jpn_clean.txt','w+')
with open(file_path,'r') as fin:
    for i in fin:
        temp1=reg_exp.sub(" ",i)
        temp=rep_num_rx.sub(" ",temp1)
        cleaned_txt.write(temp)
        #temp.append(nltk.word_tokenize(i,language='english'))

stop_words=set(stopwords.words('english'))
cleaned_txt.close()
with open('C:\\Users\\tushar.bhatt\\Desktop\\offc\\tick_desc_jpn_clean.txt', 'r') as fin:
    #for lines in fin.read():
    lines=fin.read()
    all_words=(nltk.tokenize.word_tokenize(lines,language='english'))

    word_dist=nltk.FreqDist(w.lower() for w in all_words if not w.lower() in stop_words)
    #for w in all_words:

    most_common=word_dist.most_common()
    #common_words=open('C:\\Users\\tushar.bhatt\\Desktop\\offc\\common_words.txt','w+')
    common_words_filter = open('C:\\Users\\tushar.bhatt\\Desktop\\offc\\common_words_filter.txt', 'w+')
    for i,j in enumerate(most_common):
        #print(i[0])
        #common_words.write(" {}.".format(i+1)+j[0]+"-- {}\n".format(j[1]))

        common_words_filter.write(" {}.".format(i + 1) + j[0] + "-- {}\n".format(j[1]))
    #print(most_common)
    common_words_filter.close()

    #print(all_words)
