# PHI_FLOW
### Brief Overview:
Mobile applications are widely used by individuals and by
organizations in the health industry. It is forecasted that
in 2022, there will be 86.3 million users of health or fitness
apps in the United States, which is 30% of adult smartphone
users 1. To provide services, these applications collect users’
personal data which is protected health information (PHI).
It is obligatory for these applications to provide safeguards
for such information in addition to getting permissions from
users (enforced by platforms like Android/iOS). In case of
a breach, the data and financial loss are irrecoverable. So,
this sensitive health data should be breach-proof while held
by applications. In this study, we examine such applications
using taint analysis, a static analysis method for identifying
information leakage from applications. We gather empirical
data of possible application providers’ intended use case for
users and if this leakage is in the wrong hands (Attacker)
what can be major consequences. The purpose of our study is
to make an organized dataset (which is currently not widely
available) for future research applications and provide possi-
ble resolutions to avoid PHI compromises from application
developers. Moreover, regulatory bodies can use this data to
safeguard users providing compliance information.

## Analysis steps
1. Running FlowDroid on every app in our database using script [autoAnalyseApps.py](autoAnalyseApps.py).
2. From [Analysis/](Analysis/) check txt files one by one for leaks.
3. We have documented the leaks in [ManualTestingOfReportedLeaks.txt](ManualTestingOfReportedLeaks.txt).
4. Also we have added our manual inspection (whether the leaks by FlowDroid is false positive or not) on decompiled (by [jadx](https://github.com/skylot/jadx)) apk source files. Our final dataset table given in excel format in [sample_dataset.xlsx](sample_dataset.xlsx).

## Usage & Contribution Guide

### Step 1.
[autoAnalyseApps.py](autoAnalyseApps.py) runs FlowDroid (Install from [here](https://github.com/secure-software-engineering/FlowDroid])) in your system on every application in [Apps/](Apps/) directory. You might need to modify the path according to your need.
### Step 2.
Check [Analysis/](Analysis/) directory for txt files of FlowDroid analysis. There are some errors in FlowDroid where the script gets stuck. We will improve that in future may be adding some timeout or excluding those applications depending on the output of FlowDroid.
### Step 3.
You can run jadx on APKs separately to check the inside code for false positives and intent specification.
### Step 4.
[ManualTestingOfReportedLeaks.txt](ManualTestingOfReportedLeaks.txt) is the place where to document the leaking functions from txt files and giving verdict of false positives.
### Step 5.
Finally we also have the final dataset excel ([sample_dataset.xlsx](sample_dataset.xlsx)) file which contains our verdict of developer intent and attacker intent using STRIDE model.




