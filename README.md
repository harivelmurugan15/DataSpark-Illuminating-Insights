# DataSpark-Illuminating-Insights
In this project we have done Data Cleaning and Preprocessing at the earlier stages of the project with python, We have done EDA and data merging of the given dataset based on their relationship. For Visualization we have used POWER BI

# Data-Cleaning
The Uncleaned dataset is stored in the We have used pandas for data cleaning for installing pandas please refer this documentation: https://pandas.pydata.org/docs/getting_started/install.html

In  data cleaning we have handled missing dates and removed the string values in price column to make it completely numeric.

We have also transformed the birthday column data into Age column and Overall after cleaning the raw data this is stored in the Cleaned_dataset folder.

# Data-Merging
We have merged the dataset with one another by identifying a common column in it using Pandas.The below mention merged datasets are stored in the merged_data:
   1. sales_customer_data.csv
   2. sales_exchange_data.csv
   3. sales_product_data.csv
   4. sales_store_data.csv

# Data Loading to SQL database
We have loaded to cleaned and merged data into the database with MySQL, Please follow the below steps for the installation of the MySQL :  
      
Download MySQL Installer:

        MySQL Installation
        Download MySQL Installer:
        
        Visit the MySQL Community Downloads page.
        Select the appropriate MySQL Community Server version for your operating system (e.g., Windows, macOS, Linux).
        Download the installer package.
        Run the Installer:
        
        Windows:
        
        MySQL Installation
        Download MySQL Installer:
        
        Visit the MySQL Community Downloads page.
        Select the appropriate MySQL Community Server version for your operating system (e.g., Windows, macOS, Linux).
        Download the installer package.
        Run the Installer:
        
        Windows:
        
        Double-click the downloaded installer (.msi file).
        Follow the prompts in the MySQL Installer wizard.
        During installation, you'll be prompted to choose components to install (MySQL Server, MySQL Workbench, etc.). Select MySQL Server and any other components you need.
        Set up a root password when prompted. Remember this password, as it will be required to access MySQL.
        Complete the installation process.
        
        macOS:
        
        Download the macOS DMG file from the MySQL Community Downloads page.
        Double-click the DMG file to open it.
        Drag the MySQL installer package to the Applications folder.
        Open the MySQL installer package and follow the prompts to install MySQL Server.
        Set up a root password when prompted.
        Follow any additional instructions provided during installation.

        Linux:

        On Linux systems, MySQL can often be installed using the package manager specific to your distribution (e.g., apt for Ubuntu/Debian, yum for CentOS/RHEL).
Install mysql.connector:

You can install mysql.connector using pip, which is the recommended package installer for Python:

           pip install mysql-connector-python

In the data loading process we have created sql table and inserted the respective data into it.

# Data Visualization in POWER-BI

Download and Install the POWER-BI application by this website: https://www.microsoft.com/en-us/power-platform/products/power-bi/downloads

Download the sales_customer.pbix file and open it in POWER-BI this contains the report of the valuable insights from the mergered data

# Data-Extraction
we have used 10 different MySQL quieries for the extraction of the valuable data from the cleaned and merged dataset and stored the extracted data in the extracted_data folder.



   
    
