import os
from scipy.io import loadmat
from interpolate import interpolate


def reader():
   # ENTER THE DIRECTORY WHERE YOUR DATA IS STORED
    file_paths = []

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # store all the file paths in the file_paths array and loop through to populate the database
            file_paths.append(os.path.join(directory, filename).replace('\\', '/'))

    for path in file_paths:
        data = loadmat(path)

        freq = list() # Contains all the data for the columns listed below
        col = ['EGT_1', 'EGT_2', 'EGT_3', 'EGT_4',
            'FF_1', 'FF_2', 'FF_3', 'FF_4',
            'FQTY_1', 'FQTY_2', 'FQTY_3', 'FQTY_4',
            'N1_1', 'N1_2', 'N1_3', 'N1_4',
            'N1T', 'N1C',
            'N2_1', 'N2_2', 'N2_3', 'N2_4',
            'OIT_1', 'OIT_2', 'OIT_3', 'OIT_4',
            'OIP_1', 'OIP_2', 'OIP_3', 'OIP_4',
            'PLA_1', 'PLA_2', 'PLA_3', 'PLA_4',
            'VIB_1', 'VIB_2', 'VIB_3', 'VIB_4']

        # col contains the names of the column variables

        high_sampling_rate = len(data['EGT_1'][0][0][0])

        for item in col:
            # Interpolate the data which has sampling rate 1
            if (data[item][0][0][1][0][0] == 1):
                arr1 = interpolate(high_sampling_rate,
                                data[item][0][0][0].flatten().tolist())
                freq.append(arr1)
            # Else append the data in the freq
            else:
                freq.append(data[item][0][0][0].flatten().tolist())

        # return the column names and data while looping through the paths
        return col, freq, path
