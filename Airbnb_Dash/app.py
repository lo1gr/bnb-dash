# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_html_components as html
from dash.exceptions import PreventUpdate

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

import time


from login_creds import airbnb_email, airbnb_pw, abritel_email, abritel_pw
from villas_urls import *


# select several components -> several villas

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div(dcc.Input(id='input-box', type='text')),
    dcc.Dropdown(
    id = 'dropdown',
    options=[
        {'label': 'FOURSEAS', 'value': 'https://www.abritel.fr/pe/731.1142116.1307405/pd'},
        {'label': 'ANKAY', 'value': 'ANKAY'},
        {'label': 'JALNAS', 'value': 'JALNAS'}
    ],
    multi=True
),
    html.Button('Update les prix stp', id='submit-button'),
    html.Div(id='output-container-button',
             children='Enter a value and press submit')
])


@app.callback(
    Output('output-container-button', 'children'),
    [Input('submit-button','n_clicks')],
    [State('dropdown','value')])
def update_output(n_clicks, value):
    if n_clicks is None:
        return "Faire les changements"
    # else:
    #     return str(value[0])
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())

        # driver.get("https://www.abritel.fr/auth/ui/login")
        # elem = driver.find_element_by_id("lex-emailAddress")
        # elem.send_keys(abritel_email)
        #
        # submit = driver.find_element_by_id("lex-initial-button")
        # submit.click()
        #
        # time.sleep(2)
        # driver.find_element_by_xpath("//*[@id='password']").send_keys(abritel_pw)
        #
        # time.sleep(2)
        # driver.find_element_by_id("login").click()
        #
        # time.sleep(3)
        #
        # driver.find_element_by_xpath("//*[@id='site-header__traveler']/span[1]").click()
        # driver.get('https://www.abritel.fr/haod/properties.html')

        # need to check if urls can change!!!




        ## works!!!

        ## airbnb part, also works:
        driver.get("http://www.airbnb.com/login")
        time.sleep(2)
        # if find element with id phone-login-phone-number then need to put phone number, otherwise email is good
        elem = driver.find_element_by_id("email-login-email")
        time.sleep(3)
        elem.send_keys(airbnb_email)

        elem = driver.find_element_by_id("email-login-password")
        elem.send_keys(airbnb_pw)

        submit = driver.find_element_by_class_name("_1o4htsfg")
        submit.click()

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        return str(soup)


if __name__ == '__main__':
    app.run_server(debug=True)
