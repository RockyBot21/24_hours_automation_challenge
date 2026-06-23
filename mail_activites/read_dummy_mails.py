#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 21:37:08 2026

@author: arturo
"""
from json_activities.read_json_file import JsonManipulation
from log_activities.create_log_file import Log

from shutil import rmtree
from typing import List
from glob import glob
import os

class Emails:
    def __init__(self, variables:dict, teardown:bool=False):
        """
         * Attributes         
             - variables  (dict) : Variables of the config file.
        """        
        self.folder_proyect      = os.path.dirname(variables['base_path_dir'])
        self.path_folder_output  = os.path.join(self.folder_proyect, variables['folder_output_name'])
        self.path_config_json    = os.path.join(self.folder_proyect, variables['config_json_name'])
        self.variables           = variables
        self.teardown            = teardown
        self.write_log           = ""
        self.config_json_info    = ""
    
    def __enter__(self):
        return self
    
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Close log.
        
            * Arguments:
                - None
        
            * Returns:
                - None
        """
        if self.teardown:
            self.write_log.info('Proceso terminado.')
            self.write_log.shutdown()
    
    def create_log_file(self) -> None:
        """
        Create a log traceback execution.

            * Arguments:
                - None
            
            * Returns:
                - None
        """
        if os.path.isdir(self.path_folder_output):
            rmtree(self.path_folder_output)
            
        os.makedirs(self.path_folder_output, exist_ok=True)
        
        # Craete log file        
        self.write_log = Log.create_and_write_in_log(log_name       = self.variables['log_name'],
                                                     path_log_file  = self.path_folder_output,
                                                     set_log_level  = True)

    def read_config_file(self):
        self.config_json_info = JsonManipulation.read_file(self.path_config_json)
        
        if not bool(self.config_json_info):
            self.variables['end_process_error'] = True 
            print(self.config_json_info)
        else:
            self.write_log.info('Lectura del archivo "config.json" correcto.')

    def read_emails(self):
        pass
    