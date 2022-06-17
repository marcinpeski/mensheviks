import os, os.path, re

main_dir = os.getcwd() + '\\'
file_dir = main_dir + 'files\\council meetings\\'
output_dir = main_dir + '_councilmeetings\\'

months = {'01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}
month_codes = {**{'Jan':'01', 'Feb':'02', 'Sep':'09', 'Sept':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}, **{months[c]:c for c in months}}
information = {
    'layout':'meetings\n',
    'author':'\"Marcin Peski\"\n',
    'title':'',
    'date':'',
    'last_modified':'\n',
    'categories':'meeting\n',
    'url_agenda':'',
    'tags':'\n',
    'highlights':'\n',
    'excerpt_separator':'<!--more-->\n',
    'excerpt':'',
    'contents':'',
}


files = os.listdir(file_dir)
for filename in files:
    if filename[:2] == '20':
        [year, rest] = filename.split('.')[0].split('-')
        month_code = rest[:2]
        day_code = '01'
        month = months[month_code]
        if len(rest)>2:
            add = rest[2:]
        else:
            add = ''
    else:
        elems = re.split(r'[ ._-]+', filename)
        [month_name, day_code, year_code] = elems[:3]
        month_code = month_codes[month_name]
        month = months[month_code]
        
    output_name = year+'-'+month_code+'-'+'01'+'-'+'Council-'+year+'-'+month+'.markdown'
    info = information.copy()
    if os.path.exists(output_dir+output_name):
        f = open(output_dir+output_name, 'r')
        lines = f.readlines()
        lines = lines[1:]
        head, excerpt, contents = True, False, False
        for line in lines:
            if line == '---\n':
                head, excerpt = False, True
            elif line == '<!--more-->\n':
                head, excerpt, content = False, False, True
            elif head:
                [i, b] = line.split(':', 1)
                info[i] = b 
            elif excerpt:
                info['excerpt'] = info['excerpt'] + line
            elif content:
                info['contents'] = info['contents'] + line
        f.close()
    else:
        info['title'] = info['title']+ month + ' ' + year + '"\n'
        info['date'] = year+'-'+month_code+'-'+day_code+' 00:00:01 -0400\n'
        info['url_agenda'] = '/files/council meetings/'+filename+'\n'
    
    #write file
    f = open(output_dir+output_name, 'w')
    f.write('---\n')
    for i in info:
        if not i in ['excerpt', 'contents']:
            f.write(i+': '+info[i])
    f.write('---\n')
    if info['excerpt'] != '':
        f.write(info['excerpt'])
    f.write(info['excerpt_separator'])
    f.write(info['contents'])
    f.close()
