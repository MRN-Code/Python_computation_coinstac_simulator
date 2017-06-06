
'use strict';

module.exports = { // eslint-disable-line
  name: 'ridge_regression',
  version: '0.0.1',
  cwd: __dirname,
  local: {
    type: 'docker',
    cmd: 'python',
    args: ['./ridge_regress_local.py'],
    verbose: true,
  },
  remote: {
    type: 'docker',
    cmd: 'python',
    args: ['./ridge_regress_master.py'],
    verbose: true,
  },
  plugins:['group-step'],
};
