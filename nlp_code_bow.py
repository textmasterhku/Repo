#We take the corpus and the respective weightings from previous stpes,
# the format is like: [['tariff',-1],...]
#We take the articles that we scraped from websites and read them as
# excel, the purpose is to put them in list.
import pandas as pd
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
#'result.xlsx' are the articles that we scraped from CNN
#'intergrated significant words.xlsx' are all the positive and negative 
#words regarding trade war
df1 = pd.read_excel( "F:/研究生/nlp/pre3/result_314.xlsx", header = 0)
df2 = pd.read_excel( "F:/研究生/nlp/pre2/intergrated significant words.xlsx")

#list11 contains all the positive and negative words
list11=[]
for i in range(len(df2)):
    x = df2.iloc[i,0]
    list11.append(x)
    
df3 = pd.read_excel( "F:/研究生/nlp/pre2/lm_negative (1).xlsx")
df4 = pd.read_excel( "F:/研究生/nlp/pre2/lm_positive (1).xlsx")
#list11 contains all the positive and negative words
list12=[]
for i in range(len(df3)):
    x = df3.iloc[i,0]
    list12.append(x)
list13=[]
for i in range(len(df4)):
    x = df4.iloc[i,0]
    list13.append(x)    
list_neg=[]
list_pos=[]
for i in list12:
    x = i.replace(' ','')
    list_neg.append(x)
for i in list13:
    x = i.replace(' ','')
    list_pos.append(x)
# we turn all positive and negative words into lower case
list_neg = [item.lower() for item in list_neg]   
list_pos = [item.lower() for item in list_pos]    
     
    
# we remove all space from the positive and negative words
list1=[]
for i in list11:
    x = i.replace(' ','')
    list1.append(x)
# we turn all positive and negative words into lower case
list1 = [item.lower() for item in list1]
testlist=[]
#testlist contains all articles from webscraping
for i in range(len(df1)):
    x = df1.iloc[i,2]
    testlist.append(x)

#we tokenize the articles
tokenizedlist=[]
for i in testlist:
    if type(i) == float:
        tokenizedlist.append('')
    else:
        tokenizedlist.append(word_tokenize (i))
# we turn all words in the articles into lower case
for i in range(len(tokenizedlist)):
    tokenizedlist[i] = [item.lower() for item in tokenizedlist[i]]
list_length=[]
for i in tokenizedlist:
    list_length.append(len(i))

##Stemming and lemmatization
wnl = WordNetLemmatizer()
for i in tokenizedlist:
    for n in i:
        n = wnl.lemmatize(n)
##remove all words that are neither positive nor negative
tokenizedlist_final=[]
for i in tokenizedlist:
    x = []
    for n in i:
        if n in list1:
            x.append(n)
    tokenizedlist_final.append(x)

###use bow
counter_list=[]
for i in tokenizedlist_final:
    x = Counter(i)
    counter_list.append(x)
##convert counter to list, keep the number of occurance of each of the word

resultlist_1=[]
for i in counter_list:
    xxx = sorted(i.elements())
    resultlist_1.append(xxx)
# result_list1 aims at puting all positive and negati
#ve words that occurs in each article into a list
#resultlist_1 = []
#for n in range(len(tokenizedlist)):
#    x = []
#    resultlist_1.append(x)

#for k in list1:
#    for n in range(len(tokenizedlist)):
#        x = tokenizedlist[n]
#        if x.count(k) != 0:            
#            resultlist_1[n].append(k)

resultlist_1_quchong = []
for i in resultlist_1:
    x = list(set(i))
    resultlist_1_quchong.append(x)

list_score=[]
for i in resultlist_1:
    k = 0
    for n in i:
        if n in list_neg:
            k = k - 1
        else:
            k = k + 1
    list_score.append(k)
list_score_adjusted=[]
for i in range(len(list_score)):
    if list_length[i] != 0:
        list_score_adjusted.append(list_score[i]/list_length[i]*1000)
    else:
        list_score_adjusted.append(0)
print ('mean',sum(list_score_adjusted)/len(list_score_adjusted))
timehorizon=range(len(list_score_adjusted))
plt.plot(timehorizon,list_score_adjusted)

df5 = pd.read_excel( "F:/研究生/nlp/pre3/result_314_2.xlsx", header = 0)
df5['score'] =  list_score_adjusted

df5.sort_values(by = ['Date'])
group_by_date=df5.groupby('Date')
df6 = group_by_date[['score']].sum()
df6.plot()
df6.to_csv ("F:/研究生/nlp/signal_20190319.csv")　