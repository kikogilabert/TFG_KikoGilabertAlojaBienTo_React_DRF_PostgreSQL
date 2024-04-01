FROM node:18.17.1

WORKDIR /app

COPY React/package*.json ./

RUN npm install

COPY React/ ./

EXPOSE 3000

CMD ["npm", "run", "dev"]