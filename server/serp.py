#Import required modules
import requests
import json
import pickle
import re
import pandas as pd
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()


class SerpGenerator:       

   def __init__(self):  
       #Assigns api_key to object variable
       self.api_key = os.environ["SERP_API_KEY"]

   def generate (self, prompt):
      #Set parameters
      params = {
         'api_key': self.api_key,
         #Prompt
         'q': prompt,
         #UI Language set to English
         'hl': 'en',
         #Location sent to United States
         'location': 'United States',
         #Searches routed through Canadian domain
         'google_domain': 'google.com',
         'gl': 'us'

      }
      #Make the GET request to VALUE SERP
      api_result = requests.get('https://api.valueserp.com/search', params)
      #print(json.dumps(api_result.json()))
      #Returns the JSON response from VALUE SERP
      return json.dumps(api_result.json())

   def get_links(self, data):
      #Loads the JSON data into a Python dictionary
      x = data
      h = json.loads(x, strict=False)
      #Creates empty list for storing links
      link_list = []
      #For each link, checks if question data (the dropdown menus on page 1 of Google searches) or link data (if data item is a website), and adds source link depending on case
      if (h.get("related_questions") is not None): 
         length = len(h.get("related_questions"))
      else:
          length = 0
      for i in range (length):
         if (h.get("related_questions")[i].get("source") is not None):
            new_source = {
                "title": h.get("related_questions")[i].get("source").get("title"),
                "url": h.get("related_questions")[i].get("source").get("link")
            }
            link_list.append(new_source)
         else:
            if(h.get("related_questions")[i].get("link") is not None):
                new_source = {
                    "title": h.get("related_questions")[i].get("title"),
                    "url": h.get("related_questions")[i].get("link")
                }
                link_list.append(new_source)
      #Gets organic results snippets
      if (h.get("organic_results") is not None): 
         length = len(h.get("organic_results"))
      else:
          length = 0
      if (h.get("organic_results") is not None):
         length_organic = len(h.get("organic_results"))
         for i in range (length_organic):
            if (h.get("organic_results")[i].get("link") is not None):
                new_source = {
                    "title": h.get("organic_results")[i].get("title"),
                    "url": h.get("organic_results")[i].get("link")
                }
                link_list.append(new_source)
      #Returns list of links
      return(link_list)
