# BlobCity AutoAI
A framework to find, train and generate code for the best performing AI model. Works on Classification and Regression problems.

Framework is currently designed for tabluar data, and is being extended to support images, videos and natural language. 

# Getting Started
``` shell
pip install blobcity
```

``` Python
import blobcity as bc
bc.train(file="data.csv", target="Y_column")
bc.spill("my_code.ipynb")
```
`Y_column` is the name of the target column. The column must be present within the data provided. 

Automatic inference of Regression / Classification is supported by the framework.

Support input data formats are `.csv` and `.xlsx`. Extension for other file formats is being worked on. 

The `spill` function generates the model code with exhaustive documentation. Training code is also included for basic scikit-learn models. TensorFlow and other DNN models produce only the test / final use code. 

## Use a Pandas Data Frame
``` Python
bc.train(df=my_df, target="Y_column")
```

If loading data from a Database or external system, create a DataFrame from your data source, and pass it directly to the `train` function.

## From a URL
``` Python
bc.train(file="https://example.com/data.csv", target="Y_column")
```

The `file` parameter can be a local file, or a URL. The function will load the data from URL specified. The file at the URL must be either in CSV or XLSX format. The URL should be accessible publicly without authentication. 

# Code Generation
Multiple formats of code generation is supported by the framework. The `spill` function can be used to generate both `ipynb` and `py` files. The desired type is infered from the name of the output file. The code file will be created at the path specified. Relative or absolute file paths, are both supported. 

### Generate Jupyter Notebook
``` Python
bc.spill("my_code.ipynb");
```
Generates an ipynb file with full markdown documentation of the various code lines generated by the model

### Generate Python Code
``` Python
bc.spill("my_code.py")
```
Generates a Python code file. Code documentation is intentially avoided by default to keep the Python code clean. 

``` Python
bc.spill("my_code.py", docs=True)
```
Pass the optional `docs` parameter to generate Python code along with full code documentation. 

# Specifying Features
Framework automatically performs a feature selection. All features are selected by default for feature selection.
Framework is smart enough to remove ID / Primary key columns. 

Use the below code if you would like to manually specify the features to be used for training. 

``` Python
bc.train("data.csv", target="Y_value", features=["col1", "col2", "col3"])
```

# Printing Model Stats
``` Python
model = bc.train(file='./test.csv')
```
