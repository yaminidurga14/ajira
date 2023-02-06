from collections import defaultdict
from classes import *
from typing import *


def add_device(network,type,name):
    if name in network.keys():
        return "Error: That name already exists"
    network[name] = Device(type,name) 
    return "Successfully added "+name


def set_device_strength(network:DefaultDict[str, Device], name, strength:str):
    if not strength.isdigit():
        return "Error: Invalid command syntax"
    
    if name in network.keys():
        device = network[name]
        device.strength = int(strength)
        return "Successfully defined strength"
    else:
        return "Error: No device exists"
    

def connect_device(network:DefaultDict[str, Device], device1, device2):
    if device1 == device2:
        return "Error: Cannot connect device to itself!"
    
    if device1 in network.keys() and device2 in network.keys():
        node1 = network[device1]
        node2 = network[device2]
        node1.adjacent.append(node2)
        node2.adjacent.append(node1)
        return "Successfully Connected!"
    else:
        return "Error: Node not found"

def calc_route_util(visited:DefaultDict, currentNode:Device, res:List, resNode:Device):
    if currentNode.name == resNode.name:
        print("> Route found! "+str(res))

    elif visited[currentNode.name] != 1:
        visited[currentNode.name] = 1
        print("Adjacent: ",currentNode.adjacent)
        for node in currentNode.adjacent:
            res.append(node.name)
            print(res)
            calc_route_util(visited, node, res, resNode)
            res.pop()
    else:
        pass

def calc_node(startNode:Device, resNode:Device):
    visited = defaultdict(lambda:0)
    res = []
    res.append(startNode.name)
    calc_route_util(visited, startNode, res,resNode)

def info_route(network:DefaultDict[str, Device], device1:str, device2:str):
    print("Device1",network[device1])
    print("Device2",network[device2])
    if network[device1].type == "REPEATER" or network[device2].type == "REPEATER":
        return "Error: Route cannot be calculated with a repeater!"
  
    if device1 in network.keys() and device2 in network.keys():
        node1 = network[device1]
        node2 = network[device2]

        calc_node(node1, node2)
        return "Above are the routes found"
    else:
        return "Error: Node not found"