import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https//www.link-of-the-website.com'

headers = {
    "User-Agent": 'your user agent here'}
#You can find this by searching "my user agent" in google, and pasting it here.

def check_price():
    page = requests.get(URL, headers=headers)
    
    soup = BeautifulSoup(page.content,'html.parser')
    
    title = soup.find(id="productTile").get_text()
    #This is <span id="  "> (product's name)
    price = soup.find(id="priceblock_outprice").get_text()
    #The <span id="   "> (product's price)
    converted_price = float(price[0:5])
    #Show only the first digits of the price
    
    if(converted_price < 1000):
        send_mail()
    
    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('your_address@gmail.com', 'your_password')
    #You can either activate Google two-factor auth. and create a password just for this service.
    #Or you can use your Gmail password by enabling Less Secure App Access.

    subject = 'Price fell down'
    body = 'Check the Amazon link https//www.link-of-the-website.com'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'your_address@gmail.com', #From
        'the_email_that_you_are_sending_to@gmail.com', #To
        msg
    )
    print('Email has been sent.')

    server.quit()


while(True):
    check_price()
    time.sleep(3600)
    #(seconds)Period of time that the code runs and checks the website: 60 = every minute | 3600 = every hour | 86400 = once a day.
