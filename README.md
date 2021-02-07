# Price-Tracker
Price tracker that sends an email when a price goes down using Web Scraping through BeautifulSoup4.

In order to track a price:
1. Change the `URL` to yours.
2. Change the title and the price respectively to the `<span in>` located in the HTML of the website.
3. Adjust the price alert, `server.login` to the email address details.
4. Adjust the `server.sendmail` (FROM-TO) and the `time.sleep` in order to set the tracking consistency (seconds).


## SMTP
Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and routing e-mail between mail servers. Python provides smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
