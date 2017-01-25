# DDL-Processing-Parallel-DBMS

# Implementation of the DDL processing component of a parallel SQL processing system. The parallel SQL          # processing system consists of a cluster of DBMS instances running on different machines (possibly virtual     # machines). DDLs submitted to the system will need to be translated into corresponding DDLs for each individual # DBMS instance in the cluster and executed there. In addition a catalog database stores metadata about what    # data is stored for each table on each DBMS instance in the cluster.
#
#
# LOCAL MACHINE
#
# $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
#
# Install vagrant:
# $ brew cask install virtualbox
# $ brew cask install vagrant
# $ brew cask install vagrant-manager
#
# VAGRANT VIRTUAL MACHINE
#
# Install python3 if not already on machine:
# $ sudo apt install python3
#
# Install sqlite3 if not already on machine:
# $ sudo apt install sqlite3
