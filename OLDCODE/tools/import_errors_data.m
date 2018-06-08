function [ freq_table ] = import_errors_data( path, freq_table, col )
    delimiter = '\t';
    formatSpec = '%s%f%[^\n\r]';
    fileID = fopen(path,'r');
    dataArray = textscan(fileID, formatSpec, 'Delimiter', delimiter,  'ReturnOnError', false);
    fclose(fileID);
    tuples = dataArray{:, 1};
    freq = dataArray{:, 2};
    clearvars filename delimiter formatSpec fileID dataArray ans;
    
    freq_table(:,col) = freq(3:7);

end

