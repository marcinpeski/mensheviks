import os

main_dir = os.getcwd() + '\\'
file_dir = main_dir + 'files\\council meetings\\'
output_dir = main_dir + '_councilmeetings\\'

months = {'01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}

files = os.listdir(file_dir)
for filename in files:
    [year, rest] = filename.split('.')[0].split('-')
    month_code = rest[:2]
    day_code = '01'
    month = months[month_code]
    if len(rest)>2:
        add = rest[2:]
    else:
        add = ''
    output_name = year+'-'+month_code+'-'+'01'+'-'+'Council-'+year+'-'+month+'.markdown'
    f = open(output_dir+output_name, 'w')
    f.write('---\n')
    f.write('layout: meetings\n')
    f.write('author: \"Marcin Peski\"\n')
    f.write('title:  "'+month+' '+year+'"\n')
    f.write('date:   '+year+'-'+month_code+'-'+day_code+' 00:00:01 -0400\n')
    f.write('last_modified:\n')
    f.write('categories: meeting\n')
    f.write('url_agenda: "/files/council meetings/'+filename+'"\n')
    f.write('tags: \n')
    f.write('highlights: \n')
    f.write('---\n')
    f.close()
