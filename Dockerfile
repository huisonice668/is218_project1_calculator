FROM python:3.9

ADD src /src

CMD ["python", "./src/CalculatorTests.py"]