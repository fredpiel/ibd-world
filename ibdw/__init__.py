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


# Time trials:
# mbg-infer ibdw run10 S_Data3b.csv -i 500000 (~35h - re-running as bugged) (33h, Mpro1)
# mbg-map ibdw run10 10000 landseamask2-e_10km_y-x+.asc -r 1 -t 100 -q '0.010 0.020 0.025 0.030 0.040 0.050 0.060 0.070 0.080 0.090 0.100 0.110 0.120 0.130 0.140 0.150 0.160 0.170 0.180 0.190 0.200 0.210 0.220 0.230 0.240 0.250 0.260 0.270 0.280 0.290 0.300 0.310 0.320 0.330 0.340 0.350 0.360 0.370 0.380 0.390 0.400 0.410 0.420 0.430 0.440 0.450 0.460 0.470 0.480 0.490 0.500 0.510 0.520 0.530 0.540 0.550 0.560 0.570 0.580 0.590 0.600 0.610 0.620 0.630 0.640 0.650 0.660 0.670 0.680 0.690 0.700 0.710 0.720 0.730 0.740 0.750 0.760 0.770 0.780 0.790 0.800 0.810 0.820 0.830 0.840 0.850 0.860 0.870 0.880 0.890 0.900 0.910 0.920 0.930 0.940 0.950 0.960 0.970 0.975 0.980 0.990 1.000'
# should take a small number of hours.