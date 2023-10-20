import pandas as pd
import pickle

# Inisiasi File Model
md_moma = 'model/mode_operasi.pkl'

mode = ['1PV', '1PV-1BSS', '2PV', '2PV-1BSS', '2PV-2BSS', '1PV-1BSS-1DG', '2PV-2BSS-1DG', '2PV-2BSS-2DG', 'NOT OPERATING']

def mode_prediction(pltd, pv, bss, cuaca, irr):
    data = {'pltd': pltd,
    'pv': pv,
    'bss': bss,
    'cuaca': cuaca,
    'irr': irr}

    features = pd.DataFrame(data, index=[0])

    with open(md_moma, 'rb') as file:
        loaded_model = pickle.load(file)

    prediction = loaded_model.predict(features)

    return mode[prediction[0]]