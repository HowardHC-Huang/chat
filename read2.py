def read_file(filename):    #1把檔案讀出(成一個清單)
    lines = []    #lines.append(line)該行用到lines清單,所以要先宣告

    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:    #把被讀的檔案內容. 一行行(line)裝進清單lines
            lines.append(line.strip())
    return lines    #記得把lines清單回傳出來


def convert(lines):    #2再把清單讀出(成一個個資料), 以轉換
    person = None    #手動宣告一預設值(錯誤處理,為防對話紀錄一開頭就不是人名,而當掉)
    #或直接設person = None (python獨有, 宣告一"沒有"預設值, 就不用反抵消預設值了)
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_image_count = 0
    viki_image_count = 0

    for line in lines:    #再把清單的內容, 一個個取出
        s = line.split(' ')    #以空白鍵為訊號來切割, 並存起來=s
        time = s[0]    #切開+做成清單後, 第0位置皆是時間, 1st皆是人名, 2nd皆是訊息
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count = allen_sticker_count + 1
            elif s[2] == '圖片':
                allen_image_count = allen_image_count + 1
            else:
                for msg in s[2:]:    #從s[2]開始讀到最後(全部的訊息做成一個清單),再用for循環一個個讀出來
                    allen_word_count = len(msg) + allen_word_count
        if name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count = viki_sticker_count + 1
            elif s[2] == '圖片':
                viki_image_count = viki_image_count + 1
            else:
                for msg in s[2:]:    #同上
                    viki_word_count = len(msg) + viki_word_count
    print('Allen說了', allen_word_count, '個字, 用了', allen_sticker_count, '個貼圖, 傳了', allen_image_count, '個圖片')
    print('Viki說了', viki_word_count, '個字, 用了', viki_sticker_count, '個貼圖, 傳了', viki_image_count, '個圖片')


def write_file(filename, lines):
    with open (filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('LINE-Viki.txt')    #把檔名做成參數,方便日後修改
    # print(lines)測試用    #輸出的開頭會有"\ufeff"符號(編碼問題),改用utf-8-sig
    lines = convert(lines)    #把回傳的new存回lines
#    write_file('output.txt', lines)

main()