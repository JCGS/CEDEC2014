# -*- coding: utf-8 -*-

import maya.cmds as cmds

def printAttr():
    for l in cmds.ls(sl=True):
        for attr in cmds.listAttr(i):
            print attr
