# HTTPS SSL

## Background Context

This project covers the importance of securing your website traffic using HTTPS and SSL.

## Resources

### Read or Watch:
- [What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)
- [What are the 2 main elements that SSL is providing?](https://sectigostore.com/blog/what-are-the-main-elements-of-ssl/)
- [HAProxy SSL termination on Ubuntu 16.04](https://www.haproxy.com/blog/haproxy-ssl-termination/)
- [SSL termination](https://www.nginx.com/resources/glossary/ssl-termination/)
- [Bash function](https://tldp.org/LDP/abs/html/functions.html)

### man or help:
- `awk`
- `dig`

## Learning Objectives

By the end of this project, you should be able to explain to anyone:

- What are HTTPS SSL's two main roles?
- What is the purpose of encrypting traffic?
- What does SSL termination mean?

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without errors
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script does

## Tasks

### 0. World Wide Web
**mandatory**

Configure your domain zone so that the subdomain `www` points to your load-balancer IP (`lb-01`). Add other subdomains and write a Bash script that will display information about subdomains.

**Requirements:**
- Add the subdomain `www` to your domain, point it to your `lb-01` IP
- Add the subdomain `lb-01` to your domain, point it to your `lb-01` IP
- Add the subdomain `web-01` to your domain, point it to your `web-01` IP
- Add the subdomain `web-02` to your domain, point it to your `web-02` IP
- Your Bash script must accept 2 arguments:
  - `domain`: type: string, what: domain name to audit, mandatory: yes
  - `subdomain`: type: string, what: specific subdomain to audit, mandatory: no
- Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`
- When only the parameter `domain` is provided, display information for its subdomains `www`, `lb-01`, `web-01`, and `web-02` in this specific order
- When passing domain and subdomain parameters, display information for the specified subdomain
- Ignore Shellcheck case SC2086
- Must use `awk` and at least one Bash function
- Do not handle edge cases such as empty parameters or nonexistent domain/subdomains

**Example:**
```bash
sylvain@ubuntu$ ./0-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
```

### 1. HAproxy SSL Termination
**mandatory**

"Terminating SSL on HAproxy" means configuring HAproxy to handle encrypted traffic, decrypt it, and pass it on to its destination.

**Requirements:**
- Create a certificate using `certbot`
- Configure HAproxy to accept encrypted traffic for your subdomain `www.`
- HAproxy must listen on port TCP 443
- HAproxy must accept SSL traffic
- HAproxy must serve encrypted traffic returning the `/` of your web server
- When querying the root of your domain name, the page must contain "Holberton School"
- Share your HAproxy config as an answer file (`/etc/haproxy/haproxy.cfg`)
- The file `1-haproxy_ssl_termination` must be your HAproxy configuration file

**Example:**
```bash
sylvain@ubuntu$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
sylvain@ubuntu$
sylvain@ubuntu$ curl https://www.holberton.online
Holberton School for the win!
sylvain@ubuntu$
```


## Repo

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x10-https_ssl`
- File: `0-world_wide_web`
- File: `1-haproxy_ssl_termination`

## Diagram

Below is a visual representation of the setup:

![HTTPS SSL Diagram](file-lNUeuS2EDG2fjWq2qHkyxPOj)
