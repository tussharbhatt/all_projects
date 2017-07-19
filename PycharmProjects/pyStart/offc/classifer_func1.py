from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
train=[('Serial0/0/0 Interface is down','link down'),
       ('Device is not responding to ICMP','Branch disconnected-Isolated'),
       ('primary lease line down.','Link is Down'),
       ('SBI-BLN-3845-0046-MPLS. Critical Branch Serial1/0:0  2 Mbps BSNL','fast ethernet down'),
       ('SBI-BLS-1921-0540-MPLS-Vodafone-P2S1n2-ALTSP.Korbamain.sbi.ddin','branch isolated'),
       ('RE: SBI Khutauna (12567 branch running on back up  link from 20 FEB 2017, 1:33 PM but case not gener','gigabit ethernet')]

cl=NaiveBayesClassifier(train)
fout=open("C:\\Users\\tushar.bhatt\\Desktop\\offc\\classifier_Output.txt",'w+')
with open("C:\\Users\\tushar.bhatt\\Desktop\\offc\\tick_desc_jpn.txt",'r') as fin:
    for lines in fin:
        temp=cl.classify(lines)
        fout.write(lines.strip()+" -> "+temp)
        fout.write("\n")
    fin.close()
fout.close()

'''from sklearn.neural_network import BernoulliRBM
train_feat=[i[0] for i in train]
train_label=[i[1] for i in train]
'''