#!/usr/bin/python3
"""add an item"""
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


try:
    loadFile = load_from_json_file("add_item_json")
except FileNotFoundError:
    loadFile = []

argc = len(sys.argv)
for index in range (1, argc):
    loadFile.append(sys.argv[index])
save_to_json_file(loadFile, "add_item.json")
