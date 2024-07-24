
# This repository is intended to help downloading CDS data on the new beta version using the API. 




## Appendix

Please be aware that this method will only work on Cedar cluster if you are using Alliance Canada clusters. This is because cedar is the only cluster with its nodes connected to the internet.




## Installation

You first need to install the cds API on the cluster. In the terminal (once connected), proceed with
```
$ pip install cdsapi
```

You will also need to create a file containing your CDS key:

```
touch ~/.cdsapirc
```
and add your key to this file using a text editor (e.g, vim). See cdsapirc_example file in the repo for an example. You can also visit https://cds-beta.climate.copernicus.eu/how-to-api for instructions.

Once this is done, you are ready to adjust my example scripts and download the data.
## Run the scripts

Once the scripts is adjusted (e.g, you selected the years, months, days, variables, etc.) you can proceed with running the script using the bash file 'submit_era5_downloads.sh'. Please note that you can adjust the time required for your download, depending on the size of the dataset. Please ensure the paths in ALL your files are changed to your own.

You can now proceed with 
```
sbatch submit_era5_downloads.sh
``` 
in the terminal. You can follow your requests either at https://cds-beta.climate.copernicus.eu/requests?tab=all or using 
```
sq
``` 
in the terminal. Enjoy!


## Acknowledgements
Special thanks to Dr. Yan-Ting Chen who previously created some scripts, and I could inspire myself and adjust them to the new beta version. 
 


## Authors

- [@binmenja](https://github.com/binmenja)



