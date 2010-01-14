# from mcmc import *
from generic_mbg import invlogit
import pymc as pm
from cut_geographic import cut_geographic, hemisphere
import ibdw
import os
root = os.path.split(ibdw.__file__)[0]
pm.gp.cov_funs.cov_utils.mod_search_path.append(root)

import cg
from cg import *

cut_matern = pm.gp.cov_utils.covariance_wrapper('matern', 'pymc.gp.cov_funs.isotropic_cov_funs', {'diff_degree': 'The degree of differentiability of realizations.'}, 'cut_geographic', 'cg')

def check_data(ra):
    pass

from model import *

nugget_labels={'sp_sub': 'V'}
obs_labels = {'sp_sub': 'eps_p_f'}

def mcmc_init(M):
    M.use_step_method(pm.gp.GPEvaluationGibbs, M.sp_sub, M.V, M.eps_p_f)

metadata_keys = ['fi','ti','ui']
map_postproc = invlogit
non_cov_columns = {'lo_age': 'int', 'up_age': 'int', 'pos': 'float', 'neg': 'float'}