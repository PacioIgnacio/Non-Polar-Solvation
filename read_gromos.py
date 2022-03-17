import numpy

def read_gromos_files(top_file, cnf_file):
    
    tf = open(top_file)
    top_data = tf.readlines()
    tf.close()
    
    cf = open(cnf_file)
    cnf_data = cf.readlines()
    cf.close()
    
    # Get names and types
    i_ref = 0
    while top_data[i_ref][:12]!='ATOMTYPENAME':
        i_ref +=1    
    
    i_ref += 2
    N_type = int(top_data[i_ref])
    
    while top_data[i_ref][:10]!='SOLUTEATOM':
        i_ref +=1
    
    i_ref += 2
    N_atom = int(top_data[i_ref])
    
    i_ref += 1
    while top_data[i_ref].split()[0]=='#':
        i_ref += 1
    
    atom_name = []
    atom_type = numpy.zeros(N_atom, dtype=int)
        
    i = 0
    while top_data[i_ref].split()[0] != 'END':
        line_data = top_data[i_ref].split()
        atom_name.append(line_data[2])
        atom_type[i] = int(line_data[3])
        i+=1
        i_ref+=2
        
    # Get C12 and C6
    while top_data[i_ref][:12]!='LJPARAMETERS':
        i_ref +=1
        
    i_ref += 3
    while top_data[i_ref].split()[0]=='#':
        i_ref += 1
        
    C6 = numpy.zeros(N_type, dtype=float)
    C12 = numpy.zeros(N_type, dtype=float)
    
    for i in range(N_type):
        line_data = top_data[i_ref].split()
        IAC = int(line_data[0])
        JAC = int(line_data[1])
        while IAC != JAC:
            i_ref += 1
            line_data = top_data[i_ref].split()
            IAC = int(line_data[0])
            JAC = int(line_data[1])
            
        C12[i] = float(line_data[2])
        C6[i] = float(line_data[3])
        
        i_ref += 2 # Skip # sign in list
        
    # Get atomic radius
    atom_C6  = numpy.zeros(N_atom, dtype=float)
    atom_C12 = numpy.zeros(N_atom, dtype=float)
    
    for i in range(N_atom):
        atom_C6[i] = C6[atom_type[i]-1] # -1 because type start from 1 and Python from 0
        atom_C12[i] = C12[atom_type[i]-1] # -1 because type start from 1 and Python from 0
        
    atom_sigma = (atom_C12/atom_C6)**(1./6)
    atom_radius = 2**(1./6)*atom_sigma
    atom_radius = numpy.nan_to_num(atom_radius) * 5 # x10 (nm to angs)/2 (distance to radius)
    
    # Get positions
    atom_position = numpy.zeros((N_atom,3), dtype=float)
    i_ref = 0
    while cnf_data[i_ref][:8]!='POSITION':
        i_ref +=1  
    i_ref += 1
    
    line_data = cnf_data[i_ref].split()
    i = 0
    while line_data[0]!='END':
        atom_position[i,0] = float(line_data[4])
        atom_position[i,1] = float(line_data[5])
        atom_position[i,2] = float(line_data[6])
        i += 1
        i_ref += 1
        line_data = cnf_data[i_ref].split()
    
    atom_position *= 10 # nm to angs
    
    print(atom_name)
    print(atom_type)
    print (atom_C6)
    print(atom_radius)
    print(atom_position)


read_gromos_files("1ALA_54a7.top", "gch_1ALA.cnf")

