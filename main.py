from email.message import EmailMessage
import smtplib
import ssl

def message(email_send, email_pass):
    try:
        email_rec = input('Enter your the gmail account of the reciever:')

        subject = 'dollar'
        body = '''
    226 EUR to USD or convert 226 Euro in US Dollar
    How much is 226 Euro in US Dollar? - 226 EUR to USD (226 Euro to US Dollar) 
    is 239.09 USD with exchange rate 1.0579 for today. For your convenience Mconvert has online Euro to US Dollar (EUR vs USD) history chart and a table of popular currency pairs with their latest exchange rates for 10/29/2023. If you don’t feel like visiting the site every day, currency converter widget or exchange rates widget can be installed on your website in a matter of minutes. Don’t stop, 
    there is a currency converter sidebar to your right so you can make more conversions. Enjoy!
        '''

        em = EmailMessage()
        em['From'] = email_send
        em['To'] = email_rec
        em['Subject'] = subject  # Changed 'subject' to 'Subject'
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_send, email_pass)
            smtp.sendmail(email_send, email_rec, em.as_string())
        print('sent!')
    except:
        print('Not sent!')

if __name__ == '__main__':
    message('You-Email', 'Your-App-Password')