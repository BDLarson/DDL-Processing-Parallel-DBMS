#!/usr/bin/python3
import pymysql

import sys
from sys import argv

def runDDL(argv):
    # Define variables
    hostname = ""
    username = ""
    passwd = ""

    # List of Nodes
    nodes = []

    # Takes in Command Line Arguments for files
    fname, clustercfg, ddlfile = argv

    # Reads clustercfg file line by line
    # Parses contents and creates a Cluster object for every catalog or node read in
    k = open(clustercfg, "r")
    with open(clustercfg) as fin:
        for line in fin:
            if line.strip():
                temp = line.strip().split("=")
                if temp[0].split(".")[0].find("catalog") > -1:
                    kind = "catalog"
                    if temp[0].split(".")[1].find("hostname") > -1:
                        hostname = temp[1]
                    elif temp[0].split(".")[1].find("username") > -1:
                        username = temp[1]
                    elif temp[0].split(".")[1].find("passwd") > -1:
                        passwd = temp[1]
                        catalog = Catalog(hostname, username, passwd)
                elif temp[0].split(".")[0].find("numnodes") > -1:
                    pass
                elif temp[0].split(".")[0].find("node") > -1:
                    kind = "node"
                    if temp[0].split(".")[1].find("hostname") > -1:
                        hostname = temp[1]
                    elif temp[0].split(".")[1].find("username") > -1:
                        username = temp[1]
                    elif temp[0].split(".")[1].find("passwd") > -1:
                        passwd = temp[1]
                        nodes.append(Node(hostname, username, passwd))

    # Reads ddlfile, Remove Whitespace, Remove new lines, Parse contents on ';'
    k = open(ddlfile, "r")
    sqlcmds = list(filter(None, k.read().strip().replace("\n","").split(';')))

    # Running Commands
    for cmd in sqlcmds:
        for n in nodes:
            try:
                connect = pymysql.connect(n.hostname, n.username, n.passwd, db = 'TESTDB')
                cur = connect.cursor()
                cur.execute(cmd)
                connect.close()
                print("[", nodes[0].hostname, "]: ./", ddlfile, " success.")
            except pymysql.InternalError:
                print("[", nodes[0].hostname, "]: ./", ddlfile, " failed.")
    k.close()

    # # Print Catalog Info
    # catalog.displayCatalog()
    #
    # # Print Node Info
    # for cl in nodes:
    #     cl.displayNode()

class Catalog:
    'Base Class for Catalog'
    def __init__(self, hostname, username, passwd):
        self.hostname = hostname
        self.username = username
        self.passwd = passwd
    def displayCatalog(self):
        print(" Hostname: ", self.hostname, " Username: ", self.username, " Passwd: ", self.passwd)

class Node:
    'Base Class for Nodes'
    def __init__(self, hostname, username, passwd):
        self.hostname = hostname.replace(" ", "")
        self.username = username.replace(" ", "")
        self.passwd = passwd.replace(" ", "")
    def displayNode(self):
        print("Hostname: ", self.hostname, " Username: ", self.username, " Passwd: ", self.passwd)

runDDL(argv)
