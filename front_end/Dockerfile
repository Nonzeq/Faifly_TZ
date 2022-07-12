FROM node:13.12.0-alpine
WORKDIR /app/front_end

COPY package.json package-lock.json ./
RUN npm install 
COPY . ./
EXPOSE 3000