DDL-Processing-Parallel-DBMS

Implementation of the DDL processing component of a parallel SQL processing system. The parallel SQL # processing system consists of a cluster of DBMS instances running on different machines (possibly virtual # machines). DDLs submitted to the system will need to be translated into corresponding DDLs for each individual # DBMS instance in the cluster and executed there. In addition a catalog database stores metadata about what # data is stored for each table on each DBMS instance in the cluster.

LOCAL MACHINE (macOS)

Install Homebrew:<br />
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Install virtualbox & vagrant:<br />
$ brew cask install virtualbox<br />
$ brew cask install vagrant<br />
$ brew cask install vagrant-manager<br />

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

Create remote users in each directory:<br />

Grant full access for all remote users:<br />

Create DB's in each directory:<br />


