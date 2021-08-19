import urllib.request

TEST_URL="https://spiral.imperial.ac.uk/simple-search?location=%2F&query=&rpp=10&sort_by=score&order=desc&filter_field_1=author&filter_type_1=contains&filter_value_1=Chittenden"
contents = urllib.request.urlopen(TEST_URL).read()
