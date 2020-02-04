#import numpy as np
import re
import os




def L2_norm(v,h):
    ret = 0.0;
    for el in v:
        ret = ret + el**2.0*h*h; #assume uniform grid and 2D domain
    return((ret)**(1.0/2.0))

def check_float(val):             
    if re.match(r'^-?\d+(?:\.\d+)?$',val) is None:
        return False         
    else:                     
        return True

def get_div_norms(filename, size):
    l = [];
    volume_elements = False;
    with open(filename) as div_file:
        for line in div_file:
            if 'internalField' in line: #ugly cut of the internal fied (2D in cavity)
                volume_elements = True;
            elif ')' in line:
                volume_elements = False;
                
            if check_float(line)&volume_elements:
                val = float(line);
                if int(val) - val != 0:
                    l.append(val);

    normC = max([abs(ll) for ll in l]);
    normL2 = L2_norm(l,1.0/size);
    return(size, normC, normL2)

def change_mesh_file_name(file_name, n):    
    with open(file_name) as mesh_file, open (file_name + '.new','w') as new_file:
        for line in mesh_file:
            if 'hex (0 1 2 3 4 5 6 7)' in line:
                line = 'hex (0 1 2 3 4 5 6 7) (' + str(n) + ' ' + str(n) +' ' +'1) simpleGrading (1 1 1)\n'
            new_file.write(line)
    
    cmd = 'mv ' + file_name +'.new ' + file_name 
    os.system(cmd)




N = [20, 40, 80, 160]
file_mesh = 'system/blockMeshDict'
file_div = '5/div(U)'
file_exec_all = './run_div_check.sh'
file_res = 'div_res.dat'

with open(file_res,'w') as res_file:
    res_file.write('Mesh' + ' ' + 'C_norm' + ' ' + 'L2_norm' +'\n')
    for n in N:
        change_mesh_file_name(file_mesh, n)
        os.system(file_exec_all)
        res = get_div_norms(file_div, n)
        res_file.write(str(res[0]) + ' ' + str(res[1]) + ' ' + str(res[2])+'\n')
        print(n)
