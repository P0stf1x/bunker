FROM node:22-bookworm-slim

WORKDIR /code

COPY app/package.json /code/package.json
COPY app/package-lock.json /code/package-lock.json

RUN npm --verbose install

COPY ./app /code/
# COPY public/ /code/public/
# COPY src/ /code/src/

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
CMD ["npm", "start"]