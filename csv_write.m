% Load the variable as array (data variable)
data = cat(2,EGT_1.data, EGT_2.data, EGT_3.data, EGT_4.data,...
            N1_1.data, N1_2.data, N1_3.data, N1_4.data,... 
            N2_1.data, N2_2.data, N2_3.data, N2_4.data,...
            PLA_1.data, PLA_2.data, PLA_3.data, PLA_4.data,...
            VIB_1.data,VIB_2.data,VIB_3.data,VIB_4.data);

% Array to table
T = array2table(data,...
                'VariableNames',{  'EGT_1', 'EGT_2', 'EGT_3', 'EGT_4',...
                'N1_1', 'N1_2', 'N1_3', 'N1_4',...
                'N2_1', 'N2_2', 'N2_3', 'N2_4',...
                'PLA_1', 'PLA_2', 'PLA_3', 'PLA_4',...
                'VIB_1','VIB_2','VIB_3','VIB_4'});
        

%Converting the data into csv file
csvwrite('vib1',data);
