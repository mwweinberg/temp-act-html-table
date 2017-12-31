import pandas as pd
import numpy as np

#load the csv as the dataframe with only the columns you care about
df = pd.read_csv('input.csv', usecols = ['Organization Name (English)', 'Organization Name (Chinese)', 'Organization Origin', 'Chinese Partner Unit (English)', 'Chinese Partner Unit (Chinese)', 'Activity Name (English)', 'Activity Name (Chinese)', 'Activity Location (English)', 'Activity Location (Chinese)', 'Start Date', 'End Date'])


#reorders the columns
columnsTitles = ['Organization Name (English)', 'Organization Name (Chinese)', 'Organization Origin', 'Chinese Partner Unit (English)', 'Chinese Partner Unit (Chinese)', 'Activity Name (English)', 'Activity Name (Chinese)', 'Activity Location (English)', 'Activity Location (Chinese)', 'Start Date', 'End Date']
df = df.reindex(columns=columnsTitles)

#prevents truncation of field data
pd.set_option('max_colwidth', -1)

df.style.render()

#print(df)

#outputs html to a file
#index = false is to avoid printing the index column
#df.to_html('output.html', index = False, classes = ['tableizer-firstrow'], border = 0)
new_table = df.to_html(index = False, classes = ['tableizer-firstrow'], border = 0)

#removes the formatting
#changes the formatting for the table headers
#I'm sure there is a more elegant way of doing this but I don't know it
fixed_table_1 = new_table.strip('<table border="0" class="dataframe tableizer-firstrow">')
fixed_table_2 = fixed_table_1.replace('<th>Organization Name (English)</th>', '<th style="width:10%">Organization Name (English)</th>')
fixed_table_3 = fixed_table_2.replace('<th>Organization Name (Chinese)</th>', '<th style="width:10%">Organization Name (Chinese)</th>')
fixed_table_4 = fixed_table_3.replace('<th>Organization Origin</th>', '<th style="width:10%">Organization Origin</th>')
fixed_table_5 = fixed_table_4.replace('<th>Chinese Partner Unit (English)</th>', '<th style="width:10%">Chinese Partner Unit (English)</th>')
fixed_table_6 = fixed_table_5.replace('<th>Chinese Partner Unit (Chinese)</th>', '<th style="width:10%">Chinese Partner Unit (Chinese)</th>')
fixed_table_7 = fixed_table_6.replace('<th>Activity Name (English)</th>', '<th style="width:10%">Activity Name (English)</th>')
fixed_table_8 = fixed_table_7.replace('<th>Activity Name (Chinese)</th>', '<th style="width:10%">Activity Name (Chinese)</th>')
fixed_table_9 = fixed_table_8.replace('<th>Activity Location (English)</th>', '<th style="width:10%">Activity Location (English)</th>')
fixed_table_10 = fixed_table_9.replace('<th>Activity Location (Chinese)</th>', '<th style="width:10%">Activity Location (Chinese)</th>')
fixed_table_11 = fixed_table_10.replace('<th>Start Date</th>', '<th style="width:5%">Start Date</th>')
fixed_table_12 = fixed_table_11.replace('<th>End Date</th>', '<th style="width:5%">End Date</th>')

#add the bits at the end of the html
#could do this with a seperate file but it is small enough that this seems easier

#fixed_table_13 = fixed_table_12.replace('</table>', '</table> <!–– add your tableizer data above this line––> </body> </html>')

fixed_table = fixed_table_12

print(fixed_table)

top_half = open('site_top.html', 'r')

output_page = open('tempacttable.html', 'w')


for item in top_half:
    output_page.write(item)

for item in fixed_table:
    output_page.write(item)

output_page.write("table> <!–– add your tableizer data above this line––> </body> </html>")

top_half.close()
output_page.close()
