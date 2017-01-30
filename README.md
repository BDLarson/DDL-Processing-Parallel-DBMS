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
$ sudo apt install python3

Install PyMySQL if not already on machine:
$ pip3 install PyMySQL

Create a Directory for the Catalog and Each Node

Initialize a VirtualBox in Each Directory
$ vagrant init ubuntu/xenial64
$ vagrant up
$ vagrant ssh

Change Directory to /vagrant in Each Directory
$ cd /vagrant

Install MySQL in Each Directory
$ sudo apt-get install mysql-server
Note: Password for MySQL-server: password
$ /usr/bin/mysql_secure_installation
Note: Respond No to everything but Remove test database and access to it, and Reload privilege tables
