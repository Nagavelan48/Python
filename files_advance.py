import json
import yaml
# with open("D:\\Multicoreware\\Python-Learnings\\sample.txt","a+") as f:
#     # f.seek(0)
#     f.write("\nGood Night")
#     f.seek(0)
#     cont = f.read()
#     print(cont)

# with open("D:\\Multicoreware\\Python-Learnings\\sample.txt","r") as re:
    
data ={"name": "Rocky", "age": 22, "Study":"MCA"}
# json_convert=json.dumps(data)
# print(json_convert)                    #convert dict to json

# with open("file.json","w") as f:
#     json.dump(data,f,indent=3)       #save the json file

# with open("file.json","r") as o:
#     cont = json.load(o)               #convert the json into the dictionary
#     print(cont)

with open("file.yaml","w") as f:
    yaml.dump(data,f)                   #create and write the yaml file

with open("file.yaml","r") as o:
    cont = yaml.safe_load(o)                #read the yaml file
    print(cont)