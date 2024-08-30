# Use the OSDR Public AWS S3 Bucket  

## Getting Started with AWS and OSDR Data  

This guide is for new users who want to access and work with the Open Science Data Repository (OSDR) data available on the Registry of Open Data on AWS. As part of the Science Mission Directorate (SMD) Open-Source Science Initiative, this effort aims to enhance data accessibility for open science within the NASA space biology community. Through the OSDR S3 bucket, users can access a diverse range of data including microbe, plant, fruit fly, rodent, human cell culture, ground study, and commercial astronaut studies. This guide will walk you through the steps of installing the AWS Command Line Interface (CLI) and utilizing it to access OSDR data.  

## Introduction to OSDR Data on AWS  

OSDR data is available on the Registry of Open Data on AWS, providing increased accessibility to open science data across NASA and the space biology community. The OSDR S3 bucket offers a wide range of data types for exploration and analysis.  

To get started, you have two primary methods to access and explore OSDR data:  

1. **AWS S3 Browser Interface**: This web-based interface allows you to visually browse and interact with the OSDR data. Access the [browser interface](http://nasa-osdr.s3-website-us-west-2.amazonaws.com/) to get started.  

2. **AWS Command Line Interface (CLI)**: The AWS CLI is a powerful tool that enables programmatic access to AWS services, including OSDR data. This guide will focus on using the CLI to access OSDR data programmatically.  

## Installing the AWS CLI  

Before you can start working with OSDR data using the AWS CLI, you need to install it on your system. Follow these steps to install the AWS CLI:  

1. Open a terminal window.  
2. Visit the [AWS CLI installation instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) for detailed steps.  
3. Once the AWS CLI is installed, you're ready to start exploring OSDR data programmatically.  

## Exploring OSDR Data  

Now that you have the AWS CLI installed, you can use it to explore OSDR data in the S3 bucket. Here are some basic commands to help you get started:  

- To list the contents of the OSDR S3 bucket:  
  ```
  aws s3 ls --no-sign-request s3://nasa-osdr/
  ```

- To list the contents of a specific OSDR dataset (e.g., OSD-96):  
  ```
  aws s3 ls --no-sign-request s3://nasa-osdr/OSD-96/ --recursive
  ```

## Copying Data Locally  

To copy specific files from the OSDR S3 bucket to your local machine, you can use the `aws s3 cp` command. For example:  

- To copy a specific file to your local directory:  
  ```
  aws s3 cp --no-sign-request s3://nasa-osdr/OSD-96/version-6/rna_seq/GLDS-96_rna_seq_Dmel_Can-S_wo_GC_5th-gen-GC-der_1.5hr_GSM2350418_R2_raw.fastq.gz_trimming_report.txt .
  ```

- To copy all files within a specific dataset to your local directory:  
  ```
  aws s3 cp --no-sign-request s3://nasa-osdr/OSD-96/ . --recursive
  ```

## Additional Resources  

If you're looking to delve deeper into OSDR data access and AWS capabilities, consider exploring the following resources:  

- [AWS CLI Documentation](https://docs.aws.amazon.com/cli/): Comprehensive documentation for the AWS CLI, covering various commands and features  
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/): Learn more about Amazon Simple Storage Service (S3) and its capabilities  
- [Registry of Open Data on AWS](http://nasa-osdr.s3-website-us-west-2.amazonaws.com/): Explore the OSDR data repository using the AWS S3 browser interface  
- [NASA Space Biology Open Science Data Repository (OSDR)](https://osdr.nasa.gov/): Official website for the OSDR project, providing information about datasets and research  

This tutorial serves as a starting point for beginners to access and explore OSDR data using the AWS CLI. As you become more familiar with the tools and resources, you can expand your knowledge and take advantage of advanced features for data analysis and research.  

Please [Contact Us](mailto:arc-dl-osdr-data@mail.nasa.gov) if you have any questions or need further assistance. Happy exploring the world of open science data on AWS!  
