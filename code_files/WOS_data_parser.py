import os
import pandas as pd
import re

def extract_wos_data(author_excel):
    author_info = {}
    summary = pd.read_excel(author_excel,nrows=4, skiprows=4).iloc[:,:2]
    summary.columns = ["Keys","Values"]
    pub_data = pd.read_excel(author_excel,skiprows=10)
    author_info["total_citation"] = summary[summary["Keys"] == "Sum of the Times Cited"]["Values"].iloc[0]
    author_info["hindex"] = summary[summary["Keys"] == "h-index"]["Values"].iloc[0]
    author_info["Years active"] = pub_data["Publication Year"].max() - pub_data["Publication Year"].min()
    author_info["No_of_publication"] = summary[summary["Keys"] == "Results found"]["Values"].iloc[0]
    return author_info

path = os.getcwd()+"\\WOS Files\\"
WOS_data = {}

for x in os.listdir(path):
    name = re.sub(".xls","",x)
    file_path = path + x
    WOS_data[name] = extract_wos_data(file_path)
    
wos_dataframe = pd.DataFrame(WOS_data).T
wos_dataframe.to_csv("WOS_data.csv")
