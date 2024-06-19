My first serious project. 

Personal chat-bot.

Installation:
1. Git clone https://github.com/Morgrime/gigachatgpt
2. You need to manually create in your local repo folder .streamlit and secrets.toml (so your path to this folder should looks like /<gigachatgpt>/.streamlit/secrets.toml)
3. Put your client_id and client_secret into secrets.toml so it should look like this:

CLIENT_ID = "YOUR CLIENT ID"
SECRET = "YOUR SECRET ID" 

you can find it here: https://developers.sber.ru/studio
4. Then you should be in your repo with main.py, after this run this command: streamlit run main.py
5. Done
