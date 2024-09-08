FROM python:3.9-slim

WORKDIR /app

COPY tests/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY totara ./totara/

COPY tests ./tests/

COPY setup.py .

RUN pip install .

COPY run_tests.sh .

RUN chmod +x ./run_tests.sh
