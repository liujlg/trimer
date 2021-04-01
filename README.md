This script is used for homotrimer protein interface residue-residue interaction prediction. Python version is 3.6+, and the dependent packages are attached in requirements.txt. Please type

pip install -r requirements.txt

The input values are computed by corresponding tools, which are listed in our paper.  After that we type 

python predictor.py file1 file2 file3 file4 

where file1 and file2 are 1D information from corresponding subunits, file3 is CCMpred information and file4 is contact potential information.  
  
Here, we give an example for usage：
python predictor.py
