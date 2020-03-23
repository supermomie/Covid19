import os
import json



path = "/mnt/47f9603a-2ace-4cad-a116-2167bd2496cd/datasets/CORD-19-research-challenge"
dirs = path + "/biorxiv_medrxiv/biorxiv_medrxiv"


for d in dirs:
    for f in os.listdir(f"{dirs}"):
        file_name = f"{dirs}/{f}"
        j = json.load(open(file_name, "rb"))
        #print(j)
        title = j['metadata']['title']
        try:
            abstract = j['abstract'][0]
        except:
            #print(j['abstract'])
            abstract = ""
        full_text = ""
        for text in j['body_text']:
            full_text += text['text'] + "\n\n"
        print(full_text)
        break
