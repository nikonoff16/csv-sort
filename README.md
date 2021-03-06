# csv-sort
Предыстория:
----------------------
Выполняя свои должностные обязанности, каждый участковый 
терапевт должен иметь в кабинете списки подлежащих диспансеризации
людей, равно как и план по приглашению на нее. 
Обработать участок в несколько тысяч человек - не самое 
простое мероприятие, поэтому я и написал этот парсер таблиц. 

Что он умеет делать:
----------------------
Программа сортирует списки в соответствии с годом рождения человека.
Она умеет делать разбивку граждан по месяцам - делать примерный
план работы на месяц - по разным видам диспансеризации. 
Допустимой опцией является вывод списка без распределения по 
месяцам. Подгрузив один список, пользователь получает на выход
столько списков, сколько прописано у него в конфигурационном файле
<b>years_of_disp.json</b>. 

Предварительная настройка
-----------------------
За разбивку любей по годам отвечает конфигурационный файл
<i>years_of_disp.json</i>. На данный момент он настроен на работу с
майским приказом 2019 года по диспансеризации, но ничто не мешает вам
внести в него правки в соответстии с нормативными документами или годом,
когда вы его запускаете. 

Как пользоваться программой:
-----------------------
Скрипт написан на <i>Python</i>, так что для работы нужен установленный 
в систему интерпретатор этого языка версии не ниже 3.5. Программа не имеет
графического интерфейса, так что нужно будет с помощью командной строки 
переместиться в директорию ее расположения. 

Скрипт принимает на вход только списки в формате <i>.csv</i>. 
Обычно табличные редакторы позволяют перевести текст из их формата в 
csv, так что заранее самостоятельно переведите в него нужные файлы.
В ином случае никакого адевкатного результата ожидать не следует.

Если вы желаете обработать сразу несколько участков за один вызов программы,
то при подготовке файлов указывайте в названии каждого номер участка, к 
которому они относятся. Номер следует указывать цифрами и в самом начале,
но если в названии нет других цифр, то можно в любом произвольном месте.
Скрипт умеет находить в названии номер (цифру) и помещать ее в начало всех файлов, 
которые будут созданы скриптом из исходного. Следите за тем, чтобы не было
повторяющихся номеров участков - иначе программа перезапишет уже сделанные 
списки новыми, и это вряд ли вас порадует.  

Подготовленные списки нужно поместить в директорию, где расположен скрипт.
Далее нужно сделать вызов программы:

<i> > python start_sort.py dist1.csv dist2.csv</i>

Так вы его сможете запустить на Windows, если python прописан в Path 
(обычно это указывается при установке, но если у вас не так, то вручную
добавьте интерпретатор туда). 

<i>~ python3 start_sort.py dist1.csv dist2.csv</i>

Так этот вызов следует делать в Unix системах, но их использование пока
не рекомендуется, в силу нерешенных проблем с кодировками, о чем подробнее 
будет сказано в разделе <b>Известные проблемы</b>

<i>start_sort.py</i> является точкой входа в программу. Остальные модули 
вызываются этим, и самостоятельно вызваны быть не могут. 

За названием скрипта вам следует перечислить вручную все файлы, которые 
желаете обработать. Разделять их нужно пробелом, запятые не допускаются. 
Если вы случайно вызовете скрипт без аргументов, программа сообщит вам
об этом. 

Далее программа спросит, желаете ли вы просто список подлежащих диспансеризации, 
или список с распределением по месяцам. Действие по умолчанию - с разбивкой, 
в ином случае следует ответить на приглашение явным согласием (ввести "Да" в консоль).


Далее никаких действий уже не требуется. Если одно или несколько имен  были
введены с ошибкой (не указано расширение, пропущен символ или символ в неверном регистре),
то программа сообщит вам об этом, но продолжит выполнение, если в списке есть
еще введенные вами файлы. По результату вы получите новые списки только для тех 
файлов, которые ввели верно. 
В конце своей работы программа также напомнит о том, что не все файлы были 
обработаны, если у нее это не получилось. 

Искать новые файлы следует в той же директории, где расположен скрипт.

Известные проблемы
------------------
 Алгоритм сортировки основан на сравнении года рождения, но программа заранее
 не может знать, где он находится, поэтому в первой строке она ищет регулярным
 выражением подходящий столбец. Если даты написаны не стандартно в формате
 <i>ДД.ММ.ГГГГ</i> (разделитель может быть любой), то результат работы
 будет очень далек от того, что хотелось бы получить. 
 
 Также проблемой является то, что даже на Windows-машинах безболезненно 
 перевести .xls в .csv не всегда получается. При этом успешно обработанные 
 в Windows файлы в Linux превращаются в нечто нечитабельное. Эту проблему еще 
 предстоит решить.
 
 Контактная информация и дисклеймер
 -------------------
 Автор создал этот скрипт только в личных учебных и рабочих целях, 
 и ни как не отвечает за возможный ущерб, который может быть причинен 
 его использованием, так что пользоваться им вы можете только на свой страх и риск 
 (подробнее о своих правах и прочих последствиях использования этого ПО
 вы можете ознакомиться в лицензии MIT, которую вы принимаете фактом использования, модификации и 
 прочих действий с этим скриптом)
 
Связаться с автором можно по почте: <i>i.nikonoff16@gmail.com</i>
