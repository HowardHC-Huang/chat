def read_file(filename):    #1把檔案讀出(成一個清單)
    lines = []    #lines.append(line)該行用到lines清單,所以要先宣告

    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:    #把被讀的檔案內容. 一行行(line)裝進清單lines
            lines.append(line.strip())
    return lines    #記得把lines清單回傳出來


def convert(lines):    #2再把清單讀出(成一個個資料), 以轉換
    new = []    #new.append(person + ':' + line)該行用到new清單,所以要先宣告
    person = '123'    #手動宣告一預設值(錯誤處理,為防對話紀錄一開頭就不是人名,而當掉)
#或直接設person = None (python獨有, 宣告一"沒有"預設值, 就不用反抵消預設值了)

    for line in lines:    #再把清單的內容, 一個個取出
        if line == 'Allen':    #如果開頭是人名(Allen),我們就先把它存下來,然後跳至下個循環
            person = 'Allen'
            continue
        elif line == 'Tom':    #如果開頭是人名(Tom),我們就先把它存下來,然後跳至下個循環
            person = 'Tom'
            continue

        if person != '123':    #反抵消一開始設的預設值
            new.append(person + ':' + line)    #轉換後的資料, 依然要用一個清單(new)裝起來
    return new


def write_file(filename, lines):
    with open (filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')




def main():
    lines = read_file('input.txt')    #把檔名做成參數,方便日後修改
# print(lines)測試用    #輸出的開頭會有"\ufeff"符號(編碼問題),改用utf-8-sig
    lines = convert(lines)    #把回傳的new存回lines
    write_file('output.txt', lines)

main()