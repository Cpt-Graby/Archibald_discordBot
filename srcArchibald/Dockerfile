FROM python:3.11

ADD main.py inventory.py settings.py ../.env ./

RUN mkdir logs
RUN pip install --upgrade pip && pip install discord.py python-dotenv

CMD ["python", "./main.py"]
