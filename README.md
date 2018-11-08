# archive
Automated archival of treasured websites / videos

## dependencies

- https://wkhtmltopdf.org/
- https://github.com/rg3/youtube-dl

## aws config

- env vars
  - `aws_access_key_id`
  - `aws_secret_access_key`

## todo

- have a way to skip assets and/or put them as low-priority
- download pdfs
- create docker container?

## pdf deps

```
wget https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox-0.12.5-1.centos7.x86_64.rpm
sudo yum install wkhtmltox-0.12.5-1.centos7.x86_64.rpm
rm wkhtmltox-0.12.5-1.centos7.x86_64.rpm

sudo yum install xorg-x11-fonts-100dpi.noarch xorg-x11-fonts-75dpi.noarch xorg-x11-fonts-ISO8859-1-100dpi.noarch xorg-x11-fonts-ISO8859-1-75dpi.noarch xorg-x11-fonts-ISO8859-14-100dpi.noarch xorg-x11-fonts-ISO8859-14-75dpi.noarch xorg-x11-fonts-ISO8859-15-100dpi.noarch xorg-x11-fonts-ISO8859-15-75dpi.noarch xorg-x11-fonts-ISO8859-2-100dpi.noarch xorg-x11-fonts-ISO8859-2-75dpi.noarch xorg-x11-fonts-ISO8859-9-100dpi.noarch xorg-x11-fonts-ISO8859-9-75dpi.noarch xorg-x11-fonts-Type1.noarch xorg-x11-fonts-cyrillic.noarch xorg-x11-fonts-ethiopic.noarch xorg-x11-fonts-misc.noarch

// download libpng-1.5.15.tar.gz
tar -zxvf libpng-1.5.15.tar.gz
rm libpng-1.5.15.tar.gz

cd libpng-1.5.15
./configure
sudo make install
cd ..
sudo rm -rf libpng-1.5.15/
```
