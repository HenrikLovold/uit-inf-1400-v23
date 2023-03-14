# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:10:18 2023

@author: Rune
"""

class Customer:
    
    def __init__(self,name:str)->None:
        """ Setter navn, samt poeng,level og aktiv."""
        pass        
        
        
    def is_active(self)->bool:
        """ Returnerer om kunden er aktiv eller ikke """
        pass
    
    def activation(self)->None:
        """ Setter kunden til aktiv """
        pass
        
    def add_points(self,extra_points:int)->None:
        """ Legger til de nye poengene til kunden og 
        setter ny level dersom den nye antall poeng tilsier dette """
        pass    
            
    def get_name(self)->str:
        """ Returnerer navnet til kunden """
        pass
    
    def get_level(self)->int:
        """ Returnerer level til kunden """
        pass
    
    def get_points(self)->int:
        """ Returnerer antall poeng kunden har """
        pass