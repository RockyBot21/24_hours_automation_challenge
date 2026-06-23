#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 21:33:05 2026

@author: arturo
"""
import json

class JsonManipulation:
    @staticmethod
    def filter_by_one_element(path_json_file:str, filter_col_name:str) -> str:
        """
        Filter by json element.
            
            * Arguments:
                - path_json_file        (str) : Path of json file.
                - filter_col_name       (str) : Value to filter elements.
            
            * Returns:
                - json_element_filter   (str) : Element or elements in json (Dictionary).
        """
        try:
            data = JsonManipulation.read_file(path_json_file = path_json_file)
            
            # Filter by one element
            if bool(data):
                json_element_filter = data[filter_col_name]
                return json_element_filter
            else:
                print('* Error. No se encontrarón elemetos en el archivo json.')
                return None
                
        except Exception as e:
            print(f'Error al leer archivo json.\n* Error {e}')
        
        
    @staticmethod
    def read_file(path_json_file:str) -> str:
        """
        Read json file.
    
            * Arguments:
                - path_json_file  (str) : Path of json file.
            
            * Returns:
                - data            (str) : Element or elements in json file (Dictionary).
        """
        f      = open(path_json_file)
        data   = json.load(f)
        f.close()        
        return data
    