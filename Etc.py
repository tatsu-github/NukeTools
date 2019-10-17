# set value to selected nodes
attr = 'colorspace'
val = 'linear_sRGB'
nodes = nuke.selectedNodes()
for i in nodes:
    i.knob(attr).setValue(val)
    print i.name()+': ', attr,'>>' , val
    
    
    
# replace footage path
import os
old_ver = 'v001t01'
new_ver = 'v001t02'
nodes = nuke.selectedNodes()
for i in nodes:
    getval = i.knob('file').getValue()
    if not old_ver in getval:
        continue
    else:
        new_file = getval.replace(old_ver, new_ver)
    if os.path.exists(new_file) is True:
        i.knob('file').setValue(new_file)
    else:
        print new_file.split('/')[-1],'does not exists', '\n'


            
            
            
