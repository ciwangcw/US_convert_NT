"""
__  file__: day09_US_convert_NT.py
__ brief__: practice
__author__: WANG, CI 王奇
__  date__: 2022  04  07
"""
import tkinter as tk                        # 引用GUI函式庫tkinter,以下簡稱tk

"""
建立控制字型變數
"""
fontUS = "Consolas"                         # 控制英文字型變數
fontTC = "Microsoft JhengHei"               # 控制繁中字型變數
fontSize=20                                 # 控制字型大小變數
# -------------------------------------------

"""
建立視窗及設定變數
"""
win = tk.Tk()                               # 建立視窗
win.wm_title("美金轉台幣 by CiWang")                   # 視窗標題
w=600                                       # 控制視窗寬的變數
h=300                                       # 控制視窗高的變數
win.maxsize(w,h)                            # 最大視窗
win.minsize(w,h)                            # 最小視窗
win.resizable(0,0)                          # 0=False,不調整視窗大小
# -------------------------------------------

"""
建立label,位置及相關變數設定
"""
labelX = 10                                 # 控制label x位置
labelY = 10                                 # 控制label y位置
labelYAdd = 50                              # 控制label y累加間隔的位置

labelUS = tk.Label(win,text="美金:",font=(fontTC,fontSize))
labelNT = tk.Label(win,text="台幣:",font=(fontTC,fontSize))
labelRates = tk.Label(win,text="匯率:",font=(fontTC,fontSize))
labelUS.place(x=labelX,y=labelY+labelYAdd*0)
labelNT.place(x=labelX,y=labelY+labelYAdd*2)
labelRates.place(x=labelX,y=labelY+labelYAdd*4)
# -------------------------------------------

"""
建立entry,位置相關變數及函數
"""
entryX = 100                                # 控制entry x位置
entryY = 12                                 # 控制entry y位置
entryYAdd = 50                              # 控制entry y累加間隔的位置
booleanUS = True                            # 控制判斷美金轉台幣
booleanNT = True                            # 控制判斷台幣轉美金
defalutUS = 0.0                             # 美金預設值
defalutNT = 0.0                             # 台幣預設值
defalutRates = 28.83                        # 匯率預設值

def strUS_callback(func,subst,widget):      # 美金entry,字變更觸發事件,美金轉台幣
    global booleanUS,booleanNT              # 使用全域變數
    booleanUS = True                        # 當美金觸發,設為true,代表美金轉台幣
    booleanNT = False                       # 不是台幣轉美金,設為False

def strNT_callback(func,subst,widget):      # 台幣entry,字變更觸發事件,台幣轉美金
    global booleanUS,booleanNT              # 使用全域變數
    booleanUS = False                       # 不是美金轉台幣,設為False
    booleanNT = True                        # 台幣觸發事件,設為True,台幣轉美金

def strRates_callback(func,subst,widget):   # 匯率entry,字變更觸發事件
    global booleanUS,booleanNT              # 使用全域變數
    global entryUS,entryNT
    global defalutUS,defalutNT
    entryUS.delete(0, "end")                # 更改匯率,美金數值刪除
    entryUS.insert(0, defalutUS)            # 更改匯率,美金數值歸0
    entryNT.delete(0, "end")                # 更改匯率,台幣數值刪除
    entryNT.insert(0, defalutNT)            # 更改匯率,台幣數值歸0

strUS = tk.StringVar(value=defalutUS)                   # 設定美金預設值
strNT = tk.StringVar(value=defalutNT)                   # 設定台幣預設值
strRates = tk.StringVar(value=defalutRates)             # 設定匯率預設值
strUS.trace_add("write",callback=strUS_callback)        # 當entry美金變更呼叫函式
strNT.trace_add("write",callback=strNT_callback)        # 當entry台幣變更呼叫函式
strRates.trace_add("write",callback=strRates_callback)  # 當entry匯率變更呼叫函式

entryUS = tk.Entry(win,width=30,textvariable=strUS,font=(fontTC,fontSize))
entryNT = tk.Entry(win,width=30,textvariable=strNT,font=(fontTC,fontSize))
entryRates = tk.Entry(win,width=10,textvariable=strRates,font=(fontTC,fontSize))
entryUS.place(x=entryX,y=entryY+entryYAdd*0)
entryNT.place(x=entryX,y=entryY+entryYAdd*2)
entryRates.place(x=entryX,y=entryY+entryYAdd*4)
# -------------------------------------------

"""
建立button,位置及相關變數及函數
"""
btnX = 145                                  # 控制button x位置
btnY = 59                                   # 控制button y位置

def exchange_rates():                       # btn觸發事件,匯率轉換
    global entryUS,entryNT,entryRates       # 使用全域變數
    global defalutUS,defalutNT
    global booleanUS,booleanNT
    try:                                    # str -> float 成功
        rates = float(entryRates.get())     # 取得匯率並轉浮點數
        US = float(entryUS.get())           # 取得美金並轉浮點數
        NT = float(entryNT.get())           # 取得台幣並轉浮點數
        if booleanUS == True:               # 判斷美金entry變更,美金轉台幣
            value = US * rates              # 台幣=美金*匯率
            entryNT.delete(0, "end")        # 台幣數值刪除
            entryNT.insert(0, value)        # 設定台幣數值=美金*匯率
        elif booleanNT == True:             # 判斷台幣entry變更,台幣轉美金
            value = NT / rates              # 美金=台幣/匯率
            entryUS.delete(0, "end")        # 美金數值刪除
            entryUS.insert(0, value)        # 設定美金數值=台幣/匯率
    except:                                 # str -> float 失敗
        try:                                # 判斷美金str -> float 成功或失敗
            float(entryUS.get())
        except:                             # 失敗,美金恢復預設值
            entryUS.delete(0, "end")
            entryUS.insert(0, defalutUS)
        try:                                # 判斷台幣str -> float 成功或失敗
            float(entryNT.get())
        except:                             # 失敗,台幣恢復預設值
            entryNT.delete(0, "end")
            entryNT.insert(0, defalutNT)
        try:                                # 判斷匯率str -> float 成功或失敗
            float(entryRates.get())
        except:                             # 失敗,匯率恢復預設值
            entryRates.delete(0, "end")
            entryRates.insert(0, defalutRates)

btn = tk.Button(win,text="轉換",width=5,
                font=(fontTC,fontSize-4),command=exchange_rates)
btn.place(x=btnX,y=btnY)
# -------------------------------------------

win.mainloop()                              # 視窗程式無限循環