import pandas as pd

html_df = pd.read_html('https://www.ndbc.noaa.gov/station_page.php?station=42099')
print(len(html_df))
counter = 0
for table in html_df:
  print('Table {}'.format(counter))
  print(table.columns)
  # print(table.info())
  # print(table)
  counter +=1

