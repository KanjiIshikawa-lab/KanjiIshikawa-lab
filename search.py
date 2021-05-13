import pandas as pd
import eel


def kimetsu_search(word,csv_name):
    df = pd.read_csv("./{}".format(csv_name))
    source = list(df["name"])

    if word in source:
        print("『{}』はいます".format(word))
        eel.view_log_js("『{}』はいます".format(word))
    else:
        print("『{}』はありません".format(word))
        eel.view_log_js("『{}』はいません".format(word))
        eel.view_log_js("『{}』を追加します".format(word))
        source.append(word)


    df=pd.DataFrame(source,columns=["name"])
    df.to_csv("./{}".format(csv_name),encoding="utf_8-sig")
    print(source)



        