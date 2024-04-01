# Using same version as og project
FROM python:3.12.1

# Set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY = 'django-insecure-+q2g0&*d9&lirtlk320^a+i!4#m3z8bp#(t$6#(+r3f==ix%af'
ENV RECAPTCHA_PUBLIC_KEY = '6LdzV8oeAAAAAM23NDLgb2WItZGqLaW-9UW31u85'
ENV RECAPTCHA_PRIVATE_KEY = '6LdzV8oeAAAAABMkHkwl5E_AqW--pzh9bukWtFYV'

WORKDIR /app

# Install required packages
COPY Django/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Django code into the container
COPY Django/ ./

EXPOSE 8000

# Start the Django application
CMD ["sh", "-c", "python django_api/manage.py migrate && python django_api/manage.py runserver 8888"]
