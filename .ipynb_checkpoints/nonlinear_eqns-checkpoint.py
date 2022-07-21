########## Non-linear system of equations solver ##########

###### Import packages

import numpy as np
import pandas as pd
import scipy.optimize as opt

###### Specify known values

### Constants
Kc  = 0.2      # mol / L
yA_0 = 1.0     # mol / mol
P   = 10.0      # atm
R   = 0.082    # atm L / mol K
T   = 340      # K

###### Define system of equations

def alg(U):
    
    ### Redefine inputs
    CA0 = U[0]
    Xe = U[1]
    
    ### Define equations
    setzero = np.zeros(len(U))
    setzero[0] = CA0-yA_0*P/R/T
    setzero[1] = Xe - (Kc*(1-Xe)/(4*CA0))**0.5
    
    ### Reorganize list to fit required dimensions 
    setzero = np.array(setzero).tolist()
    
    return setzero

###### Solve based on initial guesses

### Initial guesses
varguess = [0.5,0.5]

### Solver
U = opt.fsolve(alg,varguess)   # Enter function vollowed by variable guesses
U = np.array(U)                # Convert to numpy array for convenience

### Verify that solution was achieved
zerocheck = alg(U)
print("Zerocheck: ",zerocheck)

### Save results in dataframe
soln = pd.DataFrame(['Var 1','Var 2'],columns = ['Variables'])
soln[['Values']] = pd.DataFrame(U)
print(soln)