import speech_recognition
import os
import pandas as pd

r = speech_recognition.Recognizer() #解析器
r.energy_threshold = 4000

path = "C:/Users/20170507/PycharmProjects/deep_learning_practice/pandas_practice/AI_cup/1116-1129 practice/wav/wav_100/A"
files = os.listdir(path)
files = [path + "\\" + f for f in files if f.endswith('.wav')]
x=[]
for data in files:
    with speech_recognition.AudioFile(data) as source:#讀檔案，檔案讀完自己關掉
        audio = r.record(source)#從souce中獲取數據
        test = r.recognize_google(audio,language='zh_TW')#將數據轉換成文字
        x.append(test)
df = pd.DataFrame()
df["文章"] = x


path = "C:/Users/20170507/PycharmProjects/deep_learning_practice/pandas_practice/AI_cup/1116-1129 practice/wav/wav_100/B"
files = os.listdir(path)
files = [path + "\\" + f for f in files if f.endswith('.wav')]
y=[]
for data in files:
    with speech_recognition.AudioFile(data) as source:#讀檔案，檔案讀完自己關掉
        audio = r.record(source)#從souce中獲取數據
        test = r.recognize_google(audio,language='zh_TW')#將數據轉換成文字
        y.append(test)
df["題目"] = y


path = "C:/Users/20170507/PycharmProjects/deep_learning_practice/pandas_practice/AI_cup/1116-1129 practice/wav/wav_100/C"
files = os.listdir(path)
files = [path + "\\" + f for f in files if f.endswith('.wav')]
z=[]
for data in files:
    with speech_recognition.AudioFile(data) as source:#讀檔案，檔案讀完自己關掉
        audio = r.record(source)#從souce中獲取數據
        test = r.recognize_google(audio,language='zh_TW')#將數據轉換成文字
        z.append(test)
df["選項"] = z
print(df)
df.to_csv('C:/Users/20170507/PycharmProjects/deep_learning_practice/pandas_practice/Result.csv',encoding='utf_8_sig',index=False)
