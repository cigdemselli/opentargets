# opentargets
This Python programme is to query the Open Targets REST API to get association_score.overall for a given target (gene Ensembl id) or disease (EFO id).

The ouput is a) target_id, disease_id, and association_score.overall and b) some statistics (the maximum, minimum and average and standard deviation values) of association_score.overall for a given target or disease.


**Installation of required modules**

Installation of *pandas*, *argparse* and *opentargets* modules are required.

1) Ensure you can run Python from the command line. You can check this by running:
```
python --version
```
This should give an output like `Python 3.6.3`. If this is not the case, please install the latest 3.x version from `python.org`.

2) Ensure `pip` is available. You can check this by running:
```
pip --version
```
This should give an output like `pip 20.3.3`. If this is not the case, download the `get-pip.py` file from https://bootstrap.pypa.io/get-pip.py and install `pip` by running:
```
python get-pip.py
```
3) Install required modules using `pip`.
```
pip install pandas
pip install argparse
pip install opentargets
```

**Arguments**

Programme `scriptOT.py` takes two arguments, `-t` and `-d`. A target `-t` or disease `-d` argument should be provided.

Please provide one argument at a time, either `-t` a target_id such as ENSG00000197386 or `-d` a disease_id such as EFO_0000616.

Running the programme without any parameters or with more than one parameter will give an error.


**Example usage on a unix-like machine**

1) Make sure Python script `scriptOT.py` is in your `PATH`. You can check this by running:
```
ls
```
2) Make the script executable by running:
```
chmod +x scriptOT.py
```
3) load python 
```
module load python
```
4) Run the script

With a target_id such as ENSG00000197386
```
python scriptOT.py -t ENSG00000197386
```

or with a diasease_id such as Orphanet_399
```
python scriptOT.py -d Orphanet_399
```

To access help
```
python scriptOT.py -h
```
