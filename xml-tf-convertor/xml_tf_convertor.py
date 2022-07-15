"""

import xml.etree.ElementTree as ET
tree = ET.parse('C:\\Users\\manik\\Downloads\\UntitledDiagram.xml')
root = tree.getroot()
root = tree.getroot()

for book in root:

  print(book.attrib)
"""
"""
import xml.etree.ElementTree as ET
import pandas as pd

xml_data = open('C:\\Users\\manik\\Downloads\\UntitledDiagram.xml', 'r').read()  # Read file
root = ET.XML(xml_data)  # Parse XML

data = []
cols = []
for i, child in enumerate(root):
    data.append([subchild.text for subchild in child])
    cols.append(child.tag)

df = pd.DataFrame(data).T  # Write in DF and transpose it
df.columns = cols  # Update column names
print(df)

"""

from multiprocessing import Value
import xml.etree.cElementTree as ET
import os
path = 'C:\\Users\\manik\\Downloads\\'
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

# Example
createFolder('C:\\Users\\manik\\Downloads\\Cloud-Terraform\\')
print("Step-1: Project Folder Created")

root = ET.parse('C:\\Users\\manik\\Downloads\\UntitledDiagram.xml')

#root = ET.parse ('https://github.com/idatalytics/euclid-azure-draw.io/blob/edc202ccd3414c08e217f23e6a3116a7ccea33d9/Untitled%20Diagram.drawio.xml')


#temperature = root.find('.//object')
for temp in root.findall('.//object'):
    resource = temp.get("label")
    if str(resource) == 'Cloud':
         #createFolder('C:\\Users\\manik\\Downloads\\Cloud-Terraform\\provider')
         #print ("Step-2: Provider Folder Created")
         path = 'C:\\Users\\manik\\Downloads\\Cloud-Terraform'
         file = "provider.tf"
         with open(os.path.join(path, file), 'w') as fp:
             fp.write('terraform { \n')
             fp.write('required_providers { \n')
             fp.write('azurerm = { \n')
             fp.write('source  = "hashicorp/azurerm" \n version = "=3.0.1" ')
             fp.write('} \n } \n } \n')
             fp.write('provider "azurerm" { \n ')
             fp.write('features {} \n')
             subscription_id = temp.get("subscription_id")
             client_id       = temp.get("client_id")
             client_secret   = temp.get("client_secret")
             tenant_id       = temp.get("tenant_id")
             fp.write('subscription_id = ' + '"' + subscription_id  + '"\n')
             fp.write('client_id = ' + '"' + client_id + '"\n')
             fp.write('client_secret = ' + '"' + client_secret + '"\n')
             fp.write('tenant_id = ' + '"' + tenant_id + '"\n')
             fp.write('}')
             fp.close
             print("Step-3:File Created for Provider")
             pass
                          
    elif str(resource) == 'Resource Group':
         path = 'C:\\Users\\manik\\Downloads\\Cloud-Terraform'
         file = "main.tf"
         name = temp.get ("name")
         location = temp.get("location")
         with open(os.path.join(path, file), 'w') as fp:
             fp.write('resource "azurerm_resource_group" "rg1" { \n')
             fp.write('name = ' + '"' + name + '"\n')
             fp.write('location =' + '"'+ location + '"\n')
             fp.write('}')
             fp.close
             createFolder('C:\\Users\\manik\\Downloads\\Cloud-Terraform\\resource-group')
         print("Its Resource group")
    else:
        print("Its not working")
   

""""

import xml.etree.ElementTree as et

data = []
for (ev, el) in et.iterparse('C:\\Users\\manik\\Downloads\\UntitledDiagram.xml'):
    inner = []

    if el.tag == 'object':        
        for name, value in el.items():
            inner.append([name, str(value).replace('\n','').replace(' ','')])
        for i in el:
            if str(i.text) != 'None':
                inner.append([i.tag, str(i.text).replace('\n','').replace(' ','')])

            for name, value in i.items():
                inner.append([name, str(value).replace('\n','').replace(' ','')])
        data.append(inner)

print(data)
"""