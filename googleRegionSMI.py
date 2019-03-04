import os, time
from time import gmtime, strftime


URL = "https://www.google.ru/"

REGION = [
'snews.ru',
'irkutsk.aldana.ru',
'irkutsk.monavista.ru',
'ircity.ru',
'irk.gov.ru',
'baikvesti.ru',          #http://meyerweb.com/eric/tools/dencoder/
'sibinform.com',
'www.irk.aif.ru',
'irkutsk.monavista.ru',
'irkutsk-news.com',
'newirkutsk.ru',
'irkutsk.bezformata.ru',
'altairk.ru',
'irk-vesti.ru',
'babr.ru',
'newirkutsk.ru',
'admirk.ru',
'irkutsk.newsbomb.ru',
'irktorgnews.ru',
'irkutsk.smizz.ru',
'irkutsk.monavista.ru',
'irksib.ru',
'baikal-info.ru',
'irk.ru',
'irkutskmedia.ru',
'as.baikal.tv'
]


#БЮДЖЕТ
#бюджет | "бюджета" | "расходование" | "заложено в бюджет" | региональный | "траты" 
B = ' %D0%B1%D1%8E%D0%B4%D0%B6%D0%B5%D1%82%20%7C%20%22%D0%B1%D1%8E%D0%B4%D0%B6%D0%B5%D1%82%D0%B0%22%20%7C%20%22%D1%80%D0%B0%D1%81%D1%85%D0%BE%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%22%20%7C%20%22%D0%B7%D0%B0%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%BE%20%D0%B2%20%D0%B1%D1%8E%D0%B4%D0%B6%D0%B5%D1%82%22%20%7C%20%D1%80%D0%B5%D0%B3%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%7C%20%22%D1%82%D1%80%D0%B0%D1%82%D1%8B%22%20%0A'


#ДЕТИ
#"дошкольное образование" | детский | детсад | "новости дошкольн" | "дети-инвалиды" | инклюзивное | "дошкольное развитие" | "дети с ограниченными" | коррекционный | "детского сада"
KIDS = ' %22%D0%B4%D0%BE%D1%88%D0%BA%D0%BE%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%22%20%7C%20%D0%B4%D0%B5%D1%82%D1%81%D0%BA%D0%B8%D0%B9%20%7C%20%D0%B4%D0%B5%D1%82%D1%81%D0%B0%D0%B4%20%7C%20%22%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8%20%D0%B4%D0%BE%D1%88%D0%BA%D0%BE%D0%BB%D1%8C%D0%BD%22%20%7C%20%22%D0%B4%D0%B5%D1%82%D0%B8-%D0%B8%D0%BD%D0%B2%D0%B0%D0%BB%D0%B8%D0%B4%D1%8B%22%20%7C%20%D0%B8%D0%BD%D0%BA%D0%BB%D1%8E%D0%B7%D0%B8%D0%B2%D0%BD%D0%BE%D0%B5%20%7C%20%22%D0%B4%D0%BE%D1%88%D0%BA%D0%BE%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D1%80%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5%22%20%7C%20%22%D0%B4%D0%B5%D1%82%D0%B8%20%D1%81%20%D0%BE%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D0%BD%D0%BD%D1%8B%D0%BC%D0%B8%22%20%7C%20%D0%BA%D0%BE%D1%80%D1%80%D0%B5%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9%20%7C%20%22%D0%B4%D0%B5%D1%82%D1%81%D0%BA%D0%BE%D0%B3%D0%BE%20%D1%81%D0%B0%D0%B4%D0%B0%22%0A'
#"дети-инвалиды" | инклюзивное | "дети с ограниченными" | коррекционный 
IN = ' %22%D0%B4%D0%B5%D1%82%D0%B8-%D0%B8%D0%BD%D0%B2%D0%B0%D0%BB%D0%B8%D0%B4%D1%8B%22%20%7C%20%D0%B8%D0%BD%D0%BA%D0%BB%D1%8E%D0%B7%D0%B8%D0%B2%D0%BD%D0%BE%D0%B5%20%7C%20%22%D0%B4%D0%B5%D1%82%D0%B8%20%D1%81%20%D0%BE%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D0%BD%D0%BD%D1%8B%D0%BC%D0%B8%22%20%7C%20%D0%BA%D0%BE%D1%80%D1%80%D0%B5%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9%20%0A'

#МОДЕРНИЗАЦИЯ ОБРАЗ.
#образования | "учебный процесс" | "модернизация образования" | "инновации образовательного" | "концепция образования" | "законодательство в сфере образования"| "школу построят"| "строительство школы" | "новая школа" | школы
MODERN = ' %D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20%7C%20%22%D1%83%D1%87%D0%B5%D0%B1%D0%BD%D1%8B%D0%B9%20%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D1%81%D1%81%22%20%7C%20%22%D0%BC%D0%BE%D0%B4%D0%B5%D1%80%D0%BD%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%22%20%7C%20%22%D0%B8%D0%BD%D0%BD%D0%BE%D0%B2%D0%B0%D1%86%D0%B8%D0%B8%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE%22%20%7C%20%22%D0%BA%D0%BE%D0%BD%D1%86%D0%B5%D0%BF%D1%86%D0%B8%D1%8F%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%22%20%7C%20%22%D0%B7%D0%B0%D0%BA%D0%BE%D0%BD%D0%BE%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D1%82%D0%B2%D0%BE%20%D0%B2%20%D1%81%D1%84%D0%B5%D1%80%D0%B5%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%22%7C%20%22%D1%88%D0%BA%D0%BE%D0%BB%D1%83%20%D0%BF%D0%BE%D1%81%D1%82%D1%80%D0%BE%D1%8F%D1%82%22%7C%20%22%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D1%82%D0%B2%D0%BE%20%D1%88%D0%BA%D0%BE%D0%BB%D1%8B%22%20%7C%20%22%D0%BD%D0%BE%D0%B2%D0%B0%D1%8F%20%D1%88%D0%BA%D0%BE%D0%BB%D0%B0%22%20%7C%20%D1%88%D0%BA%D0%BE%D0%BB%D1%8B%0A'


counter = 1200

def t():
    global counter
    while counter != 0:
        date = strftime("%H:%M:%S") 
        print(date, ' %d' % counter, end=' \r')
        time.sleep(1)
        counter -= 1
        
def budget():
    for i in REGION:
        os.startfile(URL + '#newwindow=1&q=site:' + i + 
        B + '&newwindow=1&tbs=' +  
        'cdr:1,cd_min:8.21.2017,cd_max:8.22.2017,lr:lang_1ru&lr=lang_ru')
    print('-------------------------------------')

def k():
    for i in REGION:
        os.startfile(URL + '#newwindow=1&q=site:' + i + 
        KIDS + '&newwindow=1&tbs=' +  
        'cdr:1,cd_min:8.21.2017,cd_max:8.22.2017,lr:lang_1ru&lr=lang_ru')
    print('-------------------------------------')
    
def i():
    for i in REGION:
        os.startfile(URL + '#newwindow=1&q=site:' + i + 
        IN + '&newwindow=1&tbs=' +  
        'cdr:1,cd_min:8.21.2017,cd_max:8.22.2017,lr:lang_1ru&lr=lang_ru')
    print('-------------------------------------')
    
def modern():
    for i in REGION:
        os.startfile(URL + '#newwindow=1&q=site:' + i + 
        MODERN + '&newwindow=1&tbs=' +  
        'cdr:1,cd_min:8.21.2017,cd_max:8.22.2017,lr:lang_1ru&lr=lang_ru')
t()
budget()
