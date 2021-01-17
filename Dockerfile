# 1
FROM python:3.7

# 2
RUN pip install Flask gunicorn

# 3
COPY / /main
WORKDIR /main

# 4
ENV PORT 8080

# 5
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:main