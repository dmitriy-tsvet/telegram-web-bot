FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/
COPY security.conf /etc/nginx/

# use this command once to generate dhparam, and then copy to the container
# openssl dhparam -out /etc/ssl/certs/dhparam.pem 4096
# or delete this line and change nginx.conf

COPY /etc/ssl/certs/dhparam.pem /etc/ssl/certs/