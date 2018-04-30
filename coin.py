import requests
from tkinter import *
import json
import matplotlib.pyplot as plt
#===== Basic structure
root=Tk()
root.title("Coin Master")
root.iconbitmap(r'chart_bar.ico')
root.resizable(width=False,height=False)

#    Header labels
header_name=Label(root,text="Name",bg="white",font="Verdana 8 bold")
header_name.grid(row=0,column=0,sticky=N+S+E+W)
header_Symb=Label(root,text="Symbol",bg="Silver",font="Verdana 8 bold")
header_Symb.grid(row=0,column=1,sticky=N+S+E+W)
header_price=Label(root,text="Price",bg="white",font="Verdana 8 bold")
header_price.grid(row=0,column=2,sticky=N+S+E+W)
header_rank=Label(root,text="Rank",bg="silver",font="Verdana 8 bold")
header_rank.grid(row=0,column=3,sticky=N+S+E+W)
header_1_hr=Label(root,text="1 Hr Change",bg="white",font="Verdana 8 bold")
header_1_hr.grid(row=0,column=4,sticky=N+S+E+W)
header_24_hr=Label(root,text="24 Hr Change",bg="silver",font="Verdana 8 bold")
header_24_hr.grid(row=0,column=5,sticky=N+S+E+W)
header_7_day=Label(root,text="7 Days Change",bg="white",font="Verdana 8 bold")
header_7_day.grid(row=0,column=6,sticky=N+S+E+W)
header_current_val=Label(root,text="Value Eur",bg="silver",font="Verdana 8 bold")
header_current_val.grid(row=0,column=7,sticky=N+S+E+W)
#===============================================================================
def Data():
    #===================Defining the color of text
    def red_green(amount):
        if amount>0:
            return "green"
        else:
            return "red"
    # Graph
    def graph(pie,pie_size):
        label=pie
        size=pie_size
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red','green','black','brown','pink','darkblue']
        patches, texts = plt.pie(size, colors=colors, shadow=True, startangle=90)
        plt.legend(patches, label, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()


    # Getting the information
    url='https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit=10'
    r=requests.get(url)
    js=json.loads(r.content)
    pie=[]
    pie_size=[]
    # Putting the data of top cryptocurrency
    for i in range(len(js)):
        name = Label(root, text="{0}".format(js[i]["name"]), bg="white", font="Verdana 8 bold")
        name.grid(row=i+1, column=0, sticky=N + S + E + W)
        Symb = Label(root, text="{0}".format(js[i]["symbol"]), bg="Silver", font="Verdana 8 bold")
        Symb.grid(row=i+1, column=1, sticky=N + S + E + W)
        price = Label(root, text="{0}".format(js[i]["price_usd"]), bg="white", font="Verdana 8 bold")
        price.grid(row=i+1, column=2, sticky=N + S + E + W)
        rank = Label(root, text="{0}".format(js[i]["rank"]), bg="silver", font="Verdana 8 bold")
        rank.grid(row=i+1, column=3, sticky=N + S + E + W)
        c1_hr = Label(root, text="{0}".format(js[i]["percent_change_1h"]), bg="white",fg=red_green(float(js[i]["percent_change_1h"])), font="Verdana 8 bold")
        c1_hr.grid(row=i+1, column=4, sticky=N + S + E + W)
        c24_hr = Label(root, text="{0}".format(js[i]["percent_change_24h"]), bg="silver",fg=red_green(float(js[i]["percent_change_24h"])), font="Verdana 8 bold")
        c24_hr.grid(row=i+1, column=5, sticky=N + S + E + W)
        c7_day = Label(root, text="{0}".format(js[i]["percent_change_7d"]), bg="white",fg=red_green(float(js[i]["percent_change_7d"])), font="Verdana 8 bold")
        c7_day.grid(row=i+1, column=6, sticky=N + S + E + W)
        current_val = Label(root, text="{0}".format(js[i]["price_eur"]), bg="silver", font="Verdana 8 bold")
        current_val.grid(row=i+1, column=7, sticky=N + S + E + W)
        pie.append(js[i]["name"])
        pie_size.append(js[i]["price_usd"])
    js=""
    # update Button
    update_button = Button(root, text="Update Prices", command=Data)
    update_button.grid(row=i+2, column=7, sticky=E + S, padx=10, pady=10)
    # For graph
    gra=Button(root, text="Pie Chart", command=lambda :graph(pie,pie_size))
    gra.grid(row=i+2, column=6, sticky=E + S, padx=10, pady=10)
    l=Label(root,text="Price of top cryptocurrencies",font="Verdana 8 bold")
    l.grid(row=i+2,column=1,columnspan=10,sticky=W)
Data()
root.mainloop()
