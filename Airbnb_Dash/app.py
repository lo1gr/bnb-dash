# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_html_components as html

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

from bs4 import BeautifulSoup

import time


from login_creds import airbnb_email, airbnb_pw, abritel_email, abritel_pw
from villas_urls import *


# select several components -> several villas

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# Dash will automatically source the css files located in assets/


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div(
        className='section',
        children=[
            html.H1('MEGA UPDATOR DE PRIX', className='landing-text')
        ]
    ),
    html.Div(dcc.Input(id='input-box', type='text')),
    dcc.Dropdown(
    id = 'dropdown',
    options=[
        {'label': 'FOURSEAS', 'value': fourseas},
        {'label': 'ANKAY', 'value': ankay},
        {'label': 'JALNAS', 'value': jalnas}
        {'label': 'TARA_ANAIS', 'value': tara_anais},
        {'label': 'PERLE', 'value': perle},
        {'label': 'LOCASUN', 'value': locasun}
        {'label': 'MAMILI', 'value': mamili},
        {'label': 'MELEA', 'value': melea},
        {'label': 'SUPER', 'value': super}
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
    [State('dropdown','value'),
     State('input-box','value')])
def update_output(n_clicks, value, price):
    if n_clicks is None:
        return "Faire les changements"
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())

        abri, airb = str(value[0]).split(',')

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
        # driver.get(abri)
        # time.sleep(2)
        #
        # # if there is this element then close it, otherwise
        #
        # try:
        #     elem = driver.find_element_by_xpath("//*[@id='one-nightly-rate']/div/div/input")
        #     elem.clear()
        #     time.sleep(1)
        #     elem.send_keys(price)
        #     time.sleep(4)
        #     register = driver.find_element_by_xpath("//*[@id='rates-settings-save-button']")
        #     register.click()
        #
        # except (NoSuchElementException, ElementClickInterceptedException):
        #     driver.find_element_by_xpath("//*[@id='gdpr-close']").click()
        #     elem = driver.find_element_by_xpath("//*[@id='one-nightly-rate']/div/div/input")
        #     elem.clear()
        #     time.sleep(1)
        #     elem.send_keys(price)
        #     time.sleep(4)
        #     register = driver.find_element_by_xpath("//*[@id='rates-settings-save-button']")
        #     register.click()








        ## works!!!

        ## airbnb part, also works:
        # abri, airb = str(value).split(',')
        # abri, airb = str(value[0]).split(',')
        # driver.get("http://www.airbnb.com/login")
        # time.sleep(2)
        # # if find element with id phone-login-phone-number then need to put phone number, otherwise email is good
        # try:
        #     driver.find_element_by_xpath("//*[@id='site-content']/div/div/div/div/div/div/div/div[2]/button").click()
        # except NoSuchElementException:
        #     pass
        #
        # try:
        #     driver.find_element_by_id("email").send_keys(airbnb_email)
        # except NoSuchElementException:
        #     driver.find_element_by_id("email-login-email").send_keys(airbnb_email)
        #
        # time.sleep(2)
        #
        # try:
        #     driver.find_element_by_id("password").send_keys(airbnb_pw)
        # except NoSuchElementException:
        #     driver.find_element_by_id("email-login-password").send_keys(airbnb_pw)
        #
        # try:
        #     submit = driver.find_element_by_xpath("//*[@id='site-content']/div/div/div/div/div/div/div/form[1]/div[3]/button")
        # except NoSuchElementException:
        #     submit = driver.find_element_by_class_name("_1o4htsfg")
        # submit.click()
        #
        # time.sleep(3)
        #
        # # return str(value[0])
        #
        # driver.get(airb)
        #
        # soup = BeautifulSoup(driver.page_source, 'html.parser')

        return str(airb)


if __name__ == '__main__':
    app.run_server(debug=True)
