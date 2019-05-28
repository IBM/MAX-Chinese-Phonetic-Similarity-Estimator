FROM codait/max-base:v1.1.1

WORKDIR /workspace

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD python app.py
