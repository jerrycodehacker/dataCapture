import pyautogui

import smtplib



def capture_email():

    # Capture the currently opened window's text using pyautogui

    email_text = pyautogui.hotkey('ctrl', 'c')



    # Extract the email address from the captured text

    email = ""

    for line in email_text.split("\n"):

        if '@' in line:

            email = line

            break



    # Use smtplib to send an email to the extracted email address

    sender = "youremail@example.com"

    password = "yourpassword"

    recipient = email

    message = "Default message text"



    with smtplib.SMTP("smtp.gmail.com", 587) as server:

        server.ehlo()

        server.starttls()

        server.ehlo()

        server.login(sender, password)

        server.sendmail(sender, recipient, message)
        
        # Use the pyautogui library to bind a hotkey to the capture_email function 
        #pyautogui.hotkey('alt', 'e', capture_email)

