'''
written by alexander torres
how to run:
import internAutoRig
reload(internAutoRig)
internAutoRig.gui()
'''

import pymel.core as pm 

scriptName = __name__
winName = 'autoRig_interns'

black = [0.0, 0.0, 0.0]
white = [1.0, 1.0, 1.0]
grey = [0.5, 0.5, 0.5]

class WindowButton:

    def __init__(self, button_width, button_height, button_name, button_command, button_color):
        self.btnW = button_width
        self.btnH = button_height
        self.btnName = button_name
        self.btnCommand = button_command
        self.btnColor = button_color
        self.btn = None
        self.create_button()

    def create_button(self):
        self.btn = pm.button(w=self.btnW, h=self.btnH, l=self.btnName, c=scriptName + self.btnCommand,
            bgc=self.btnColor)


def gui():
    if pm.window(winName, q=True, exists=True):
        pm.deleteUI(winName)
    if pm.windowPref(winName, q=True, exists=True):
        pm.windowPref(winName, r=True)

    win_w = 170
    win_h = 200
    btn_w = win_w/2
    btn_h = win_h/5
    win = pm.window(winName, w=win_w, h=win_h + btn_h, nde=True, tlb=True, s=False, mnb=True, mxb=True, ds=True)

    mainLayout = pm.rowColumnLayout(nc=1)
    pm.text(label='This tool renames and\norients the joints for\nthe respective anatomy\npart, just select and\n press the proper button')
    btnLayout = pm.rowColumnLayout(nc=2, cw=[[1, btn_w], [2, btn_w]])
    armBtn = WindowButton(btn_w, btn_h, 'Arm Bone\nSetup', '.arm_setup()', black)
    legBtn = WindowButton(btn_w, btn_h, 'Leg Bone\nSetup', '.leg_setup()', black)
    handBtn = WindowButton(btn_w, btn_h, 'Hand Bone\nSetup', '.hand_setup()', black)
    thumbBtn = WindowButton(btn_w, btn_h, 'Thumb Bone\nSetup', '.thumb_setup()', black)
    index_fingerBtn = WindowButton(btn_w, btn_h, 'Index Finger\nBone Setup', '.index_finger_setup()', black)
    middle_fingerBtn = WindowButton(btn_w, btn_h, 'Middle Finger\nBone Setup', '.middle_finger_setup()', black)
    ring_fingerBtn = WindowButton(btn_w, btn_h, 'Ring Finger\nBone Setup', '.ring_finger_setup()', black)
    pinky_fingerBtn = WindowButton(btn_w, btn_h, 'Pinky Finger\nBone Setup', '.pinky_finger_setup()', black)
    clavicleBtn = WindowButton(btn_w, btn_h, 'Clavicle\nBone Setup', '.clavicle_setup()', black)
    hipsBtn = WindowButton(btn_w, btn_h, 'Hips Bone\nSetup', '.hip_setup()', black)
    spineBtn = WindowButton(btn_w, btn_h, 'Spine Bone\nSetup', '.spine_setup()', black)
    neckBtn = WindowButton(btn_w, btn_h, 'Neck Bone\nSetup', '.neck_setup()', black)
    headBtn = WindowButton(btn_w, btn_h, 'Head Bone\nSetup', '.head_setup()', black)
    mirror_jointsBtn = WindowButton(btn_w, btn_h, 'Mirror Selected\nBones', '.mirror_joints()', black)

    win.show()

def arm_setup():
    selection = pm.ls(sl=True, dag=True, type='transform')
    print selection
    renamer('lt', 'arm', 'bind', selection)
    orient_joints('x', 'y', 'x', '-', selection)

def leg_setup():
    selection = pm.ls(sl=True, dag=True, type='transform')
    print selection
    renamer('lt', 'leg', 'bind', selection)
    orient_joints('x', 'y', 'z', '+', selection)

def hand_setup():
    selection = pm.ls(sl=True, dag=True, type='transform')
    print selection
    renamer('lt', 'hand', 'bind', selection)
    orient_joints('x', 'y', 'x', '-', selection)

def thumb_setup():
    selection = pm.ls(sl=True, dag=True, type='transform')
    print selection
    renamer('lt', 'thumb', 'bind', selection)
    orient_joints('x', 'y', 'x', '+', selection)

def index_finger_setup():
    selection = pm.ls(sl=True, dag=True, type='transform')
    print selection
    renamer('lt', 'index_finger', 'bind', selection)
    orient_joints('x', 'y', 'x', '-', selection)

def middle_finger_setup():
    selection = pm.ls(sl=True, dag=True, type='transform')
    print selection
    renamer('lt', 'middle_finger', 'bind', selection)
    orient_joints('x', 'y', 'x', '-', selection)

