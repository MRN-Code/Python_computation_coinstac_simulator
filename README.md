# Python_computation_coinstac_simulator

This repo hold python version single-shot ridge regression for coinstac.

There are several key points in terms of connecting pythong with coinstac-simulator:

1) coinstac-simulator runs python code in such way: it connects python code with JSON structure generated in previous step. For example

  python ./ridge_regress_master.py --run {"computationId":"testcomputationid","consortiumId":"testconsortiumid1493750822199","pluginState":{"group-step":{"step":1,"userStep":{"testUser1":1}}},"previousData":null,"usernames":["testUser1","testUser2"],"userResults":[{"data":{"beta_vector":[1.0833333333333335,-0.1666666666666667]},"pipelineState":{"inProgress":false,"step":0},"pluginState":{"group-step":{"step":1}},"computationId":"testcomputationid","consortiumId":"testconsortiumid1493750822199","username":"testUser1","userData":{"dirs":["site1"]},"_id":"test_run_id-testUser1","_rev":"1-c4afc47f4faed173cb4421ed1ce933c5"},{"data":{"beta_vector":[1.916666666666667,-0.1666666666666667]},"pipelineState":{"inProgress":false,"step":0},"pluginState":{"group-step":{"step":1}},"computationId":"testcomputationid","consortiumId":"testconsortiumid1493750822199","username":"testUser2","userData":{"dirs":["site2"]},"_id":"test_run_id-testUser2","_rev":"1-3acc4e4c17bff8c47c0ddaad07af6d02"}]}

2) for each part of python code, a JSON structure with output need to be dumped and also sended to coinstac-simulator via sys.stdout.write() command


3) In order to inform coinstac-simulator, the computation is ended. the last JSON output from python code need to include a variable 'complete', and its value need to be set as 'True'
