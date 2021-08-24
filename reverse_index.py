# url1, [keyword:freq] ...
# url2, [keyword:freq] ...

# To:

# keyword1, [url:freq] ...
# keyword2, [url:freq] ...

import csv
import json
import codecs

src = 'mySpider/data.csv'
dst = 'mySpider/data-reverse.csv'

def load_csv_file(filename):
    rows = []
    with open(filename,encoding='UTF-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            index = 1
            row[index] = row[index].replace("'", '"')
            row[index] = json.loads(row[index])
            rows.append(row)
    return rows

rows = load_csv_file(src)

reverse_map = {}
for row in rows:
    url = row[0]
    freq_dict = row[1]
    for keyword, freq in freq_dict.items():
        if keyword not in reverse_map:
            reverse_map[keyword] = {}
        if freq != 0:
            reverse_map[keyword][url] = freq

fieldnames = ['keyword', 'freq_dict']
f = codecs.open(dst, 'w', 'UTF-8')
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()
for keyword, freq_dict in reverse_map.items():
    print(keyword, freq_dict)
    writer.writerow({'keyword': keyword, 'freq_dict': str(freq_dict)})
