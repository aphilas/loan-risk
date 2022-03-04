**Department of Computing and Informatics** \
**CSC 452 Knowledege Discovery and Data Mining**

# Assignment Report

| Date       | Assignment     |
| ---------- | -------------- |
| 04/03/2022 | Loan Risk Data |

## Group Members

| Reg. No       | Name                  | Role                                                               |
| ------------- | --------------------- | ------------------------------------------------------------------ |
| P15/1214/2018 | Christine Wanjau      | KNN model development, report writing                              |
| P15/1210/2018 | Agunda Vareen Rose    | Feature selection, Decision Tree model development, report writing |
| P15/81790/217 | Omangi Neville Mogita | Feature selection, SVM model development                           |

## Questions

1. **Study the dataset first.**
   1. **Describe the dataset.** \
The dataset is gotten from a bank in one of the states in the USA. It describes a bank’s clients with respect to whether they qualify for loans, that is whether, they are a bad loss,  bad profit or a good risk. \
The data attributes that form the dataset columns are as follows:
      * ID - client record identification number, which is a random integer
      * AGE - a client’s age, stored as an integer
      * INCOME - a client’s annual income in USD
      * GENDER - a client's gender, of which valid values are m or f
      * MARITAL	- the client’s marital status of which valid values include single, married or divorced/separated/widowed (represented as divsepwid)
      * NUMKIDS	- the client's number of dependant children, represented as an integer
      * NUMCARDS - the number of electronic cards in use by the client (and his/her family), represented as an integer	
      * HOWPAID	- how the client is paid of which valid values are, monthly or weekly
      * MORTGAGE - whether or not the client has a mortgage, represented as a y for yes and n for no
      * STORECAR - the number of Store Cards with the client (and with family), represented as an integer
      * LOANS RISK - a classification of the client's Loan Risk, of which valid classes are bad profit, bad loss or good risk

1. **Using three different classification algorithms, after some suitable data description, data preparation and processing classify the data and try and achieve the highest accuracy.**
   1. **Identify the attributes that can be discretized**
      * INCOME
      * AGE
      * NUMKIDS
      * NUMCARDS
      * STORECAR
      * LOANS
   2. **Discretize these attributes using two different bins and see whether they affect the accuracy of your Model. Explain the thinking behind the discretization.** \
      The attributes were discretized using different sets of bins, and the bins that yielded the highest score retained. In most cases binning resulted in better accuracies as it increases the model’s ability to generalize. The bin sizes were generated based on the quartiles of the data, the mean, and intuition. The eventual bin border are highlighted below:
      * INCOME: 15000, 20000, 24000, 30000, 42000, 60000
      * AGE: 17, 21, 31, 41, 51
      * NUMKIDS: -1,0,1,5
      * NUMCARDS: -1,1,2,7
      * STORECAR: -1,1,2,3,6
      * LOANS: -1,0,1,6
2. **Extract 20% of the dataset randomly for testing and use the rest for training and parameter tuning.** \
   _DONE IN CODE_
3. **What attributes were the most relevant and which ones were irrelevant for your model?** \
   The attributes `INCOME`, `LOANS`, `NUMKIDS`, and `NUMCARDS` are the most relevant. \
   `STORECAR`, `GENDER`, `AGE`, `HOWPAID` didn't seem to change the score by much.
   1. **Explain the process used to achieve this** \
   Multiple rounds of training and scoring were performed, with each attribute excluded, and the mean score used to gauge which attribute's absence yielded the lowest scores.
4. **What is the highest and lowest classification accuracies that you are able to achieve?**
   * Highest classification accuracies
     * The DT score was 0.788834
     * The KNN score was 0.71966
     * The SVM score was 0.76092
   * Lowest classification accuracies
     * The DT score was 0.60558
     * The KNN score was 0.61
     * The SVM score was 0.64

## Observations
In KNN, increasing the number of neighbours resulted in lower scores and in DT increasing tree depth led to lower accuracies.

## Usage
```sh
pip install -r requirements.txt
python bank-loan-risk.py # or execute jupyter notebook instead
```
