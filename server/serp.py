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

   def generate (self, company):
      #Set parameters
      params = {
         'api_key': self.api_key,
         #Prompt
         'q': f"{company} company wiki",
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
      #Generates pickle file for output parsing
      pickle_file_path = Path('runs\\company_descriptions\\response_serp_company.p')
      # Open the pickle file for writing
      with pickle_file_path.open(mode='wb') as pickle_file:
         pickle.dump(json.dumps(api_result.json()), pickle_file)
      #Returns the JSON response from VALUE SERP
      return json.dumps(api_result.json())
   
   def generate_query_with_location(self, company, location):
      #Set parameters
      params = {
         'api_key': self.api_key,
         #Prompt
         'q': company,         
         #Location set to retrieved location
         'location': location,
         #google-domain, gl, and hl are auto-updated based on location
      }
      #Make the GET request to VALUE SERP
      api_result = requests.get('https://api.valueserp.com/search', params)
      #Generates pickle file for output parsing
      pickle_file_path = Path('runs\\company_descriptions\\response_serp_company_location.p')
      # Open the pickle file for writing
      with pickle_file_path.open(mode='wb') as pickle_file:
         pickle.dump(json.dumps(api_result.json()), pickle_file)
      #Returns the JSON response from VALUE SERP
      return json.dumps(api_result.json())


   def get_snippets(self, data):
      #Loads the JSON data into a Python dictionary
      x = data
      h = json.loads(x, strict=False)
      #Retrieves number of relevant snippet blocks
      if (h.get("related_questions") is not None): 
         length = len(h.get("related_questions"))
      else:
          length = 0
      #Creates empty list for storing links
      snippet_list = []
      #For each block, checks if there is an answer from a question block or a preview of a link that can be used as a snippet
      for i in range (length):
         if (h.get("related_questions")[i].get("answer") is not None):
               #Removes trailing characters so clean snippet is appended
               snippet = self.remove_trailing_characters(h.get("related_questions")[i].get("answer"))
               snippet_list.append(snippet)
         else:
               if(h.get("related_questions")[i].get("snippet") is not None):
                  snippet = self.remove_trailing_characters(h.get("related_questions")[i].get("snippet"))
                  snippet_list.append(snippet)
      #Checks all of the organic results
      if (h.get("organic_results") is not None):
         length_organic = len(h.get("organic_results"))
         for i in range (length_organic):
            if (h.get("organic_results")[i].get("snippet") is not None):
               snippet = self.remove_trailing_characters(h.get("organic_results")[i].get("snippet"))
               snippet_list.append(snippet)
      #Returns list of snippets
      return(snippet_list)

   def remove_trailing_characters(self, snippet):
       #Replaces trailing characters with blank character
       snippet = snippet.replace('\u00a0...', '')   
       return snippet
   
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
               link_list.append(h.get("related_questions")[i].get("source").get("link"))
         else:
               if(h.get("related_questions")[i].get("link") is not None):
                  link_list.append(h.get("related_questions")[i].get("link"))
      #Gets organic results snippets
      if (h.get("organic_results") is not None): 
         length = len(h.get("organic_results"))
      else:
          length = 0
      if (h.get("organic_results") is not None):
         length_organic = len(h.get("organic_results"))
         for i in range (length_organic):
            if (h.get("organic_results")[i].get("link") is not None):
               link_list.append(h.get("organic_results")[i].get("link"))
      #Returns list of links
      return(link_list)

serp = SerpGenerator()
print("Initialized?")