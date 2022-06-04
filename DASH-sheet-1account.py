from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
import os
from selenium.webdriver.common.keys import Keys
#
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#
#from wand.image import Image
from io import BytesIO
from PIL import Image
import base64
from PIL import ImageTk,Image
import PIL.Image
#
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
#
import tkinter as tk
from tkinter import *
from tkinter import Tk, font
import pyautogui 
#
import pandas as pd
#
path = os.path.dirname(os.path.abspath(__file__))
address = os.path.join(path, 'chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options, executable_path=address)
#
ls_mizan =[]


driver.get('https://www.dttsonline.com/dtts/dtts/customer/login.jsp') 
# taking screenshot
time.sleep(0.5)
a = driver.execute_script("return outerWidth")
b = driver.execute_script("return outerHeight")
c = driver.execute_script("return outerHeight - innerHeight")
elem = driver.find_element_by_xpath('//*[@id="sCaptchaId"]')
driver.save_screenshot('screenshot.png')
#pyautogui.keyDown('alt') 
#pyautogui.keyDown('space') 
#pyautogui.press('n') 
#pyautogui.keyUp('space') 
#pyautogui.keyUp('alt')
#crop the screenshot
img = PIL.Image.open('screenshot.png')
loc = elem.location
size = elem.size
screenSize = img.size
left = loc['x'] * screenSize[0]/a
top = (loc['y'] + c/2) * screenSize[1]/b
right = left + size['width'] + 20
bottom = top + size['height']+ 10
area1 = img.crop((left, top, right, bottom))
area1.save('scaptcha.png', 'PNG')
#minimizing
driver.minimize_window()
#######################################################
#root = Tk()
#root.geometry('+850+100')
#root.configure(bg='teal')
#root.defaultFont = font.nametofont("TkDefaultFont")
#root.defaultFont.configure(family="B Nazanin", size = 11)
#root.title("ورود")
#root.geometry("350x320")
#######################################################
userField = '//*[@id="uid"]'
passField = '//*[@id="passwordInput"]'
capField = '//*[@id="cptch"]'
submit = '//*[@id="loginSmtBtn"]'
refreshcap = '//*[@id="captchaImage"]/a'
#global second
global azad1
#######################################################
from tkinter import *  
from PIL import ImageTk,Image  
root = Tk() 
root.defaultFont = font.nametofont("TkDefaultFont")
root.defaultFont.configure(family="B Nazanin", size = 11)
root.title("ورود") 
canvas = Canvas(root, width = 300, height =100)
#canvas.configure(bg='royalblue')  
img = ImageTk.PhotoImage(Image.open("scaptcha.png"))  
canvas.create_image(150,40,anchor = CENTER, image=img) 
canvas.pack() 
text3 = Text( height = 2 , width = 15)
text3.pack()
l4 = Label( text =  ".لطفا بعد از وارد کردن کپچا، دکمه ورود را بفشارید")
l4.pack(pady= 10)
def sendCaptcha1():
    global azad1
    inp1 = 'psg902460168179'
    inp2 = 'RobIn1400'
    inp3 = text3.get("1.0",'end-1c' )
    inp3 = int(inp3)
    #xpath(ONLINE PLUS SYSTEM)
    driver.find_element_by_xpath(userField).send_keys(inp1)
    driver.find_element_by_xpath(passField).send_keys(inp2)
    itt3 = driver.find_element_by_xpath(capField)
    itt3.send_keys(inp3)
    itt3.send_keys(Keys.ENTER)
    root.withdraw()
    time.sleep(3)
    he = driver.find_element_by_xpath('//*[@id="_accounting"]/a/i')
    he.click()
    ele1 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sec2"]/div[2]/span[2]/span')))
    azad1 = ele1.text
    #print("Value is: %s" % ele1.get_attribute("asset-value.ng-binding.green-val"))
    #print("azad:",azad1)
    driver.quit()
    datacloud()
    #print ("azad:", azad1)
    #driver.switch_to.window("secondtab")
    root.quit()
sendbutton = Button(root,height = 1 , width = 15 , text="ورود", command=sendCaptcha1)
sendbutton.pack(pady =15)
#itt3 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="_dttsLogin_vecchio"]')))
#itt3.click()
#itt2 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, refreshcap)))
#itt2.click()
###############################################################################################
def datacloud():
    global ramzarz
    global ddown
    global sood
    global zarar
    global trade
    sheet_url = 'https://docs.google.com/spreadsheets/d/1Hd3vshQlqpP42NC9XjJyXb1V6sZZt0WeNOiCwIxSK6E/edit#gid=0'
    url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
    df = pd.read_csv(url_1 )
    ramzarz = df['رمز ارز'][0]
    ddown =df['دراپ داون'][0]
    sood = df['سود'][0]
    zarar = df['ضرر'][0]
    trade = df['ترید'][0]

    i = 0
    while(i<4):
        ele = df['میزان'][i]
        ls_mizan.append(ele)
        i = i+1
        

    seedash()
    
#for i in range(0 , 4):
#    print(ls_mizan[i])

#    seedash()



def seedash():
    ###############################################################################################
    app = dash.Dash()

    fig_names = ['حساب اول', 'حساب دوم']
    #fig_general
    fig_dropdown = html.Div(children =[
    html.Div("داشبورد عملکرد شرکت رابین" ,style = {"color" : "royalblue", "padding" : "40px",
                                        "text-align" : "center" ,"background-color" : "white", "font" : "100px","font-family" :"B Nazanin" ,  "border-radius" : "20px"
                                        ,"display" : "left" , "width" : "90%" , "height" : "40px" , "font-size" : "30px",
                                        "margin-down" : "10px"
                                                    }),

    html.Div("میزان دارایی آزاد پرتفو های شرکت رابین" ,style = {"color" : "white", "padding" : "40px",
                                        "text-align" : "center" ,"background-color" : "royalblue", "font" : "100px","font-family" :"B Nazanin" ,  "border-radius" : "20px"
                                        ,"display" : "left" , "width" : "40%" , "height" : "40px" , "font-size" : "30px",
                                        "margin-down" : "10px", "box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"

                                                    }),
    html.Div(("حساب شرکت:  ", azad1 ), style = {
                                "color" : "royalblue" , "font-size" : "30px", "font-family" :"B Nazanin" ,
                                "text-align" : "center" , "background-color" : "lavender","border-radius" : "20px", "padding" : "20px",
                                 "display":"center" , "width" : "40%", "height" : "25px" , "box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"
                                  , "left": "100px"  , "position" : "absolute", "top" : "248px" , "left" : "23px"
                                 }),
    html.Div(("حساب علی:  " , ls_mizan[1] ) , style = {
                                "color" : "royalblue" , "font-size" : "30px", "font-family" :"B Nazanin" ,
                                "text-align" : "center" , "background-color" : "lavender","border-radius" : "20px", "padding" : "20px",
                                "display":"left" , "width" : "40%", "height" : "25px"
                                ,"box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"
                                 ,"position" : "absolute", "top" : "313px" , "left" : "23px" }),
    html.Div(("حساب آرش:   ", ls_mizan[2] ), style = {
                                "color" : "royalblue" , "font-size" : "30px", "font-family" :"B Nazanin" ,
                                "text-align" : "center" , "background-color" : "lavender","border-radius" : "20px", "padding" : "20px",
                                "display":"left" , "width" : "40%", "height" : "25px"
                                ,"box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"
                                , "position" : "absolute", "top" : "378px" , "left" : "23px"
                                                    }),
    html.Div(("حساب سینا:   ", ls_mizan[3] ), style = {
                                "color" : "royalblue" , "font-size" : "30px", "font-family" :"B Nazanin" ,
                                "text-align" : "center" , "background-color" : "lavender","border-radius" : "20px", "padding" : "20px",
                                "display":"left" , "width" : "40%", "height" : "25px"
                                ,"box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"
                                 ,"position" : "absolute", "top" : "443px" , "left" : "23px"     }),
###################################################################################################

    html.Div(("میزان دارایی آزاد رمز ارز شرکت رابین" ), style = {
                                "color" : "white", "padding" : "40px",
                                        "text-align" : "center" ,"background-color" : "royalblue", "font" : "100px", "font-family" :"B Nazanin", "border-radius" : "20px"
                                        ,"float": "up" , "width" : "40%" , "height" : "40px" , "font-size" : "30px",
                                        "margin-down" : "10px"
                                        ,"box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"
                                        ,"position" : "absolute", "top" : "508px" , "left" : "7px"
                                                    }),
    html.Div(("اول:   ", ramzarz ),style = {"color" : "royalblue" , "font-size" : "30px", "font-family" :"B Nazanin" ,
                                "text-align" : "center" , "background-color" : "lavender","border-radius" : "20px", "padding" : "20px",
                                 "display":"right" , "width" : "40%", "height" : "25px"
                                 ,"box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"
                                  ,"position" : "absolute", "top" : "627px" , "left" : "23px"  ,'backgroundColor': 'lavender'
                                                    }),
     html.Div(("opacity   ", "3" ), style = {
                                "color" : "lavender" , "font-size" : "1px", "font-family" :"B Nazanin" ,
                                "text-align" : "center" , "background-color" : "lavender","border-radius" : "20px", "padding" : "20px",
                                "display":"left" , "width" : "1%", "height" : "25px" ,"opacity":"0"
                                                    }),
    #html.Div(("mid" ), style = {
     #                           "color" : "royalblue" , "font-size" : "0.00001px", "font-family" :"B Nazanin" ,
      #                          "text-align" : "center" , "background-color" : "royalblue","border-radius" : "20px", "padding" : "20px",
       #                         "display":"left" , "width" : "20%", "height" : "500px" ,"opacity":"0",
        #                        "position" : "absolute", "top" : "127px" , "right" : "300px"
         #                                           }),

######################################################################################################
    html.Div(("میزان سود امروز:  ", sood ), style = {
                                "color" : "white", "padding" : "40px",
                                        "text-align" : "center" ,"background-color" : "royalblue", "font" : "100px", "font-family" :"B Nazanin", "border-radius" : "20px"
                                        ,"float": "up" , "width" : "40%" , "height" : "40px" , "font-size" : "30px",
                                        "margin-down" : "10px",  "position" : "absolute", "top" : "127px" , "right" : "8px"
                                        ,"box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"
                                                    }),
    html.Div(("میزان ضرر امروز:  ", zarar ), style = {
                                "color" : "white", "padding" : "40px",
                                        "text-align" : "center" ,"background-color" : "dodgerblue", "font" : "100px", "font-family" :"B Nazanin", "border-radius" : "20px"
                                        ,"float": "up" , "width" : "40%" , "height" : "40px" , "font-size" : "30px",
                                        "margin-down" : "10px",  "position" : "absolute", "top" : "241px" , "right" : "7px"
                                        ,"box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"
                                                    }),
    html.Div(("میزان تریدهای امروز:  ", trade ), style = {
                                "color" : "black", "padding" : "40px",
                                        "text-align" : "center" ,"background-color" : "deepskyblue", "font" : "100px", "font-family" :"B Nazanin", "border-radius" : "20px"
                                        ,"float": "up" , "width" : "40%" , "height" : "40px" , "font-size" : "30px",
                                        "margin-down" : "10px",  "position" : "absolute", "top" : "361px" , "right" : "7px"
                                        ,"box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"
                                                    }),
    html.Div(("دراپ داون حساب:  ",ddown ), style = {
                                "color" : "black", "padding" : "40px",
                                        "text-align" : "center" ,"background-color" : "paleturquoise", "font" : "100px", "font-family" :"B Nazanin", "border-radius" : "20px"
                                        ,"float": "up" , "width" : "40%" , "height" : "40px" , "font-size" : "30px",
                                        "margin-down" : "10px",  "position" : "absolute", "top" : "475px" , "right" : "7px"
                                        ,"box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"
                                                    }),

        html.Div([dcc.Dropdown(
                id='fig_dropdown',
                options=[{'label': x, 'value': x} for x in fig_names],
                value=None),
        ], style={'backgroundColor': 'royalblue',
                  "box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)",
                  "border-radius": "20px",
                  "width": "40%",
                  "position": "absolute",
                  "top": "750px",
                  "right": "10px",
                  'overflow': 'show'})
    ])

    fig_plot = html.Div(style={'backgroundColor': 'lavender',"position" : "absolute", "top" : "800px" ,  "width" : "97%"},id='fig_plot')
    app.layout = html.Div([ fig_dropdown, fig_plot])
    #
    #
    @app.callback(
    dash.dependencies.Output('fig_plot', 'children'),        #children
    [dash.dependencies.Input('fig_dropdown', 'value')])
    def name_to_figure(fig_name):
        figure = go.Figure()
        if fig_name == 'حساب اول':
            figure.add_trace(go.Scatter(y=[4, 2, 1]))
        elif fig_name == 'حساب دوم':
            figure.add_trace(go.Bar(y=[2, 1, 3]))
        return dcc.Graph(figure=figure)
    def update_output(fig_name):
        return name_to_figure(fig_name)
    app.run_server(debug=True, use_reloader=False)

root.mainloop()