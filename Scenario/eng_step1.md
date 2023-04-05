### Creating a Linear Regression Model with Scikit-Learn Library

In this CTF scenario, you are expected to create a Linear Regression model trained on the data we provided, using the Scikit-Learn library, which is one of the most widely used Python libraries in the field of Machine Learning.

Within the scope of the scenario, we expect you to:
* Perform the necessary installations on the assigned machines,
* Download the dataset we prepared for you,
* Train a Linear Regression model with these data using the Scikit-Learn library, and
* Export your model, which is ready for testing.

### Instructions

- You should install Python on the Alpine Linux machine assigned to you using apk commands.
- After installing Python, you should install the Python libraries you will need during the work with the commands of the 'pip' package manager, which is the most commonly used and activated after you install Python. The required libraries are as follows:
  - scikit-learn
  - pickle
  - numpy
  - pandas
  - json
  - requests
  
- You should clone the data sets we provided you for training to your '/home' directory with the 'git clone' command from the following address: **https://github.com/Bulut-Bilisimciler/ctf-regression-traindata.git**.

<!---
Depending on the return regarding the service, we can directly embed the cloning part of the test data into the service if we install the train data inside the machine and run the test script with verify.json.
-->

- Complete your model training using the 'train.csv' file you downloaded with git clone.

```bash
# HINT: Examination of data and variable names

import pandas as pd
data = pd.read_csv('example_data.csv')
data.head()
```

- Don't forget to export the model you trained in your Python script/app for model training to your home directory using the 'Pickle' library.

```bash
# HINT: Save the model with Pickle
import pickle
with open('/home/linear_regression_model.pkl', 'wb') as file:
    pickle.dump(model, file)
```

- After completing all the steps, click on the "Check" button for the control processes and complete the scenario.

### Resources  

- [apk](https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management)  
- [pip](https://pip.pypa.io/en/stable/getting-started/)
- [Scikit-Learn](https://scikit-learn.org/stable/index.html)  