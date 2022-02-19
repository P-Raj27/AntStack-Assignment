#Note-For Instructions please see Description of this File.
import requests
import json
path_Of_Input_File="Please Paste the Path Here"           #Enter the Path of the File Here
text=open(path_Of_Input_File,"r")
text=text.read()
JSON_ARRAY_STRING=text
url="Please Paste the URL here"+"/Store/"+JSON_ARRAY_STRING    #Paste the URL Obtained here
data={
    "JSONArray":JSON_ARRAY_STRING
}
r1=requests.get(url)
jsonList=((r1.json()))
totalAmount=0
totalTax=0
jsonList=(sorted(jsonList,key=lambda x:x['item']))      
for i in jsonList:
    print(f"Item = {i['item']} , Final Price = {i['final_price']} , Tax Amount = {i['tax_amount']}, Tax Rate = {i['tax_rate']*100}% ")
for i in jsonList:
    totalAmount=totalAmount+i['final_price']
    totalTax=totalTax+i['tax_amount']
if(totalAmount>=2000):
    totalAmount=totalAmount-totalAmount*0.05
print(f"Total Tax on the Purchased Commodity ={totalTax}")
print(f"Total Amount to pay ={totalAmount}")
