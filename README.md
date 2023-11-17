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

запуск
pytest --url="http://localhost:80" --log_level=DEBUG
pytest tests/test_with_page_object.py --url="http://localhost:80" --log_level=DEBUG 
pytest tests/test_find_elements.py --url="http://localhost:80" --log_level=INFO    

