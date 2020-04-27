from tkinter import*
from tkinter import ttk
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import threading

root=Tk()
root.geometry("755x400")
root.config(bg="white")
root.title("miniGoogle")

search=Frame(root,background="white")
search.place(x=0,y=0,width=750,height=400)

showResult=Frame(root,background="white")
showResult.place(x=0,y=0,width=750,height=400)
def show(frame):
   frame.tkraise()
#-------------------------------------------------------
style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )
style.configure('TButton', font = 
               ('calibri',23),  
                    borderwidth = '1')
#--------------------------------------------

Estyle = ttk.Style()
Estyle.configure('TEntry', foreground = 'green')
#---getValue---------------------------------------------------------
def getValue():
   ua = UserAgent()
   query=SearcBox.get()
   tit.config(text="search : "+str(query))
   google_url = "https://www.google.com/search?q=" + query + "&num=" + str(5)
   response = requests.get(google_url, {"User-Agent": ua.random})
   soup = BeautifulSoup(response.text, "html.parser")
   result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})
   links = []
   titles = []
   descriptions = []
   for r in result_div:
       # Checks if each element is present, else, raise exception
       try:
           link = r.find('a', href = True)
           title = r.find('div', attrs={'class':'vvjwJb'}).get_text()
           description = r.find('div', attrs={'class':'s3v9rd'}).get_text()
           
           # Check to make sure everything is present before appending
           if link != '' and title != '' and description != '': 
               links.append(link['href'])
               titles.append(title)
               descriptions.append(description)
       # Next loop if one element is not present
       except:
           continue
   style.configure('TButton', font = 
                  ('calibri',10), 
                       borderwidth = '1')
   show(showResult)
   length=len(descriptions)
   line=1
   for i in descriptions:
      answer.insert(END,"=> "+i+'\n')
   for i in descriptions:
      a=i.split("\n")
      st=f"{line}"+".0"
      end=f'{line}'+'.2'
      answer.tag_add(f"start{line}",st,end)
      answer.tag_config(f"start{line}", foreground="red")
      line+=len(a)
   answer.config(height=2+2*length)

def goBack():
   SearcBox.delete(0,END)
   show(search)
   answer.delete('1.0','end')
   style.configure('TButton', font = 
                  ('calibri',23), 
                       borderwidth = '1')
#----------showResult------------------------------------------------------
tit=Label(showResult,font=('Comic Sans MS',18),bg="white")
tit.place(x=10,y=10)

back=ttk.Button(showResult,text="Go Back",style='C.TButton',command=lambda:goBack())
back.place(x=600,y=40)

answer=Text(showResult,foreground='blue',font=('Comic Sans MS', 12),width=74,height=2)
answer.place(x=10,y=100)


#----search----------------------------------------------------------------
canvas=Canvas(search,width=500,height=130)
canvas.place(x=120,y=0)
photoi=PhotoImage(file='mini.png')
canvas.create_image(0,0,anchor=NW,image=photoi)

SearcBox=ttk.Entry(search,width=25,font = ('Comic Sans MS', 22))
SearcBox.place(x=68,y=200)

btn=Button(search,text="search",command=lambda:threading.Thread(target=getValue).start())#,font = ('Kristen ITC', 22))
btn.place(x=500,y=199)

show(search)





root.mainloop()
