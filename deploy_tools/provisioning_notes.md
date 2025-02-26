Provisioning a new site
=======================

# # Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install nginx git python36 python3.6-venv

# # Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

# # Systemd service

* see gunicorn-systemd.tempalte.service
* replace DOMAIN with, e.g., staging.my-domain.com

# # Folder structure:

Assume we have a user account at /home/username

/home/username
|___sites
|   |--- .env
|   |--- db.sqlite3
|   |--- manage.py etc
|   |--- static
|   |___ virtualenv
|___DOMAIN2
    |--- .env
    |--- db.sqlite3
    |--- etc
