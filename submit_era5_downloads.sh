#!/bin/bash

for year in {1998..2023}; do
    echo "Submitting job for year: $year"

    # Create a temporary sbatch script
    sbatch_script=$(mktemp)

    cat <<EOT > $sbatch_script
#!/bin/bash
#SBATCH --account=def-yihuang
#SBATCH --job-name=era5_download_$year
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=100:00:00  # 1 hour
#SBATCH --mem-per-cpu=2G  # Adjust memory as needed
#SBATCH --output=era5_download_$year_%j.out
#SBATCH --error=era5_download_$year_%j.err

module load python
source ENV/bin/activate

echo "Running download for year: $year"
python /home/binmenja/projects/def-yihuang/binmenja/cdsapi/retrieve_era5_yearly.py $year
EOT

    # Submit the job
    sbatch $sbatch_script

    # Optionally, you can remove the temporary script file after submission
    # rm $sbatch_script
done

