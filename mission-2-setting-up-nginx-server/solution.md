## Mission 2 - Setting Up NGINX Server

### Table of contents
* [Launching EC2 instance](#launching-ec2-instance)
* [Accessing the static website](#accessing-the-static-website)
<br>

### Launching EC2 instance

1. Go to AWS EC2 service.

2. Press `Launch instance`.

3. Instance name: `NGINX Server`.

4. We'll create EC2 instance with the following AMI:<br>
   ![EC2 AMI](https://github.com/idomeisner/dynamodb-rest-api-and-nginx-server/blob/main/mission-2-setting-up-nginx-server/images/ec2_ami.png)

5. For best practice we'll create a key pair:<br>
   ![EC2 Key Pair](https://github.com/idomeisner/dynamodb-rest-api-and-nginx-server/blob/main/mission-2-setting-up-nginx-server/images/ec2_key_pair.png)

6. We need to attach a security group to the EC2 instance.\
   The Security group need to have an inbound rule with HTTP access from `xxx.xxx.xxx.xxx/32`.\
   In the `Network settings` section we need to press `Edit` and add the following security group rule:<br>
   ![EC2 Security Group](https://github.com/idomeisner/dynamodb-rest-api-and-nginx-server/blob/main/mission-2-setting-up-nginx-server/images/ec2_security_group.png)

7. Now we'll add NGINX installation to the EC2 bootstrap.\
   In the `Advanced details` section, we'll add the following bootstrap script:

```
#!/bin/bash
# update the server package list
sudo apt update

# install nginx
sudo apt install nginx -y

# create the static website HTML file
sudo cat > /var/www/html/index.html << EOL
<!doctype html>
<html>
   <head>
      <meta charset="utf-8">
      <title>NGINX Server</title>
   </head>
   <body>
      <h1>Hello from the NGINX Server</h1>
      <p>Congratulations! </p>
   </body>
</html>
EOL
```
![EC2 Bootstrap](https://github.com/idomeisner/dynamodb-rest-api-and-nginx-server/blob/main/mission-2-setting-up-nginx-server/images/ec2_bootstrap.png)

8. Press `Launch instance`.
<br>

### Accessing the static website

1. Go to the created instance page.

2. The website address is written under the field `Public IPv4 address`.\
   **Note:** Every time the instance is stopped and resumed, the Public IPv4 address changes.<br>
   ![EC2 IPv4](https://github.com/idomeisner/dynamodb-rest-api-and-nginx-server/blob/main/mission-2-setting-up-nginx-server/images/ec2_ipv4.png)

3. We'll open this URL in the browser.\
   **Note:** The website will be accessible only from `xxx.xxx.xxx.xxx` IP.\
   **Note 2:** Every time the instance is stopped and resumed, the Public IPv4 address changes.\
   **Note 3:** Make sure you use HTTP protocol when accessing the website.

4. The static website:<br>
   ![NGINX Static Website](https://github.com/idomeisner/dynamodb-rest-api-and-nginx-server/blob/main/mission-2-setting-up-nginx-server/images/nginx_static_website.png)
