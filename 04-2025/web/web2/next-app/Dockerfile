# Use official lightweight Node.js image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy only package files first (for caching layer)
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the code
COPY . .

# Fix permissions just in case
RUN chmod -R 755 node_modules/.bin

# Build the app
RUN npm run build

# Expose port
EXPOSE 3000

# Start app
CMD ["npm", "start"]
