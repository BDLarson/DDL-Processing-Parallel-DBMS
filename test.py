#!/usr/bin/python3
import pymysql
import _thread
import sys
from sys import argv

def runDDL(argv):
    # Define variables
    hostname = ""
    username = ""
    passwd = ""
    url = ""
    port = ""
    db = ""

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
                    if temp[0].split(".")[1].find("driver") > -1:
                        pass
                    elif temp[0].split(".")[1].find("hostname") > -1:
                        url = temp[1]
                        hostname = temp[1].split("/", 2)[2].split(":")[0]
                        port = temp[1].split("/", 2)[2].split(":")[1].split("/")[0]
                        db = temp[1].split("/", 2)[2].split(":")[1].split("/")[1]
                    elif temp[0].split(".")[1].find("username") > -1:
                        username = temp[1]
                    elif temp[0].split(".")[1].find("passwd") > -1:
                        passwd = temp[1]
                        catalog = Catalog(hostname, username, passwd, db)
                elif temp[0].split(".")[0].find("numnodes") > -1:
                    pass
                elif temp[0].split(".")[0].find("node") > -1:
                    kind = "node"
                    if temp[0].split(".")[1].find("driver") > -1:
                        pass
                    elif temp[0].split(".")[1].find("hostname") > -1:
                        url = temp[1]
                        hostname = temp[1].split("/", 2)[2].split(":")[0]
                        port = temp[1].split("/", 2)[2].split(":")[1].split("/")[0]
                        db = temp[1].split("/", 2)[2].split(":")[1].split("/")[1]
                    elif temp[0].split(".")[1].find("username") > -1:
                        username = temp[1]
                    elif temp[0].split(".")[1].find("passwd") > -1:
                        passwd = temp[1]
                        nodes.append(Node(hostname, username, passwd, db))


    # Reads ddlfile, Remove Whitespace, Remove new lines, Parse contents on ';'
    k = open(ddlfile, "r")
    sqlcmds = list(filter(None, k.read().strip().replace("\n","").split(';')))

    # Create catalog
    try:
        catalog.createCatalog()
    except pymysql.InternalError:
        # Table Exists so it Errors
        print("Catalog already exists")

    # Running Commands from ddlfile
    for cmd in sqlcmds:
        for n in nodes:
            try:
                connect = pymysql.connect(n.hostname, n.username, n.passwd, n.db)
                cur = connect.cursor()
                cur.execute(cmd)
                connect.close()
                print("[", n.hostname, "]: ./", ddlfile, " success.")
            except pymysql.InternalError:
                print("[", n.hostname, "]: ./", ddlfile, " failed.")

    k.close()

    # # Print Catalog Info
    # catalog.displayCatalog()
    #
    # # Print Node Info
    # for cl in nodes:
    #     cl.displayNode()

class Catalog:
    'Base Class for Catalog'
    def __init__(self, hostname, username, passwd, db):
        self.hostname = hostname.replace(" ", "")
        self.username = username.replace(" ", "")
        self.passwd = passwd.replace(" ", "")
        self.db = db.replace(" ", "")
    def displayCatalog(self):
        print("Hostname: ", self.hostname, " Username: ", self.username, " Passwd: ", self.passwd, " DB: ", self.db)
    def createCatalog(self):
        createCMD = "create table dtables(tname VARCHAR(32), nodedriver VARCHAR(64), nodeurl VARCHAR(128), nodeuser VARCHAR(16), nodepasswd VARCHAR(16), partmtd INT, nodeid INT, partcol VARCHAR(32), partparam1 VARCHAR(32), partparam2 VARCHAR(32))"
        connect = pymysql.connect(self.hostname, self.username, self.passwd, self.db)
        cur = connect.cursor()
        cur.execute(createCMD)

class Node:
    'Base Class for Nodes'
    def __init__(self, hostname, username, passwd, db):
        self.hostname = hostname.replace(" ", "")
        self.username = username.replace(" ", "")
        self.passwd = passwd.replace(" ", "")
        self.db = db.replace(" ", "")
    def displayNode(self):
        print("Hostname: ", self.hostname, " Username: ", self.username, " Passwd: ", self.passwd, " DB: ", self.db)

runDDL(argv)
