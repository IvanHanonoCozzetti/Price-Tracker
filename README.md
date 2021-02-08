# Price Tracker
Price tracker that sends an email when a price goes down using Web Scraping through BeautifulSoup4.

### In order to track a price:
1. Change the `URL` to yours.
2. Change the title and the price respectively to the `<span in>` located in the HTML of the website.
3. Adjust the price alert, `server.login` to the email address details.
4. Adjust the `server.sendmail` (FROM-TO) and the `time.sleep` in order to set the tracking consistency (seconds).


## SMTP
Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and routing e-mail between mail servers. Python provides smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.

## Requests
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — we can simply use the json method.

## Beautiful Soup
Beautiful Soup is a Python library for pulling data out of HTML and XML files. It provides idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.
The bs4/doc/ directory contains full documentation in Sphinx format. Hence we can run `make html` in the directory to create HTML documentation.
