DDL-Processing-Parallel-DBMS

Implementation of the DDL processing component of a parallel SQL processing system. The parallel SQL # processing system consists of a cluster of DBMS instances running on different machines (possibly virtual # machines). DDLs submitted to the system will need to be translated into corresponding DDLs for each individual # DBMS instance in the cluster and executed there. In addition a catalog database stores metadata about what # data is stored for each table on each DBMS instance in the cluster.

==========================

LOCAL MACHINE (macOS)

Install Homebrew:<br />
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"<br />

Install virtualbox & vagrant:<br />
$ brew cask install virtualbox<br />
$ brew cask install vagrant<br />
$ brew cask install vagrant-manager<br />

Install python3 if not already on machine: <br />
$ brew install python3<br />

==========================

LOCAL MACHINE (Linux)<br />

Install virtualbox & vagrant:<br />
$ sudo apt install virtualbox<br />
$ sudo apt install vagrant<br />
$ sudo apt install vagrant-manager<br />

Install python3 if not already on machine:<br />
$ sudo apt install python3<br />

==========================

Install PyMySQL if not already on machine:<br />
$ pip3 install PyMySQL<br />

Create a Directory for the Catalog and each Node:<br />
$ mkdir catalog<br />
$ mkdir node1<br />
$ mkdir node2<br />

Install all necessary files from the repo:<br />
1) test.py<br />
2) c.cfg<br />
3) d.sql<br />
4) run.sh<br />

Initialize a virtual machine in each directory:<br />
$ vagrant init ubuntu/xenial64<br />
$ vagrant up<br />
$ vagrant ssh<br />

Change to the /vagrant directory of each virtual machine<br />
$ cd /vagrant<br />

Open Vagrantfile in Each Directory:<br />
Replace line 25 with:<br />
  config.vm.network "forwarded_port", guest: 3306, host: 3306, auto_correct: true<br />
Replace line 29 with:<br />
  config.vm.network "private_network", ip: "ADDRESS_VALUE"<br />
Note: ADDRESS_VALUE depends on Directory:<br />
  /textbox2, address_value = localhost_network.20<br />
  /textbox1, address_value = localhost_network.10<br />
  /catalogbox, address_value = localhost_network.30<br />

Install MySQL in Each Directory:<br />
$ sudo apt-get install mysql-server<br />
Note: Password for MySQL-server: password<br />
$ /usr/bin/mysql_secure_installation<br />
Note: Respond No to everything but Remove test database and access to it, and Reload privilege tables<br />

Connect to MySQL in Each Directory:<br />
$ mysql -u root -p;<br />
Enter password: 'password'<br />

Create a database in Each Directory: <br />
NOTE: If a user already exists then drop it:<br />
mysql> drop user 'username'<br />
Create the database:<br />
mysql> create database TESTDB;<br />

Create Remote Users in Each Directory:<br />
mysql> use TESTDB;<br />
mysql> create user 'username';<br />
mysql> grant all on TESTDB.* to username@'%' identified by 'password';<br />
mysql> exit<br />
$ exit<br />

Run the DDL from your local host repo:<br />
$ python3 test.py c.cfg d.sql<br />
