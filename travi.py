import numpy as np


#ide kell beirni, h. mibol mennyid van (vagy mennyit szeretnel felhasznalni)
fa = 82000
tegla = 78000
vas = 77000


ei = {
    "fa": 350,
    "tegla": 260,
    "vas": 180
}

impi = {
    "fa": 100,
    "tegla": 110,
    "vas": 140
}

kata = {
    "fa": 690,
    "tegla": 1000,
    "vas": 400
}
#****************************************************

#EI IMPI KATA
EIK = np.array([
    [ei["fa"],impi["fa"],kata["fa"]],
    [ei["tegla"],impi["tegla"],kata["tegla"]],
    [ei["vas"],impi["vas"],kata["vas"]]
    ])


#EI IMPI
EI = np.array([
    [ei["fa"],impi["fa"]],
    [ei["tegla"],impi["tegla"]],
    [ei["vas"],impi["vas"]]
    ])
 

#EI KATA  
EK = np.array([
    [ei["fa"],kata["fa"]],
    [ei["tegla"],kata["tegla"]],
    [ei["vas"],kata["vas"]]
    ]) 


#IMPI KATA
IK = np.array([
    [impi["fa"],kata["fa"]],
    [impi["tegla"],kata["tegla"]],
    [impi["vas"],kata["vas"]]
    ])

#****************************************************
B = np.array([fa, tegla, vas])

#X = np.linalg.solve(A,B)
#X = np.linalg.lstsq(A,B)

try:
    X = np.linalg.lstsq(EIK,B,rcond=None)
    print("ei: ", int(round(X[0][0])))
    print("impi: ", int(round(X[0][1])))
    print("kata: ", int(round(X[0][2])))
except:
    print("")   

print("\n")  

try:
    X = np.linalg.lstsq(EI,B,rcond=None)
    print("ei: ", int(round(X[0][0])))
    print("impi: ", int(round(X[0][1])))
except:
    print("")  

print("\n")    

try:
    X = np.linalg.lstsq(EK,B,rcond=None)
    print("ei: ", int(round(X[0][0])))
    print("kata: ", int(round(X[0][1])))
except:
    print("")

print("\n")

try:
    X = np.linalg.lstsq(IK,B,rcond=None)
    print("impi: ", int(round(X[0][0])))
    print("kata: ", int(round(X[0][1])))
except:
    print("")