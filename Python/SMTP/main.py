import smtplib
my_email = "pedramos21@gmail.com"
password = "edrurvcwnmgmsukv" #Generate a App Password

#gmail - "smtp.gmail.com"
#yahoo - "smtp.mail.yahoo.com"
#hotmail - "stmp.live.com"
#outlook - "smtp.office365.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #TLS - Transport Layer Security
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="xxxxxx@gmail.com", 
        msg="Subject:Xxxxx\n\nXxxxxxxxxxx"
        )