def ring_finger_setup():
    selection = pm.ls(sl=True, dag=True, type='transform')
    print selection
    renamer('lt', 'ring_finger', 'bind', selection)
    orient_joints('x', 'y', 'x', '-', selection)

def pinky_finger_setup():
    selection = pm.ls(sl=True, dag=True, type='transform')
    print selection
    renamer('lt', 'pinky_finger', 'bind', selection)
    orient_joints('x', 'y', 'x', '-', selection)

def clavicle_setup():
    selection = pm.ls(sl=True, dag=True, type='transform')
    print selection
    renamer('lt', 'clavicle', 'bind', selection)
    orient_joints('x', 'y', 'y', '-', selection)

def hip_setup():
    selection = pm.ls(sl=True, dag=True, type='transform')
    print selection
    renamer('lt', 'hip', 'bind', selection)
    orient_joints('x', 'y', 'x', '-', selection)

def spine_setup():
    selection = pm.ls(sl=True, dag=True, type='transform')
    print selection
    renamer('lt', 'spine', 'bind', selection)
    orient_joints('x', 'y', 'x', '-', selection)

def neck_setup():
    selection = pm.ls(sl=True, dag=True, type='transform')
    print selection
    renamer('lt', 'neck', 'bind', selection)
    orient_joints('x', 'y', 'x', '-', selection)

def head_setup():
    selection = pm.ls(sl=True, dag=True, type='transform')
    print selection
    renamer('lt', 'head', 'bind', selection)
    orient_joints('x', 'y', 'x', '-', selection)

def renamer(prefix, name, suffix, items):
    count = 0
    for each in items:
        count = count + 1
        new_name = '%s_%s_0%s_%s' %(prefix, name, count, suffix)
        each.rename(new_name)

        if pm.nodeType(each) == 'joint':
            if len(items) > 1:
                last_name = items[-1].replace(suffix, 'waste')
                items[-1].rename(last_name)
            else:
                print ('Single Joint')

def orient_joints(aim_axis, secondary_axis, world_up_axis, pos_neg, joints):
    orientation = None
    if aim_axis == 'x':
        if secondary_axis == 'y':
            orientation = '%s%s%s' %(aim_axis, secondary_axis, 'z')
        elif secondary_axis == 'z':
            orientation = '%s%s%s' %(aim_axis, secondary_axis, 'y')
        else:
            orientation = '%s%s%s' % (aim_axis, secondary_axis, 'z')
    elif aim_axis == 'y':
        if secondary_axis == 'x':
            orientation = '%s%s%s' %(aim_axis, secondary_axis, 'z')
        elif secondary_axis == 'z':
            orientation = '%s%s%s' %(aim_axis, secondary_axis, 'x')
        else:
            orientation = '%s%s%s' % (aim_axis, secondary_axis, 'z')
    elif aim_axis == 'z':
        if secondary_axis == 'x':
            orientation = '%s%s%s' %(aim_axis, secondary_axis, 'y')
        elif secondary_axis == 'y':
            orientation = '%s%s%s' %(aim_axis, secondary_axis, 'x')
        else:
            orientation = '%s%s%s' % (aim_axis, secondary_axis, 'y')

    axis = None
    if world_up_axis == 'x':
        if pos_neg == '+':
            axis = 'xup'
        elif pos_neg == '-':
            axis = 'xdown'
    elif world_up_axis == 'y':
        if pos_neg == '+':
            axis = 'yup'
        elif pos_neg == '-':
            axis = 'ydown'
    elif world_up_axis == 'z':
        if pos_neg == '+':
            axis = 'zup'
        elif pos_neg == '-':
            axis = 'zdown'

    if pm.nodeType(joints[0]) == 'joint':
        pm.joint(joints[0], edit=True, orientJoint=orientation, secondaryAxisOrient=axis, ch=True, zso=True)
    else:
        print ('You tried to orient an obj with the %s orientation, this tool works on joints' %orientation)

def mirror_joints(mir_xy=False, mir_yz=True, mir_xz=False, search='lt', replace='rt'):
    selection = pm.ls(sl=True, type='transform')

    for each in selection:
        joint_chain = pm.ls(each, dag=True)
        if pm.nodeType(joint_chain[0]) == 'joint':
            pm.mirrorJoint(joint_chain[0], mirrorBehavior=True, mirrorXY=mir_xy, mirrorYZ=mir_yz,
                mirrorXZ=mir_xz, searchReplace=[search, replace])
            pm.select(cl=True)
        else:
            print ("You tried to mirror an object that isn't a joint. This tool only functions on joints.")
