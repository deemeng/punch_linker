import os
from params.hyperparams import *
from params.utils import create_folder

# 1. trained models
path_predictor = 'predictor'

path_output = 'output'
path_prediction = os.path.join(path_output, 'disorder')
create_folder(path_prediction)
path_time = os.path.join(path_output, 'timings.csv')

# 2. Data
path_data = 'data'
path_input_json = os.path.join(path_data, 'input.json')

path_seq = os.path.join(path_data, 'seq')
create_folder(path_seq)

path_input = os.path.join(path_data, 'input.fasta')
path_msaTrans = os.path.join(path_data, 'msaTrans')
path_protTrans = os.path.join(path_data, 'protTrans')




'''
import os

path_input_file = 'test_input.fasta'
path_addInput_hhblits = os.path.join('example', 'hhblits') # path to hhblit results folder. a3m format
path_addInput_protTrans = '' # path to protTrans results folder. .npy files
path_addInput_msaTransformer = '' # path to msa_transformer results folder. .npy files
'''