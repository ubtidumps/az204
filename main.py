from bs4 import BeautifulSoup
finalhtml = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AZ 204 Dumps</title>
        <!-- deflink == defered link (loaded later by jquery) -->
    <!-- bootstrap v4 css -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="css/style.css">

</head>
<body>
    
'''
question_count = 1
for i in range(1, 49):
    with open(f'AZ-204 Exam – Page{i}.html', encoding='utf8') as f:
        content = f.read()
        soup = BeautifulSoup(content, features='html.parser')
        for ele in soup.find_all('div', {'class': 'questions-container'}):
            for header in ele.find_all('div',{'class':'exam-question-card'}):
                header.div.next.string.replace_with(f'Question #{question_count}')
                question_count+=1
            for remove in ele.find_all('a', {'class': ['question-discussion-button']}):
                remove['href'] = '#'
            for img in ele.find_all('img', {'class': 'in-exam-image'}):
                img['src'] = "images/"+img['src'].split("/")[-1].split('.')[0]
            finalhtml += ele.prettify()+'<br/>'
finalhtml += '''

'''
with open('index.html', 'w', encoding='utf8') as f1:
    f1.write(finalhtml)

import glob
for i in range(1,49):
    # print(glob.glob(f'AI-900 Exam – Page{i}_files/^[0-9]*.png'))
    for dir in glob.glob(f'AZ-204 Exam – Page{i}_files/[0-9]*.png'):
        fname = dir.split("\\")[-1]
        with open(dir, 'rb') as img1, open(f'images/{fname}', 'wb') as img2:
            img2.write(img1.read())
