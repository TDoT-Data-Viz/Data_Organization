import arcpy
import pandas as pd
import os

layer = arcpy.GetParameterAsText(0)
dest = arcpy.GetParameterAsText(1)

output_path = os.path.join(dest, os.path.basename(layer)+"_Data_Dict.csv")
arcpy.AddMessage(output_path)
# Create a list of fields using the ListFields function
fields = arcpy.ListFields(layer)

# Empty list that will become a list of lists for csv
lists=[]
# Create Search Cursor
cur = arcpy.SearchCursor(layer)

# Iterate through fields in layer and store wanted property values.
for field in arcpy.ListFields(layer):
    n = next(cur, None)
    lists.append([field.name, field.aliasName, field.type, n.getValue(field.name)])

df = pd.DataFrame(lists)
df.columns = ["Field", "Alias", "Data Type", "Example"]
df.to_csv(output_path)   