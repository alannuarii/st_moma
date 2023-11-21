import pandas as pd
from joblib import load

# Inisiasi File Model
md_moma = 'model/mode_operasi.pkl'

# mode = ['1PV', '1PV-1BSS', '2PV', '2PV-1BSS', '2PV-2BSS', '1PV-1BSS-1DG', '2PV-2BSS-1DG', '2PV-2BSS-2DG', 'NOT OPERATING']

def mode_prediction(pv, bss, pltd, cuaca, irr):
    data = {'pltd': pltd,
    'pv': pv,
    'bss': bss,
    'cuaca': cuaca,
    'irr': irr}

    features = pd.DataFrame(data, index=[0])

    loaded_model = load(md_moma)

    prediction = loaded_model.predict(features)

    return prediction[0]


print(mode_prediction(2,2,2,1,1))
