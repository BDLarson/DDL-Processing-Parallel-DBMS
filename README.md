DDL-Processing-Parallel-DBMS

Implementation of the DDL processing component of a parallel SQL processing system. The parallel SQL # processing system consists of a cluster of DBMS instances running on different machines (possibly virtual # machines). DDLs submitted to the system will need to be translated into corresponding DDLs for each individual # DBMS instance in the cluster and executed there. In addition a catalog database stores metadata about what # data is stored for each table on each DBMS instance in the cluster.

LOCAL MACHINE (macOS)

Install Homebrew:
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Install virtualbox & vagrant:
$ brew cask install virtualbox
$ brew cask install vagrant
$ brew cask install vagrant-manager
VAGRANT VIRTUAL MACHINE

Install python3 if not already on machine:
$ brew install python3

Install PyMySQL if not already on machine:
$ pip3 install PyMySQL

Create a Directory for the Catalog and Each Node

Initialize a VirtualBox in Each Directory
$ vagrant init ubuntu/xenial64
$ vagrant up
$ vagrant ssh

Open Vagrantfile in Each Directory
Replace line 25 with:
  config.vm.network "forwarded_port", guest: 3306, host: 3306, auto_correct: true
Replace line 29 with:
  config.vm.network "private_network", ip: "ADDRESS_VALUE"
ADDRESS_VALUE depends on Directory:
  /textbox2, address_value = localhost_network.20
  /textbox1, address_value = localhost_network.10
  /catalogbox, address_value = localhost_network.30

Install MySQL in Each Directory
$ cd /vagrant
$ sudo apt-get install mysql-server
Note: Password for MySQL-server: password
$ /usr/bin/mysql_secure_installation
Note: Respond No to everything but Remove test database and access to it, and Reload privilege tables

Create Remote Users in Each Directory
$ cd /etc/mysql/mysql.conf.d
$ sudo vim mysqld.cnf
Comment out BIND-ADDRESS
$ sudo service mysql restart
$ mysql -u root -p
Enter password

Creating Database
mysql > create database TESTDB;
mysql > show databases;
mysql > use TESTDB;
mysql > CREATE USER 'username'@'localhost_value' IDENTIFIED BY 'passwd';
mysql > grant all on * to 'username'@'192.168.10.1';
