import urllib.request

TEST_URL="https://spiral.imperial.ac.uk/simple-search?location=&query=&filter_field_1=author&filter_type_1=contains&filter_value_1=Chittenden&rpp=10&sort_by=dc.date.issued_dt&order=DESC&etal=5"
contents = urllib.request.urlopen(TEST_URL).read().decode()

#Data is arranged in a table and is the only table on the page. Here I remove the HTML before/after the table and then break it down into rows.
table_line = '<table align="center" class="table" summary="This table browses all dspace content">'
top_split = contents.split(table_line)[1]
table = top_split.split("</table>")[0].split("<tr>")[1:]

for line in table:
    print(line)
