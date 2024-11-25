print("hello")
print("hello world")

# python japan ゼロからのPython入門講座("https://www.python.jp/train/index.html")
1 + 1
abs(122)
minus_value = 100 * -1/3
abs(minus_value)
round(minus_value, 2)

min(10, 3, minus_value)
max(10, minus_value, 1)

import math #モジュールをインポート
math.sqrt(2) #モジュール.関数でモジュール内の特定の関数を呼び出せる

import calendar
calendar.prmonth(2024, 11)
"ptyhon test" #文字列

# 文字列の結合
"ABSD" + "EFGH"
# 123 + "ABC" 数値と文字列の演算は不可

# 文字列の数値化
text = "123"
int(text)
int(text) + 456
# int("hello")はもちろん数値化不可

# 数値の文字列化
num = 123
str(num)

# 文章内に数値を挿入する
hight = 172
print("わたしの身長は" + str(hight) + "cmです")
print("my hight is", hight, "cm.")

# input()
input("好きな文字を入力") #よくわからないので別の場所で

# メソッド：データに結びついた関数
# データ.メソッド(引数)
text = "lower text"
uppered_text = text.upper() # upper()メソッドで大文字に変換
print(uppered_text)

text = "I love you very much"
text.find("very") # text内の特定の文字列を検索し、先頭(0)から何文字目(スペースを含む)にあるかを返す

data = 0.5
data.as_integer_ratio() # 実数を二つの整数の比で返す

# Python学習講座("https://www.python.ambitious-engineer.com/archives/3012")

#演習問題1
x = 100
y = 200
z = 300
w = x + y + z
print(w)
# 演習問題2
x = 100
y = 200
w = (x + y) * 2
print(w)

# 演習問題1(文字列)
text1 = "こんばんは、"
text2 = "いい夜ですね。"
text3 = "今日の夕飯は何ですか？"
bun = text1 + text2 + text3
print(bun)

# 演習問題2(文字列)
text1 = "私の年齢は"
age = 22
text2 = "歳です。"
print(text1 + str(age) + text2)
print(text1, age, text2)

print("適当なキーを入力してください")
x = input(">> ")
print(x + "が入力されました。")

print("2数の和を求めます")
print("一つ目の数値を入力してください")
x = input(">> ")
print("2つ目の数値を入力してください")
y = input(">> ")

x2 = int(x)
y2 = int(y)
z = x2 + y2
print("2つの和：", z)

# 条件分岐
input_val = input("年齢 = ")
age = int(input_val)
# if 条件式: 条件が真のときに実行する処理
if age < 18:
    print("購入できません")

# 例題1
input_val = input("x = ")
x = int(input_val)
if x > 20:
    print("入力した値は20より大きいです")
print("処理が終了しました")
# 例題2
input_val = input("x = ")
x = int(input_val)
if x == 100:
    print("入力値は100と等しいです")

# 複数の条件分岐
input_val = input("年齢 = ")
age = int(input_val)
if age < 18:
    price = 500
else:
    price = 1000
print("値段：", price)

input_val = input("年齢 = ")
age = int(input_val)
if age < 18:
    price = 500
elif 18 <= age < 65:
    price = 1000
else:
    price = 700
print("値段：", price, "円")

# 演習問題1
input_age = input("年齢を入力してください。>> ")
age = int(input_age)
input_men = input("会員であればYを入力してください。>> ")
if input_men == "Y":
    if age < 18:
        price = 100
    else:
        price = 1000
else:
    if age < 18:
        price = 1500
    else:
        price = 2000
print("値段：", price, "円")

# リストとループ
points = [69, 75, 81, 80, 77] # リストは[]で囲む
print(points) # 要素の確認

# リストのインデックスは0から始まる
my_list = [1, 3, 5, 7, 9]
x = my_list[2] # my_listの2番目の要素を変数xに格納
print(x)

# 上書きもできる
my_list[2] = 100
print(my_list)

# リストをループ処理
# forループ内変数inリスト: 処理
# リストの先頭から順に取り出した値がループ内変数xに格納され、for文内部で使用可能
points = [69, 75, 81, 80, 77]
for x in points:
    print(x)

sum_val = 0
points = [69, 75, 81, 80, 77]
for x in points:
    sum_val = sum_val + x # リストの値を順に足し合和得て合計を変数sum_valに格納
    print("現在のsum_val...", sum_val)
print("合計...", sum_val)

# ループ内変数を利用しない例
points = [69, 75, 81, 80, 77]
for x in points:
    print("おはよう")
# 同じことをrange()関数で行う
points = [69, 75, 81, 80, 77]
for x in range(25):
    print("おはよう")

# 演習問題1
test_suzuki = [89, 70, 66, 88, 82]
print(test_suzuki[2]) # 3回目のテスト結果を表示
# forloopで合計を求める
sum_val = 0
for x in test_suzuki:
    sum_val = sum_val + x
    print("今回までの得点の合計...", sum_val)
print("全ての合計点...", sum_val)

# 演習問題2: if文と合わせて80以上の合計をだす
test_suzuki = [89, 70, 66, 88, 82]
my_sum = 0
for p in test_suzuki:
    if p >= 80:
        my_sum = my_sum + p
        print("有効値の合計...", my_sum)
print("合計...", my_sum)

# 演習問題3
for x in range(5):
    print("ohayou")