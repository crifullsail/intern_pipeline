'''
anim_toolset.py

@Jacob Meeks @Briana Taylor Riddle me this.  How would you select all the controls in a given system through a script.  The animator would select a control apart of a group , like a tail.  The script would then select all the control in that system.

Another option would be to select the rest of the system from a given point.  Like say ct_tail_03_icon is selected and the script will select the rest of the systems down the chain. 

Attack it!

How to Run:

import intern_pipeline.anim_toolset as anim_toolset
reload(anim_toolset)
anim_toolset.gui()

'''

import pymel.core as pm

gray = [.6, .6, .6]
win_width = 200

def gui():
	win = pm.window(w=win_width, title='Anim Toolset')
	main_layout = pm.columnLayout()
	gui_select(main_layout)
	gui_reset(main_layout)
	win.show()

def gui_select(parent_layout):
	pm.text(w=win_width, label='Select Tools', bgc=gray)
	pm.rowColumnLayout(nr=1)
	pm.button(w=win_width/3, h=win_width/5, label='ALL', c=pm.Callback(select_all))
	pm.button(w=win_width/3, h=win_width/5, label='Chain', c=pm.Callback(select_chain))
	pm.button(w=win_width/3, h=win_width/5, label='Rest Chain', c=pm.Callback(select_rest_of_chain))
	pm.setParent(parent_layout)

def gui_reset(parent_layout):
	pm.text(w=win_width, label='Reset Tools', bgc=gray)
	pm.rowColumnLayout(nr=1)
	pm.button(w=win_width/3, h=win_width/5, label='ALL', c=pm.Callback(reset_all))
	pm.button(w=win_width/3, h=win_width/5, label='Chain', c=pm.Callback(reset_chain))
	pm.button(w=win_width/3, h=win_width/5, label='Rest Chain', c=pm.Callback(reset_rest_of_chain))
	pm.setParent(parent_layout)


def select_all():
	icons = pm.ls('*_icon')
	pm.select(icons, r=True)

def select_chain():
    icon = pm.ls(sl=True)[0]
    icons = get_entire_chain(icon)
    
    pm.select(icons, r=True)

def select_rest_of_chain():
    icon = pm.ls(sl=True)[0]
    icons = get_rest_of_chain(icon)
    pm.select(icons, r=True)
    print 'Selected: {0}'.format(icons)
    
def get_entire_chain(icon): 
    icon_pieces = icon.split('_')
    icon_name = icon_pieces[1]
    
    icon_select = pm.ls('{0}*_{1}*_icon'.format(icon_pieces[0], icon_name))
    
    return icon_select

def get_rest_of_chain(icon):    
    icon_pieces = icon.split('_')
    icon_name = icon_pieces[1]
    icon_count = int(icon_pieces[2]) - 1
    icons = pm.ls('{0}*_{1}*_icon'.format(icon_pieces[0], icon_name))
     
    i = int(icon_pieces[2]) - 1
    icon_select = []
    for icon_count in xrange(icon_count, len(icons)):
        icon_select.append(icons[icon_count])

    return icon_select

def reset_icons(icon):
    reset_attrs = pm.listAttr(icon, unlocked=True, keyable=True)
    
    for current_attr in (reset_attrs):
        #print icon.attr(current_attr)
        icon.attr(current_attr).set(0)
   
def reset_chain():
    icons = get_entire_chain(pm.ls(sl=True)[0])
    for current_icon in icons:
        reset_icons(current_icon)

def reset_rest_of_chain():
    icons = get_rest_of_chain(pm.ls(sl=True)[0])
    for current_icon in icons:
        reset_icons(current_icon)   


def reset_all():
    icons = pm.ls('*_icon')
    for current_icon in icons:
        reset_icons(current_icon)

# Reset Hands