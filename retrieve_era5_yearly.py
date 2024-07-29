#!/usr/bin/env python
import calendar
import cdsapi
import os
import sys

f = open('badfile_name.txt', 'a')
c = cdsapi.Client()

def retrieve_interim(year):
    """
       A function to retrieve ERA5 data for a given year.
    """

    monthStart = 1
    monthEnd = 12

    for month in range(monthStart, monthEnd + 1):
        numberOfDays = range(1, calendar.monthrange(year, month)[1] + 1)
        target_year_dir = "/project/6006604/binmenja/cdsapi/%04d" % year
        target_month_dir = "%02d" % month

        if not os.path.exists(target_year_dir):
            os.makedirs(target_year_dir)

        target_month_dir = os.path.join(target_year_dir, target_month_dir)
        if not os.path.exists(target_month_dir):
            os.makedirs(target_month_dir)

        for day in numberOfDays:
            print("Requesting %04d%02d%02d" % (year, month, day))
            startYear = '%04d' % year
            startMonth = '%02d' % month
            startDay = '%02d' % day
            target = os.path.join(target_month_dir, "%04d%02d%02d.nc" % (year, month, day))
            

            if not os.path.exists(target):
                interim_request(startYear, startMonth, startDay, target)
                f.write(startYear + startMonth + startDay)
                f.write('\n')

            else:
                print(f"File {target} already exists. Skipping request.")

def interim_request(startYear, startMonth, startDay, target):
    """
        An ERA interim request for analysis pressure level data.
    """
    output_path = target
    c = cdsapi.Client(timeout=600, quiet=False, debug=False)
    c.retrieve(
        'reanalysis-era5-pressure-levels',
        {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            'area': [
                71.5, -156.5, 71,
                -156,
            ],
            "year": startYear,
            "month": startMonth,
            "day": startDay,
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
            'variable': [
                'fraction_of_cloud_cover', 'ozone_mass_mixing_ratio', 'specific_humidity',
                'temperature',
            ],
            'pressure_level': [
                '1', '2', '3',
                '5', '7', '10',
                '20', '30', '50',
                '70', '100', '125',
                '150', '175', '200',
                '225', '250', '300',
                '350', '400', '450',
                '500', '550', '600',
                '650', '700', '750',
                '775', '800', '825',
                '850', '875', '900',
                '925', '950', '975',
                '1000',
            ],
        },
        output_path)

if __name__ == '__main__':

    year = int(sys.argv[1])
    retrieve_interim(year)

