DDL-Processing-Parallel-DBMS

Implementation of the DDL processing component of a parallel SQL processing system. The parallel SQL # processing system consists of a cluster of DBMS instances running on different machines (possibly virtual # machines). DDLs submitted to the system will need to be translated into corresponding DDLs for each individual # DBMS instance in the cluster and executed there. In addition a catalog database stores metadata about what # data is stored for each table on each DBMS instance in the cluster.

LOCAL MACHINE (macOS)

Install Homebrew:
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Install virtualbox & vagrant:
$ brew cask install virtualbox
$ brew cask install vagrant
$ brew cask install vagrant-manager

LOCAL MACHINE (Linux)

Install virtualbox & vagrant
$ sudo apt install virtualbox
$ sudo apt install vagrant
$ sudo apt install vagrant-manager

Install python3 if not already on machine (macOS):
$ brew install python3

Install python3 if not already on machine (Linux):
$ sudo apt install python3

Install PyMySQL if not already on machine:
$ pip3 install PyMySQL

Create a Directory for the Catalog and each Node:
$ mkdir catalog
$ mkdir node1
$ mkdir node2

Initialize a virtual machine in each directory:
$ vagrant init ubuntu/xenial64
$ vagrant up
$ vagrant ssh

Change directory to /vagrant in each directory:
$ cd /vagrant

Install MySQL in each directory:
$ sudo apt-get install mysql-server
NOTE: Password for MySQL-server: password

Edit the MySQL settings in each directory:
$ /usr/bin/mysql_secure_installation
NOTE: Respond No to everything but Remove test database and access to it, and Reload privilege tables

Create remote users in each directory:

Grant full access for all remote users:

Create DB's in each directory:


