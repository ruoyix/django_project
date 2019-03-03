#!/usr/bin/expect
set time out 30
spawn python3 manage.py createsuperuser --username test --emall test@qq.com
expect "password for figo"
send "123456"
expect "password for figo"
send "123456"
