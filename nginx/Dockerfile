FROM nginx:1.21-alpine
LABEL maintainer=Parin_Lai

# import with variable
COPY default.conf.template /etc/nginx/templates/default.conf.template
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]