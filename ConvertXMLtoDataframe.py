#File Name- Convert XML to dataframe
#Author- Kanishka Narayan (kanishkan91@gmail.com)


import xml.etree.cElementTree as et
import pandas as pd

Year=[]
Gas=[]
Value=[]
Technology=[]
Crop=[]
Country=[]

tree=et.parse(r'C:\GCAM Windows\input\gcamdata\xml\all_aglu_emissions.xml')
root=tree.getroot()

for x in root.iter('region'):
    root1=et.Element('root')
    root1=x
    for supply in root1.iter('AgSupplySector'):
        root2=et.Element('root')
        print(supply)
        root2=(supply)
        for tech in root2.iter('AgProductionTechnology'):
            root3 = et.Element('root')
            root3=(tech)
            for yr in root3.iter('period'):
                root4 = et.Element('root')
                root4=yr
                for gas in root4.iter('Non-CO2'):
                    root5 = et.Element('root')
                    root5=gas
                    for em in root5.iter('input-emissions'):
                        Technology.append(tech.attrib['name'])
                        Value.append(em.text)
                        Gas.append(gas.attrib['name'])
                        Year.append(yr.attrib['year'])
                        Crop.append(supply.attrib['name'])
                        Country.append(x.attrib['name'])


print('Creating dataframe')

test_df = pd.DataFrame({'Year': Year,'Gas':Gas,'Value':Value,'Technology':Technology,'Country':Country,'Crop':Crop })
print(test_df.head())

test_df.to_csv('TestXML.csv')






