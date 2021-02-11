FROM nginx:1.16-alpine

ADD nginx.conf /etc/nginx/default.conf

EXPOSE 80

CMD ["/usr/sbin/nginx", "-c", "/etc/nginx/default.conf"]