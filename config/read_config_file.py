#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 20:54:52 2026

@author: arturo
"""
import traceback
import os

class Config:    
    @classmethod
    def load_info(cls) -> dict:
        """
        Read file "config.json".
        
            * Arguments:
                - None

            * Returns:
                -            (dict) : All variables for the execution.
                -             (str) : Text log error.
        """
        try:
            # Read config file (Get variables in "config.json" file.) 
            current_work_dir:str   = (os.getcwdb()).decode('utf-8')
            base_path_dir:str      = os.path.abspath(current_work_dir)
            
            config_json_name:str    = 'config.json'
            folder_output_name:str  = 'output'
            log_name:str            = 'log.log'
            file_execution_name:str = 'Reporte.csv'
            end_process_error:bool  = False
            
            return {
                    'base_path_dir': base_path_dir,
                    'config_json_name' : config_json_name,
                    'folder_output_name': folder_output_name,             
                    'log_name': log_name,
                    'file_execution_name': file_execution_name,
                    'end_process_error': end_process_error
                    }, ''

        except:
            print('* No se pudo leer archivo config.\n * Error:', traceback.print_exc())
            txt_in_log = '* No se pudo leer archivo config.\n'
            return {}, txt_in_log
