# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


# select several components -> several villas

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div(dcc.Input(id='input-box', type='text')),
    html.Button('Submit', id='button'),
    html.Div(id='output-container-button',
             children='Enter a value and press submit')
])


@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')])
def update_output(n_clicks):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://www.airbnb.com/login")

    # works!!!
    # path_logo = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/header/div/div/div[1]/div/div[1]/div/div/button/div')
    # path_logo.click()
    # driver.find_element_by_xpath("//*[contains(text(), 'Log In')]").click()

    # return (driver.find_element_by_xpath("//*[contains(text(), 'Log In')]"))
    # input type: email
    # name: email

    elem = driver.find_element_by_id("email-login-email")
    elem.send_keys("caca")


    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return str(soup)

    # return 'The button has been clicked {} times'.format(n_clicks)


if __name__ == '__main__':
    app.run_server(debug=True)
