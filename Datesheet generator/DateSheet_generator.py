import pandas as pd
import itertools as it

name = input("Enter the name of the file: ")
def datesheet_generator(name):
    print("DATESHEET GENERATOR".center(40, " "))
    d = {}
    subject = []
    dates = []
    class_list = []
    for i in it.count(1):
        sub = input(f"enter subject {i}: \t")
        if sub.lower() == "stop":
            break
        date = input(f"enter date for {sub.upper()}, format should be dd/mm/yy {i}: \t")
        if date.lower() == "stop":
            break
        classes = input(f"enter class: \t")
        if classes.lower() == "stop":
            break
#new
        subject.append(sub)
        dates.append(date)
        class_list.append(classes)
        d['SUBJECTS'] = subject
        d['DATES'] = dates
        d['CLASS'] = class_list

        df = pd.DataFrame(d)
        print(df)
        df.to_csv(f"C:\\Users\\pc\\Desktop\\{name}.csv", index=False)
datesheet_generator(name)