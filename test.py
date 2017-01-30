#!/usr/bin/python3
import pymysql

import sys
from sys import argv

def runDDL(argv):
    # Define variables
    driver = ""
    kind = ""
    hostname = ""
    username = ""
    passwd = ""

    # Takes in Command Line Arguments for files
    fname, clustercfg, ddlfile = argv
    # print('clustercfg is', clustercfg)
    # print('ddlfile is', ddlfile)

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
                        driver = temp[1]
                    elif temp[0].split(".")[1].find("hostname") > -1:
                        hostname = temp[1]
                    elif temp[0].split(".")[1].find("username") > -1:
                        username = temp[1]
                    elif temp[0].split(".")[1].find("passwd") > -1:
                        passwd = temp[1]
                        ClusterPt(kind, driver, hostname, username, passwd)
                elif temp[0].split(".")[0].find("numnodes") > -1:
                    pass
                elif temp[0].split(".")[0].find("node") > -1:
                    kind = "node"
                    if temp[0].split(".")[1].find("driver") > -1:
                        driver = temp[1]
                    elif temp[0].split(".")[1].find("hostname") > -1:
                        hostname = temp[1]
                    elif temp[0].split(".")[1].find("username") > -1:
                        username = temp[1]
                    elif temp[0].split(".")[1].find("passwd") > -1:
                        passwd = temp[1]
                        ClusterPt(kind, driver, hostname, username, passwd)

    # Reads ddlfile, Remove Whitespace, Remove new lines, Parse contents on ';'
    k = open(ddlfile, "r")
    sqlcmds = list(filter(None, k.read().strip().replace("\n","").split(';')))
    print(sqlcmds)

    k.close()

def parseCFG(str):
    print('PASSED IN: ', str)

class ClusterPt:
    'Base Class for the parts of a Cluster'
    def __init__(self, kind, driver, hostname, username, passwd):
        # kind is either catalog or node
        self.kind = kind
        self.driver = driver
        self.hostname = hostname
        self.username = username
        self.passwd = passwd
    def displayCluster(self):
        print("Kind: ", self.kind, " Driver: ", self.driver, " Hostname: ", self.hostname, " Username: ", self.username, " Passwd: ", self.passwd)

runDDL(argv)
