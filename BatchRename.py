import maya.cmds as cmds


def re():
    renameInput = cmds.textField('RenameInput', q=True, tx=True)
    idInput = cmds.textField('IdInput', q=True, tx=True)
    selectList = cmds.ls(selection=True)
    i = int(idInput)
    for n in range(len(selectList)):
        cmds.rename(selectList[n], renameInput + str(i))
        i = i + 1


def gui():
    windowName = 'BatchRename'
    windowTitle = 'BatchRename'

    try:
        cmds.deleteUI(windowName)
    except:
        pass

    myWindow = cmds.window(windowName, title=windowTitle)
    cmds.columnLayout(adj=True)
    cmds.rowLayout(numberOfColumns=2, columnWidth2=(75, 150), adj=2)
    cmds.text(l='Prefix')
    cmds.textField('RenameInput')
    cmds.setParent('..')
    cmds.rowLayout(numberOfColumns=2, columnWidth2=(75, 150), adj=2)
    cmds.text(l='SerialNumber')
    cmds.textField('IdInput')
    cmds.setParent('..')
    cmds.button(l='Start', c='re()', backgroundColor=[0.33, 0.33, 0.33])
    allowedAreas = ['right']
    cmds.dockControl(area='right', content=myWindow, allowedArea=allowedAreas)

gui()
