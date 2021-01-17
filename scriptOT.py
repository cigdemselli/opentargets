#!/usr/bin/env python

#import necessary packages
import argparse
import pandas
import opentargets
from opentargets import OpenTargetsClient

#arguments and help
parser = argparse.ArgumentParser(description='This is a Python script to  query the Open Targets REST API to get association_score.overall for a given target (gene Ensembl id) or disease (EFO id).')
parser.add_argument('-t','--target', help='target_id such as ENSG00000197386')
parser.add_argument('-d','--disease', help='disease_id such as EFO_0000616 or Orphanet_399')
args = parser.parse_args()

#get arguments
datadict_target = {k: v for k, v in args._get_kwargs() if k.startswith("target")}
target_id = datadict_target.get ("target")

datadict_disease = {k: v for k, v in args._get_kwargs() if k.startswith("disease")}
disease_id = datadict_disease.get("disease")

#First, print an error message if no argument is provided.
#Then, run appropriat code depending on input argument (target or disase)
if target_id == None and disease_id == None:
    print("Error: target_id or disease_id must be provided. Provide a target_id such as ENSG00000197386 or disease_id such as Orphanet_399.")
elif target_id != None and disease_id != None:
    print("Error: One argument should be provided at a time. Provide either a target_id such as ENSG00000197386 or disease_id such as Orphanet_399.")
else:
    #get associations
    client = OpenTargetsClient() 
    response = client.filter_associations()

    #filter, calculate and print required information for a target or disease 
    if target_id != None:
      #filter for target_id. Print target_id, disease_id & association_score.overall. 
      filtered = response.filter(target=target_id)
      target_filtered = filtered.to_dataframe()
      target_fin = target_filtered[["target.id", "disease.id", "association_score.overall"]]
      print(target_fin)
      #calculate and print maximum, minimum and average and standard deviation values of association_score.overall
      maximum = target_fin["association_score.overall"].max()
      minimum = target_fin["association_score.overall"].min()
      average = target_fin["association_score.overall"].mean()
      std_dev = target_fin["association_score.overall"].std()
      print(f"maximum={maximum} minimum={minimum} average={average} standard_deviation={std_dev}")
     
    else:
      #filter for disease_id. Print target_id, disease_id & association_score.overall. 
      filtered = response.filter(disease=disease_id)
      disease_filtered = filtered.to_dataframe()
      disease_fin = disease_filtered[["target.id", "disease.id", "association_score.overall"]]
      print(disease_fin)
      #calculate and print maximum, minimum and average and standard deviation values of association_score.overall
      maximum = disease_fin["association_score.overall"].max()
      minimum = disease_fin["association_score.overall"].min()
      average = disease_fin["association_score.overall"].mean()
      std_dev = disease_fin["association_score.overall"].std()
      print(f"maximum={maximum} minimum={minimum} average={average} standard_deviation={std_dev}")

  






