# OpenFOAM_div_test
(c) 2020 Evstigneev N.M.
GPLv3 licence.

# OpenFOAM divergence test with Rhie-Chow interpolation

This test besically executes OpenFOAM on different mesh sized and calculates norms of divergence distributions.
Divergence is calculated using standard routine be OpenFOAM and is then calculated using 'postProcess' tool.
Maximum and integral norms are used, namely C_norm and L2_norm. 
Observe, that C_norm increaes, while L2_norm is bounded as \BigO(1).

To run the tests in automated mode execute 'python get_all_tests.py'. Designed to be used in docker.
Results are placed into the file 'div_res.dat'.

