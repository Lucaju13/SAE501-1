FROM python:3.8
RUN pip install scapy
COPY script_sniffer.py /app/
WORKDIR /app
CMD [ "python", "./script_sniffer.py" ]
