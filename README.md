

# Библиотеки

- Python 3.11.6
- Streamlit 1.35.0
- Requests 2.31.0

# Установка:
1. `Git clone https://github.com/Morgrime/gigachatgpt`
2. Вам нужно вручную создать в вашем репозитории с кодом папку .streamlit, а внутри файл secrets.toml, где будут хранится ваши апи ключи (конечный путь до secret.toml должен выглядеть так: /<gigachatgpt>/.streamlit/secrets.toml)
3. Запишите в **secrets.toml** ваши CLIENT_ID и SECRET_ID чтобы вы последствии это выглядело так (после регистрации вы можете найти их [тут](https://developers.sber.ru/studio)):

    ```toml
    CLIENT_ID = "YOUR CLIENT ID"
    SECRET = "YOUR SECRET ID" 
    ```

1. Зайдите в ваш репозиторий с файлом main.py и запустите следующую команду: `streamlit run main.py` 

2. У вас откроется сайт с чат-ботом где вы сможете задавать вопросы.

# TODO:
- [x] Бот отвечает на вопросы 
- [x] Генерация картинок
- [ ] Работа с историей чата
- [ ] Сделать так чтобы папка .streamlit с файлом secret.toml появлялись сами без вручного создания