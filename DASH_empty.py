from typing import type_check_only
import dash
import dash_core_components as dcc
import dash_html_components as html
#from dash import dcc
#from dash import html
import plotly.graph_objects as go


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
    html.Div(("حساب شرکت:  ", "azad1" ), style = {
                                "color" : "royalblue" , "font-size" : "30px", "font-family" :"B Nazanin" ,
                                "text-align" : "center" , "background-color" : "lavender","border-radius" : "20px", "padding" : "20px",
                                 "display":"center" , "width" : "40%", "height" : "25px" , "box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"
                                  , "left": "100px"  , "position" : "absolute", "top" : "248px" , "left" : "23px"
                                 }),
    html.Div(("حساب علی:  " , "ls_mizan[1]" ) , style = {
                                "color" : "royalblue" , "font-size" : "30px", "font-family" :"B Nazanin" ,
                                "text-align" : "center" , "background-color" : "lavender","border-radius" : "20px", "padding" : "20px",
                                "display":"left" , "width" : "40%", "height" : "25px"
                                ,"box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"
                                 ,"position" : "absolute", "top" : "313px" , "left" : "23px" }),
    html.Div(("حساب آرش:   ", "ls_mizan[2]" ), style = {
                                "color" : "royalblue" , "font-size" : "30px", "font-family" :"B Nazanin" ,
                                "text-align" : "center" , "background-color" : "lavender","border-radius" : "20px", "padding" : "20px",
                                "display":"left" , "width" : "40%", "height" : "25px"
                                ,"box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"
                                , "position" : "absolute", "top" : "378px" , "left" : "23px"
                                                    }),
    html.Div(("حساب سینا:   ", "ls_mizan[3]" ), style = {
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
    html.Div(("اول:   ", "ramzarz" ),style = {"color" : "royalblue" , "font-size" : "30px", "font-family" :"B Nazanin" ,
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
    html.Div(("میزان سود امروز:  ", "sood" ), style = {
                                "color" : "white", "padding" : "40px",
                                        "text-align" : "center" ,"background-color" : "royalblue", "font" : "100px", "font-family" :"B Nazanin", "border-radius" : "20px"
                                        ,"float": "up" , "width" : "40%" , "height" : "40px" , "font-size" : "30px",
                                        "margin-down" : "10px",  "position" : "absolute", "top" : "127px" , "right" : "8px"
                                        ,"box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"
                                                    }),
    html.Div(("میزان ضرر امروز:  "," zarar "), style = {
                                "color" : "white", "padding" : "40px",
                                        "text-align" : "center" ,"background-color" : "dodgerblue", "font" : "100px", "font-family" :"B Nazanin", "border-radius" : "20px"
                                        ,"float": "up" , "width" : "40%" , "height" : "40px" , "font-size" : "30px",
                                        "margin-down" : "10px",  "position" : "absolute", "top" : "241px" , "right" : "7px"
                                        ,"box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"
                                                    }),
    html.Div(("میزان تریدهای امروز:  ", "trade "), style = {
                                "color" : "black", "padding" : "40px",
                                        "text-align" : "center" ,"background-color" : "deepskyblue", "font" : "100px", "font-family" :"B Nazanin", "border-radius" : "20px"
                                        ,"float": "up" , "width" : "40%" , "height" : "40px" , "font-size" : "30px",
                                        "margin-down" : "10px",  "position" : "absolute", "top" : "361px" , "right" : "7px"
                                        ,"box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)"
                                                    }),
    html.Div(("دراپ داون حساب:  ","ddown" ), style = {
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
                       
seedash()
