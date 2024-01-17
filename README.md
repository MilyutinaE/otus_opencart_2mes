# otus_opencart_2mes
домашка по опенкарту 

запуск из терминала:
(по умолчанию открывает опенкарт в хроме)
pytest

в режиме headless (по умолчанию в хроме)
pytest --headless  

в edge браузере
pytest --browser=edge

в edge браузере открыть яндекс
pytest --browser=edge --url="https://ya.ru/" 

в opera браузере в headlessflake
pytest --browser=opera --headless

--url="http://localhost:80"  (еще можно подставить айпи адрес вместо localhost)

ЗАПУСК НА ЛОКАЛЬНОЙ МАШИНЕ: запустить докер в докер-десктоп
опенкарт находится по адресу http://localhost:80
pytest tests/test_with_page_object.py  --log_level=DEBUG 
pytest tests/test_find_elements.py  --log_level=INFO  
pytest tests/test_find_elements.py  --browser="edge" 

запустили тесты, потом аллюр
D:\programsfortests\allure\allure-2.24.1\bin\allure.bat generate allure-results\ --clean
потом в аллюр-репорт открыть индекс.хтмл и открыть в хроме




ЗАПУСК В ВИРТУАЛКЕ (http://192.168.0.105): открываем виртуалку, запускаем опенкарт docker-compose up -d
на хосте запускаем из терминала 

pytest  --executor="192.168.0.105" --log_level=INFO  --remote=True --user="X" --password="XXXX"

по умолчанию будут в хроме. можно добавить  --browser="firefox"
на виртуалке можно открыть селеноид http://localhost:8080/ 
в конфтесте можно включить или выключить видео 
"enableVNC": True, "enableVideo": False

после прогона тестов можно также открыть аллюр репорт
D:\programsfortests\allure\allure-2.24.1\bin\allure.bat generate allure-results\ --clean
потом в аллюр-репорт открыть индекс.хтмл и открыть в хроме


how to work with dockerfile (on my VMware):
1. open linux terminal
2. build dockerfile
docker build -t tests .
3. run
docker run --rm tests --executor="192.168.244.128"  --remote=true --user="X" --password="X"