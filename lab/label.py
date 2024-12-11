import pandas as pd
from IPython.display import HTML


labelscsv = pd.read_csv('/Users/chrimar3/projects/sample-project/dogbreeds/data/labels.csv')
labelscsv = labelscsv.head(5)
result = labelscsv.to_html()


text_file = open("/Users/chrimar3/projects/html/djsite/lab/labels.html", "w")
text_file.write(result)
text_file.close()