#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:57:54 2020

@author: Miles
"""

def codon(seq, pos):
    
    seq = seq.upper()
    
    oldchars = "AUCG"       #defined for transcribing
    newchars = "UAGC"
    
    if pos == 2:            #editing seq for read frames          
        seq = seq[1:]
    elif pos == 3:
        seq = seq[2:]
    elif pos == 1:
        seq = seq
    elif pos == 4:
        tab = seq.maketrans(oldchars, newchars) #transcribing
        seq = seq.translate(tab)[::-1]          #reversing
    elif pos == 5:
        tab = seq.maketrans(oldchars, newchars)
        seq = seq.translate(tab)[::-1][1:]
    elif pos == 6:
        tab = seq.maketrans(oldchars, newchars)
        seq = seq.translate(tab)[::-1][2:]
    else:
        print("Error invalid position. Accepted values 1, 2, 3, 4, 5, 6.")
               
    n = 3
    cod = [seq[i:i+n] for i in range(0, len(seq), n)] #read frames
    
    a = cod[-1:]            #removing incomplete codons
    a = str(a)
    if len(a) != 7:
        del cod[-1:]
   
    return cod

def trans_codon(frame):
   #dict for codons to protein
   gencode = {                  
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
    'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W'}
   
   output = []
   
   
   for i in frame:
       if i in gencode:
           output += gencode[i]
       else:
           print("Error: protein not found for", i)
   return output
