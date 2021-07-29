
lines = []

with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())    #依然要把結果裝起來→把每行,裝進一個清單(姑且叫lines); lines記得回到頂宣告

#重要!!!!!(上方)1.讀完"檔案→清單"後, 2.繼續讀取"清單→?"(用for循環)
for line in lines:
#    print(line)    #中途先print, 先觀察結果: 哪邊要調整or有意外要處理的地方 →發現有換行符號(跑到6行用strip去掉)
    s = line.split(" ")    #怎麼把時間和&人名切開? 先把能切的切開(人名&訊息)

#想不到時,就先印出來觀察+思考: 發現時間字符長度是固定的!!!!! 5個字
    time = s[0][:5]    #直接取前面5個字符 (python中,字符視作清單), 記得存起來
#    print(time)    #暫印出來觀察
    name = s[0][5:]
    print('時間:', time)
    print('人名:', name)