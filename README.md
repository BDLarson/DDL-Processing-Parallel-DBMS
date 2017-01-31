DDL-Processing-Parallel-DBMS

Implementation of the DDL processing component of a parallel SQL processing system. The parallel SQL # processing system consists of a cluster of DBMS instances running on different machines (possibly virtual # machines). DDLs submitted to the system will need to be translated into corresponding DDLs for each individual # DBMS instance in the cluster and executed there. In addition a catalog database stores metadata about what # data is stored for each table on each DBMS instance in the cluster.

==========================

LOCAL MACHINE (macOS)

Install Homebrew:<br />
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Install virtualbox & vagrant:<br />
$ brew cask install virtualbox<br />
$ brew cask install vagrant<br />
$ brew cask install vagrant-manager<br />

Install python3 if not already on machine: <br />
$ brew install python3

==========================

LOCAL MACHINE (Linux)

Install virtualbox & vagrant:<br />
$ sudo apt install virtualbox<br />
$ sudo apt install vagrant<br />
$ sudo apt install vagrant-manager<br />

Install python3 if not already on machine (macOS):<br />
$ brew install python3<br />

Install python3 if not already on machine (Linux):<br />
$ sudo apt install python3<br />

Install PyMySQL if not already on machine:<br />
$ pip3 install PyMySQL<br />

Create a Directory for the Catalog and each Node:<br />
$ mkdir catalog<br />
$ mkdir node1<br />
$ mkdir node2<br />

Initialize a virtual machine in each directory:<br />
$ vagrant init ubuntu/xenial64<br />
$ vagrant up<br />
$ vagrant ssh<br />

Change directory to /vagrant in each directory:<br />
$ cd /vagrant<br />

Install MySQL in each directory:<br />
$ sudo apt-get install mysql-server<br />
NOTE: Password for MySQL-server: password<br />

Edit the MySQL settings in each directory:<br />
$ /usr/bin/mysql_secure_installation<br />
NOTE: Respond No to everything but Remove test database and access to it, and Reload privilege tables<br />

Open Vagrantfile in Each Directory:<br />
Replace line 25 with:<br />
  config.vm.network "forwarded_port", guest: 3306, host: 3306, auto_correct: true <br />
Replace line 29 with:<br />
  config.vm.network "private_network", ip: "ADDRESS_VALUE"<br />
Note: ADDRESS_VALUE depends on Directory:<br />
  /textbox2, address_value = localhost_network.20<br />
  /textbox1, address_value = localhost_network.10<br />
  /catalogbox, address_value = localhost_network.30<br />

Install MySQL in Each Directory:<br />
$ cd /vagrant<br />
$ sudo apt-get install mysql-server<br />
Note: Password for MySQL-server: password<br />
$ /usr/bin/mysql_secure_installation<br />
Note: Respond No to everything but Remove test database and access to it, and Reload privilege tables<br />

Create Remote Users in Each Directory:<br />
$ cd /etc/mysql/mysql.conf.d<br />
$ sudo vim mysqld.cnf<br />
Comment out BIND-ADDRESS<br />
$ sudo service mysql restart<br />
$ mysql -u root -p<br />
Enter password<br />
mysql > create database TESTDB;<br />
mysql > show databases;<br />
mysql > use TESTDB;<br />
mysql > create user 'username'@'localhost_value' identified by 'passwd';<br />
mysql > grant all on * to 'username'@'192.168.10.1';<br />
