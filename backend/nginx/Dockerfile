# Используем официальный образ nginx
FROM nginx:alpine

# Копируем наш конфиг в контейнер
COPY nginx.conf /etc/nginx/nginx.conf

# Создаем директорию для логов
RUN mkdir -p /var/log/nginx

# Экспортируем порт 80
EXPOSE 80
# EXPOSE 443

# Запускаем nginx в foreground режиме
CMD ["sh", "-c", "nginx -g 'daemon off;'"]