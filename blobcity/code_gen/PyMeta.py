# Copyright 2021 BlobCity, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



"""
This python file consists of class  PyComments,  which has dictionary models and procedures utilized to add comments/meta description in Code generation.
"""
class PyComments:
    models={
        'Classification':{
            'LogisticRegression':"Logistic regression is a statistical model that in its basic form uses a logistic function to model a binary dependent variable,\n# although many more complex extensions exist. In regression analysis,\n# logistic regression (or logit regression) is estimating the parameters of a logistic model (a form of binary regression).\n# This can be extended to model several classes of events\r\n",
            'RidgeClassifier':"Classifier using Ridge regression.\n# This classifier first converts the target values into {-1, 1}\n# and then treats the problem as a regression task (multi-output regression in the multiclass case).\r\n",
            'SGDClassifier':"Stochastic Gradient Descent (SGD) is a simple yet very efficient approach to fitting linear classifiers and regressors\n# under convex loss functions such as (linear) Support Vector Machines and Logistic Regression.\n# SGD is merely an optimization technique and does not correspond to a specific family of machine learning models. It is only a way to train a model.\n# Often, an instance of SGDClassifier or SGDRegressor will have an equivalent estimator in the scikit-learn API,\n# potentially using a different optimization technique.For example,\n# using SGDClassifier(loss='log') results in logistic regression, i.e. a model equivalent to LogisticRegression which is fitted via\n# SGD instead of being fitted by one of the other solvers in LogisticRegression. \r\n",
            'ExtraTreesClassifier':"ExtraTreesClassifier is an ensemble learning method fundamentally based on decision trees.\n# ExtraTreesClassifier, like RandomForest, randomizes certain decisions and subsets\n# of data to minimize over-learning from the data and overfitting.\r\n",
            'RandomForestClassifier':"A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples\n# of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.\n# The sub-sample size is controlled with the max_samples parameter if bootstrap=True,\n# otherwise the whole dataset is used to build each tree.\r\n",
            'AdaBoostClassifier':"AdaBoost is one of the initial boosting ensemble algorithms to be adapted in solving studies.\n# It helps by combine multiple “weak classifiers” into a single “strong classifier.” \n# The core concept of the algorithm is to fit a sequence of weak learners on repeatedly modified versions of the data.\n# The predictions from all the Weak learners are then combined through a weighted majority vote or sum to produce the outcome/Prediction.\n# The data modifications at each iteration consist of applying weights to each of the training samples.\n# Initially, those weights are all set so that the first iteration only trains a weak learner on the original data.\n# For every successive iteration, the sample weights are individually modified, and the algorithm is reapplied to the reweighted data.\n# At a given iteration, those training examples which get incorrectly classified by the model at the previous iteration have their weights increased.\n# Whereas the weight gets decreased for data that has been predicted accurately.\n#As iterations continue, data that are difficult to predict or incorrectly classified receive ever-increasing influence.\n# Each subsequent weak learner is thereby forced to concentrate on the data that are missed by the previous ones in the sequence\r\n",
            'GradientBoostingClassifier':"Gradient Boosting builds an additive model in a forward stage-wise fashion; it allows for the optimization of arbitrary differentiable loss functions.\n# In each stage nclasses regression trees are fit on the negative gradient of the binomial or multinomial deviance loss function.\r\n",
            'HistGradientBoostingClassifier':"Histogram-based Gradient Boosting Classification Tree.This estimator is much faster than GradientBoostingClassifier for big datasets (n_samples >= 10 000).\n# This estimator has native support for missing values (NaNs).\r\n",
            'SVC':"Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.\n# A Support Vector Machine is a discriminative classifier formally defined by a separating hyperplane.\n# In other terms, for a given known/labelled data points, the SVM outputs an appropriate hyperplane that classifies the inputted new cases based on the hyperplane.\n# In 2-Dimensional space, this hyperplane is a line separating a plane into two segments where each class or group occupied on either side.\r\n",
            'NuSVC':"SVC and NuSVC are similar methods, but accept slightly different sets of parameters and have different mathematical formulations.\r\n",
            'LinearSVC':"LinearSVC is similar to SVC with kernel='linear'.\n# It has more flexibility in the choice of tuning parameters and is suited for large samples\r\n",
            'DecisionTreeClassifier':"Decision tree is the most powerful and popular tool for classification and prediction.\n# A Decision tree is a flowchart like tree structure, where each internal node denotes a test on an attribute,\n# each branch represents an outcome of the test, and each leaf node holds a outcome label.\n# As with other classifiers, DecisionTreeClassifier takes as input two arrays:\n# an array X, sparse or dense, of shape (n_samples, n_features) holding the training samples,\n# and an array Y of integer values, shape (n_samples,), holding the class labels for the training samples.\n# It is capable of both binary ([-1,1] or [0,1]) classification and multiclass ([0, …,K-1]) classification.\r\n",
            'KNeighborsClassifier':"KNN is one of the easiest Machine Learning algorithms based on Supervised Machine Learning technique.\n# The algorithm stores all the available data and classifies a new data point based on the similarity.\n# It assumes the similarity between the new data and data and put the new case into the category that is most similar to the available categories.\n# KNN algorithm at the training phase just stores the dataset and when it gets new data,\n# then it classifies that data into a category that is much similar to the available data.\r\n",
            'RadiusNeighborsClassifier':"RadiusNeighborsClassifier implements learning based on the number of neighbors within a fixed radius  of each training point,\n# where  is a floating-point value specified by the user.\n# In cases where the data is not uniformly sampled, radius-based neighbors classification can be a better choice.\r\n",
            'MultinomialNB':'With a multinomial event model, samples (feature vectors) represent the frequencies with which certain events have been generated by a multinomial probability that an event occurs.\n# The multinomial Naive Bayes classifier is suitable for classification with discrete features.\n# The multinomial distribution normally requires integer feature counts. However, in practice, fractional counts such as tf-idf may also work.\r\n',
            'CategoricalNB':'CategoricalNB implements the categorical naive Bayes algorithm for categorically distributed data.\n# It assumes that each feature, which is described by the index , has its own categorical distribution.\n# The categorical Naive Bayes classifier is suitable for classification with discrete features that are categorically distributed.\n# The categories of each feature are drawn from a categorical distribution.\r\n',
            'XGBClassifier':'XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable.\n# It implements machine learning algorithms under the Gradient Boosting framework.\n# XGBoost provides a parallel tree boosting (also known as GBDT, GBM) that solve many data science problems in a fast and accurate way.\r\n',
            'NearestCentroid':'The NearestCentroid classifier is a simple algorithm that represents each class by the centroid of its members.\n # In effect, this makes it similar to the label updating phase of the KMeans algorithm.\n# It also has no parameters to choose, making it a good baseline classifier.\n# It does, however, suffer on non-convex classes, as well as when classes have drastically different variances, as equal variance in all dimensions is assumed.\r\n',
            'Perceptron':'The Perceptron is an algorithm for supervised learning of binary classifiers.\n# The algorithm learns the weights for the input signals in order to draw a linear decision boundary.\n# This enables you to distinguish between the two linearly separable classes +1 and -1\r\n',
            'LGBMClassifier':'LightGBM is a gradient boosting framework that uses tree based learning algorithms.\n# It is designed to be distributed and efficiency\r\n',
            'PassiveAggressiveClassifier':'The passive-aggressive algorithms are a family of algorithms for large-scale learning.\n# They are similar to the Perceptron in that they do not require a learning rate. However, contrary to the Perceptron,\n# they include a regularization parameter C.\r\n',
            'LinearDiscriminantAnalysis':'A classifier with a linear decision boundary, generated by fitting class conditional densities to the data and using Bayes’ rule.\n #The model fits a Gaussian density to each class, assuming that all classes share the same covariance matrix.\n# The fitted model can also be used to reduce the dimensionality of the input by projecting it to the most discriminative directions, using the transform method.\r\n',
            'TF':"Deep learning is a subset of machine learning, which is essentially a neural network with three or more layers.\n# These neural networks attempt to simulate the behavior of the human brain—albeit far from matching its ability—allowing it to “learn” from large amounts of data.\n# While a neural network with a single layer can still make approximate predictions,\n# additional hidden layers can help to optimize and refine for accuracy."
        },
        'Regression':{
            'OrthogonalMatchingPursuit':"OrthogonalMatchingPursuit and orthogonal_mp implements the OMP algorithm for approximating\n# the fit of a linear model with constraints imposed on the number of non-zero coefficients\n# OMP is based on a greedy algorithm that includes at each step the atom most highly\n# correlated with the current residual. It is similar to the simpler matching pursuit (MP) method, but better in that at each iteration, the residual is recomputed using an orthogonal projection on the space of the previously chosen dictionary elements.",
            'LinearRegression':"Linear regression algorithm attempts to model the relationship between two variables by fitting a linear equation to observed data.\n# One variable is considered to be an independent variable, and the other is considered to be a dependent variable. LinearRegression fits a linear model with coefficients w = (w1, …, wp) to minimize the residual sum of squares between the observed targets in the dataset, and the targets predicted by the linear approximation.\r\n",
            'Ridge':"Ridge regression addresses some of the problems of Ordinary Least Squares by imposing a penalty on the size of the coefficients.\n#The complexity parameter  controls the amount of shrinkage: the larger the value of,\n# the greater the amount of shrinkage and thus the coefficients become more robust to collinearity.\n# This model solves a regression model where the loss function is the linear least squares function and regularization is given by the l2-norm.\n# Also known as Ridge Regression or Tikhonov regularization.\n# This estimator has built-in support for multi-variate regression.\r\n",
            'SGDRegressor':"SGDRegressor model Descriptions\r\n",
            'ExtraTreesRegressor':"ExtraTrees Regressor model implements a meta estimator that fits a number of randomized decision trees (a.k.a. extra-trees)\n# on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.\r\n",
            'RandomForestRegressor':"A random forest is a meta estimator that fits a number of classifying decision trees\n# on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.\n# The sub-sample size is controlled with the max_samples parameter if bootstrap=True, otherwise the whole dataset is used to build each tree.\r\n",
            'AdaBoostRegressor':"AdaBoost is one of the initial boosting ensemble algorithms to be adapted in solving studies. It helps by combine multiple 'weak classifiers' into a single 'strong classifier.'\n# The core concept of the algorithm is to fit a sequence of weak learners on repeatedly modified versions of the data.\n# The predictions from all the Weak learners are then combined through a weighted majority vote or sum to produce the outcome/Prediction.\n# The data modifications at each iteration consist of applying weights to each of the training samples.\n# Initially, those weights are all set so that the first iteration only trains a weak learner on the original data. For every successive iteration, the sample weights are individually modified, and the algorithm is reapplied to the reweighted data.    At a given iteration, those training examples which get incorrectly classified by the model at the previous iteration have their weights increased. Whereas the weight gets decreased for data that has been predicted accurately.As iterations continue, data that are difficult to predict or incorrectly classified receive ever-increasing influence.\n# Each subsequent weak learner is thereby forced to concentrate on the data that are missed by the previous ones in the sequence\r\n",
            'GradientBoostingRegressor':"Gradient Boosting builds an additive model in a forward stage-wise fashion;\n# it allows for the optimization of arbitrary differentiable loss functions.\n# In each stage a regression tree is fit on the negative gradient of the given loss function.\r\n",
            'HistGradientBoostingRegressor':"Histogram-based Gradient Boosting Regression Tree.\n# This estimator is much faster than GradientBoostingRegressor for big datasets (n_samples >= 10 000).\n# This estimator has native support for missing values (NaNs). \r\n",
            'SVR':"Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.\n# A Support Vector Machine is a discriminative classifier formally defined by a separating hyperplane.\n# In other terms, for a given known/labelled data points, the SVM outputs an appropriate hyperplane that classifies the inputted new cases based on the hyperplane.\n#  In 2-Dimensional space, this hyperplane is a line separating a plane into two segments where each class or group occupied on either side.\n# Here we will use SVR, the svr implementation is based on libsvm.\n#  The fit time scales at least quadratically with the number of samples and maybe impractical beyond tens of thousands of samples.\r\n",
            'NuSVR':"Support vector machines (SVMs) are a set of supervised learning methods used for classification and regression.\n# A Support Vector Machine is a discriminative classifier formally defined by a separating hyperplane.\n# In other terms, for a given known/labelled data points,\n# the SVM outputs an appropriate hyperplane that classifies the inputted new cases based on the hyperplane.\n# In 2-Dimensional space, this hyperplane is a line separating a plane into two segments where each class or group occupied on either side.\n# Here we will use NuSVR, the NuSVR implementation is based on libsvm.\n# Similar to NuSVC, for regression, uses a parameter nu to control the number of support vectors. However,\n# unlike NuSVC, where nu replaces C, here nu replaces the parameter epsilon of epsilon-SVR. \r\n",
            'LinearSVR':"LinearSVR is similar to SVR with kernel='linear'.\n# It has more flexibility in the choice of tuning parameters and is suited for large samples.\r\n",
            'DecisionTreeRegressor':"DecisionTreeRegressor model DescriptionsDecision tree is the most powerful and popular tool for classification and prediction.\n#  A Decision tree is a flowchart like tree structure, where each internal node denotes a test on an attribute,\n#  each branch represents an outcome of the test, and each leaf node holds a outcome label.\n# Decision trees can also be applied to regression problems, using the DecisionTreeRegressor class.\n# As in the classification setting, the fit method will take as argument arrays X and y,\n#  only that in this case y is expected to have floating point values instead of integer values\r\n",
            'KNeighborsRegressor':"KNN is one of the easiest Machine Learning algorithms based on Supervised Machine Learning technique.\n# The algorithm stores all the available data and classifies a new data point based on the similarity.\n# It assumes the similarity between the new data and data and put the new case into the category that is most similar to the available categories.\n# KNN algorithm at the training phase just stores the dataset and when it gets new data,\n# then it classifies that data into a category that is much similar to the available data.\r\n",
            'Lasso':"Linear Model trained with L1 prior as regularizer (aka the Lasso).\n# The Lasso is a linear model that estimates sparse coefficients.\n# It is useful in some contexts due to its tendency to prefer solutions with fewer non-zero coefficients, effectively reducing the number of features upon which the given solution is dependent.\n# For this reason Lasso and its variants are fundamental to the field of compressed sensing.\r\n",
            'Lars':"Least-angle regression (LARS) is a regression algorithm for high-dimensional data, developed by Bradley Efron,\n# Trevor Hastie, Iain Johnstone and Robert Tibshirani. LARS is similar to forward stepwise regression. At each step,\n# it finds the feature most correlated with the target. When there are multiple features having equal correlation,\n# instead of continuing along the same feature, it proceeds in a direction equiangular between the features.\r\n",
            'BayesianRidge':'Bayesian Regression can be very useful when we have insufficient data in the dataset or the data is poorly distributed.\n# The output of a Bayesian Regression model is obtained from a probability distribution,\n# as compared to regular regression techniques where the output is just obtained from a single value of each attribute.\n# Bayesian regression techniques can be used to include regularization parameters in the estimation procedure:\n# the regularization parameter is not set in a hard sense but tuned to the data at hand.\r\n',
            'LassoLars':'LassoLars is a lasso model implemented using the LARS algorithm,\n# and unlike the implementation based on coordinate descent, this yields the exact solution,\n# which is piecewise linear as a function of the norm of its coefficients.\r\n',
            'XGBRegressor':'XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. \n#It implements machine learning algorithms under the Gradient Boosting framework. XGBoost provides a parallel tree boosting\n# (also known as GBDT, GBM) that solve many data science problems in a fast and accurate way.\r\n',
            'ARDRegressor':'Bayesian ARD regression.Fit the weights of a regression model, using an ARD prior.\n# The weights of the regression model are assumed to be in Gaussian distributions.\n# Also estimate the parameters lambda (precisions of the distributions of the weights) and alpha (precision of the distribution of the noise).\n# The estimation is done by an iterative procedures (Evidence Maximization)\r\n',
            'CatBoostRegressor':'CatBoost is an algorithm for gradient boosting on decision trees.\n# Developed by Yandex researchers and engineers, it is the successor of the MatrixNet\n# algorithm that is widely used within the company for ranking tasks, forecasting and making recommendations\r\n',
            'GammaRegressor':"Generalized Linear Model with a Gamma distribution.This regressor uses the 'log' link function\r\n",
            'LGBMRegressor':'LightGBM is a gradient boosting framework that uses tree based learning algorithms.\n# It is designed to be distributed and efficiency\r\n',
            'RadiusNeighborsRegressor':'RadiusNeighborsRegressor implements learning based on the neighbors within a fixed radius  of the query point,\n# where  is a floating-point value specified by the user.\r\n',
            'PassiveAggressiveRegressor':'The passive-aggressive algorithms are a family of algorithms for large-scale learning.\n# They are similar to the Perceptron in that they do not require a learning rate.\n# However, contrary to the Perceptron, they include a regularization parameter C\r\n',
            'HuberRegressor':"Linear regression model that is robust to outliers.\n#  The Huber Regressor optimizes the squared loss for the samples\n#  where |(y - X'w) / sigma| < epsilon and the absolute loss for the samples where |(y - X'w) / sigma| > epsilon, where w and sigma are parameters to be optimized.\n# The parameter sigma makes sure that if y is scaled up or down by a certain factor, one does not need to rescale epsilon to achieve the same robustness.\n# Note that this does not take into account the fact that the different features of X may be of different scales.\n# This makes sure that the loss function is not heavily influenced by the outliers while not completely ignoring their effect.\r\n",
            'ElasticNet':'Elastic Net first emerged as a result of critique on Lasso, whose variable selection can be too dependent on data and thus unstable.\n# The solution is to combine the penalties of Ridge regression and Lasso to get the best of both worlds.\r\n',
            'PoissonRegressor':"Poisson regression is a generalized linear model form of regression used to model count data and contingency tables.\n# It assumes the response variable or target variable Y has a Poisson distribution, and assumes the logarithm of its expected value can be modeled by a linear combination of unknown parameters.\n# It is sometimes known as a log-linear model, especially when used to model contingency tables.\r\n",
            'TF':"Deep learning is a subset of machine learning, which is essentially a neural network with three or more layers.\n# These neural networks attempt to simulate the behavior of the human brain—albeit far from matching its ability—allowing it to “learn” from large amounts of data.\n# While a neural network with a single layer can still make approximate predictions,\n# additional hidden layers can help to optimize and refine for accuracy."
        }
    }

    procedure={
        'datafetch':"\n### Data Fetch\n# Pandas is an open-source, BSD-licensed library providing high-performance,\n# easy-to-use data manipulation and data analysis tools.\n",
        'missing':"\n### Data Preprocessing\n# Since the majority of the machine learning models in the Sklearn library doesn't handle string category data and Null value,\n# we have to explicitly remove or replace null values.\n# The below snippet have functions, which removes the null value if any exists.\n",
        'encoding':"\n### Data Encoding\n# Converting the string classes data in the datasets\n# by encoding them to integer either using OneHotEncoding or LabelEncoding\n",
        'datasplit':"\n### Train & Test\n# The train-test split is a procedure for evaluating the performance of an algorithm.\n# The procedure involves taking a dataset and dividing it into two subsets.\n# The first subset is utilized to fit/train the model.\n# The second subset is used for prediction.\n# The main motive is to estimate the performance of the model on new data.\n",
        'metrics':"\n### Accuracy Metrics\n# Performance metrics are a part of every machine learning pipeline. \n# They tell you if you're making progress, and put a number on it. All machine learning models,\n# whether it's linear regression, or a SOTA technique like BERT, need a metric to judge performance.\n",
        'x&y':"\n### Feature Selection\n# It is the process of reducing the number of input variables when developing a predictive model.\n# Used to reduce the number of input variables to reduce the computational cost of modelling and,\n# in some cases,to improve the performance of the model.\n",
        'cor_matrix': "### Correlation Matrix\n# In order to check the correlation between the features, we will plot a correlation matrix.\n# It is effective in summarizing a large amount of data where the goal is to see patterns.\n"
    }