FROM python:3.10
WORKDIR /Question 2
COPY . /Question 2
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "Question 2.py"]
