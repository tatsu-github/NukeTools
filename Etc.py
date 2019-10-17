# set value to selected nodes
attr = 'colorspace'
val = 'linear_sRGB'
nodes = nuke.selectedNodes()
for i in nodes:
    i.knob(attr).setValue(val)
    print i.name()+': ', attr,'>>' , val
    
    
    
# replace footage path
import glob
old_ver = 'v001t01'
new_ver = 'v001t02'
nodes = nuke.selectedNodes()
replaced_file = 'Result: \n'
for i in nodes:
    try:
        getval = i.knob('file').getValue()
    except AttributeError:
        continue
    if not old_ver in getval:
        continue
    else:
        new_file = getval.replace(old_ver, new_ver)
    search_name = new_file.replace('%04d.exr', '????.*')
    if glob.glob(search_name):
        i.knob('file').setValue(new_file)
        replaced_file = replaced_file + 'Update: ' + getval.split('/')[-1].split('.')[0] + ' >> ' + new_ver + '\n'
    else:
        print new_file.split('/')[-1],'does not exists', '\n'
if replaced_file:
    nuke.message(replaced_file)

            
            
            
