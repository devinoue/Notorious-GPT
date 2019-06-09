import re
import pandas as pd


df = pd.read_csv("lyrics.csv")

df_hiphop = df.loc[df['genre'] == "Hip-Hop"]

# 歌詞が欠損している場合は削除
df_hiphop = df_hiphop.dropna(subset=['lyrics'])


# 不要な要素の置き換え
df_hiphop['lyrics'] = df_hiphop['lyrics'].replace('\[[^]]+\]', '', regex=True)
df_hiphop['lyrics'] = df_hiphop['lyrics'].replace('\([^)]+\)', '', regex=True)
df_hiphop['lyrics'] = df_hiphop['lyrics'].replace('\{[^}]+\}', '', regex=True)
df_hiphop['lyrics'] = df_hiphop['lyrics'].replace('[+]+', '', regex=True)
df_hiphop['lyrics'] = df_hiphop['lyrics'].replace('[. ]{2,}', '', regex=True)
df_hiphop['lyrics'] = df_hiphop['lyrics'].replace('(VERSE|Verse|verse)+[ ]*\d', '', regex=True)

drop_germany = df_hiphop.index[df_hiphop['lyrics'].str.contains("ich") == True]
df_hiphop = df_hiphop.drop(drop_germany)
drop_french = df_hiphop.index[df_hiphop['lyrics'].str.contains("suis") == True]
df_hiphop = df_hiphop.drop(drop_french)
drop_spanish = df_hiphop.index[df_hiphop['lyrics'].str.contains(" que ") == True]
df_hiphop = df_hiphop.drop(drop_spanish)

drop_other = df_hiphop.index[df_hiphop['lyrics'].str.contains(" je ") == True]
df_hiphop = df_hiphop.drop(drop_other)
drop_other = df_hiphop.index[df_hiphop['lyrics'].str.contains(" ca ") == True]
df_hiphop = df_hiphop.drop(drop_other)




arr=[]

arr = df_hiphop['lyrics'].values.tolist()
text = "\n".join(arr)
text = re.sub("\\n","\n",text)
text = re.sub("\n{2,}","",text)
text = re.sub("\\'","'",text)
text = re.sub(" \n","\n",text)

# Delete too short or too long lines.
lines = text.split("\n");
lines = [line for line in lines if line]
lines = [line for line in lines if len(line) > 3 and len(line) < 369]
lines = [line for line in lines if " " in line]

# 重複を削除(できる限り順番を維持して)
seen = set()
seen_add = seen.add
lines = [ x for x in lines if x not in seen and not seen_add(x)]


text = "\n".join(lines)

with open("lyrics.txt","w",encoding="utf-8") as f:
    f.write(text)
