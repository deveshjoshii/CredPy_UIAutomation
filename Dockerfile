From python:3.11
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY --chown=1001 . .
RUN chmod +x start.sh
CMD ["sh","-c","./start.sh $endpoint"]