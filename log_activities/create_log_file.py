#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 20:56:31 2026

@author: a
"""
import logging
import os

class Log:
    @staticmethod
    def create_and_write_in_log(log_name:str, path_log_file:str, set_log_level:bool, level:str='info') -> logging:
        """
        Write log with the notification error.
        
            * Arguments:
                - log_name            (str) : Log file name error.
                - path_log_file       (str) : Path of the file processed.
                - level               (str) : Chat type of message write in log file.  
                - set_log_level      (bool) : Set level of log info to write.
            
            * Returns:
                -              (RootLogger) : Logging instance text file (Log).
                -                 (logging) : Session of the logging instance.
        """
        try:
            if bool(log_name) and bool(path_log_file):                
                match level:
                    case 'info':      level = logging.INFO
                    case 'debug':     level = logging.DEBUG
                    case 'critical':  level = logging.CRITICAL
                    case 'info':      level = logging.ERROR
                    case 'info':      level = logging.FATAL
                    case _:           level = logging.INFO
                
                # Creating an object
                logging.basicConfig(filename = os.path.join(path_log_file, log_name),
                                    encoding = 'utf-8',
                                    format   = '%(asctime)s - %(levelname)s - %(message)s',
                                    level    = level,
                                    filemode = 'w')
                
                # Set log level
                if set_log_level:      logging.getLogger('dev').setLevel(level=level)
                else:                  logging.getLogger('dev')
                
                return logging
                
            else:
                raise TypeError("*************** NO SE CREO LOG DE SEGUIMIENTO ***************")

        except FileNotFoundError as FileNotFound:
            print(f'* Error: {FileNotFound}')
            raise TypeError("*************** NO SE CREO LOG (Ruta no existe) ***************")        

