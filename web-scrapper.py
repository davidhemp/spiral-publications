import urllib.request
import re

def get_column_names(line):
    pattern = '>([a-zA-Z1-9 ()]+)<'
    result = re.findall(pattern, line)
    print(result)


def get_publication_date(line):
    pattern = '>([a-zA-Z0-9\-]+)<'
    result = re.findall(pattern, line)
    return result[0]

def get_publication_title(line):
    url = get_publication_url(line)
    pattern = '(?<=\<a href="{}"\>)(.+)(?=\<\/a\>)'.format(url)
    result = re.findall(pattern, line.replace('&#x20;', ' '))
    return result[0]

def get_publication_url(line):
    pattern = '<a href="([\/a-z0-9]+)"'
    result = re.findall(pattern, line)
    return result[0]

def get_publication_authors(line):
    pattern = '(?<=\<em\>)(.+)(?=\<\/em\>)'
    result = re.findall(pattern, line.replace('&#x20;', ' '))
    return result[0]

TEST_URL='https://spiral.imperial.ac.uk/simple-search?location=&query=&filter_field_1=author&filter_type_1=contains&filter_value_1=Chittenden&rpp=10&sort_by=dc.date.issued_dt&order=DESC&etal=5'
contents = urllib.request.urlopen(TEST_URL).read().decode()

#Data is arranged in a table and is the only table on the page. Here I remove the HTML before/after the table and then break it down into rows.
table_line = '<table align="center" class="table" summary="This table browses all dspace content">'
top_split = contents.split(table_line)[1]
table = top_split.split('</table>')[0].split('<tr>')[1:] # The final split also removes the leading colgroup info

header_line = table[0]
get_column_names(header_line)
for line in table[1:]:
        items = line.split('</td>')
        print(get_publication_authors(line.split("/td")[2]))
        print(get_publication_title(items[1]))
        print( get_publication_date(line.split("/td")[0]))
        print("")
