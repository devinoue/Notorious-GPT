import re
import pandas as pd

df_hiphop = pd.read_csv("hiphop_lyrics.csv")

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
