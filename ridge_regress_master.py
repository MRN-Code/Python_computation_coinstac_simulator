import json;
import argparse
from os import listdir
from os.path import isfile, join
import sys
import numpy as np
import sklearn
import sklearn.linear_model


parser = argparse.ArgumentParser(description='read beta vector from single site and do beta averaging!')
parser.add_argument('--run', type=str,  help='grab coinstac args')
args = parser.parse_args()
args.run = json.loads(args.run)

#inspect what args were passed
#runInputs = json.dumps(args.run, sort_keys=True, indent=4, separators=(',', ': '))
#sys.stderr.write(runInputs + "\n")

#if 'remoteResult' in args.run and \
#    'data' in args.run['remoteResult'] and \
#    username in args.run['remoteResult']['data']:
#    sys.exit(0); # no-op!  we already contributed our data



user_results = args.run['userResults']

sum_beta_vector = np.zeros(np.shape(user_results[0]['data']['beta_vector']))
n_site = len(user_results)

for i in range(0,n_site):
    sum_beta_vector = sum_beta_vector + user_results[i]['data']['beta_vector']

avg_beta_vector = sum_beta_vector/n_site 

sys.stderr.write("Done! averaged beta vector is : {}".format(avg_beta_vector)+"\n")

computationOutput = json.dumps({'complete': True, 'avg_beta_vector': avg_beta_vector.tolist()}, sort_keys=True, indent=4, separators=(',', ': '))

# preview output data
#sys.stderr.write(computationOutput + "\n")

# send results
sys.stdout.write(computationOutput)

