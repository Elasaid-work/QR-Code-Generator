FROM node:22-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm install

# Copy everything including src/
COPY . .

# Build from src/app
RUN npm run build

FROM node:22-alpine AS runtime

WORKDIR /app

# Copy only what's needed for runtime
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/src ./src

# If you're using the App Router, Next.js needs to see ./src/app
ENV NODE_ENV=production
EXPOSE 3000
CMD ["npm", "run", "start"]
