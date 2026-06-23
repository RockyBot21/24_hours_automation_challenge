#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 20:49:55 2026

@author: arturo
"""
from mail_activites.read_dummy_mails import Emails
from config.read_config_file import Config

if __name__ == "__main__":
    # Read config file
    variables, text_error = Config.load_info() 
    
    if not bool(text_error):
        with Emails(variables=variables, teardown=True) as bot:
            bot.create_log_file()
            bot.read_config_file()
            bot.read_emails()

    else:
        print('ERROR: Revisar lectura del archivo config (.json).\n * ERROR: {text_error}')