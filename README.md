This script is used for homotrimer protein interface residue-residue interaction prediction. 

Python version is 3.6+, and the dependent packages are attached in requirements.txt. Please type

pip install -r requirements.txt

The input values are computed by corresponding tools, which are listed in our paper.  After that we type 

python predictor.py file1 file2 file3 file4 

where file1 and file2 are 1D information from corresponding subunits, file3 and file4 are 2D information.  
  
Here, we give an example for usage：
python scripts/predictor.py example/2bsd_A.txt example/2bsd_B.txt example/2bsd_A_B.mat example/2bsd_A_B.pair.npy


Reference

Zhonghua Hong, Jiale Liu, Yinggao Chen, An interpretable machine learning method for homo-trimeric protein interface residue-residue interaction prediction, Biophysical Chemistry,278(10666),2021.



If you find our paper useful in your research, please cite it:

@article{HONG2021106666,
title = {An interpretable machine learning method for homo-trimeric protein interface residue-residue interaction prediction},
journal = {Biophysical Chemistry},
volume = {278},
pages = {106666},
year = {2021},
issn = {0301-4622},
doi = {https://doi.org/10.1016/j.bpc.2021.106666},
url = {https://www.sciencedirect.com/science/article/pii/S0301462221001484},
author = {Zhonghua Hong and Jiale Liu and Yinggao Chen}
}

