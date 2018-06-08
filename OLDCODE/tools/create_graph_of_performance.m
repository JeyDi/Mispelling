path_begin = 'C:\Users\kivid\Dropbox\Universita\Corsi Magistrale\Modelli probabilistici per le decisioni\Progetto Mispelling\HMMispelling\results\performance\apple_tweets_autowrong_words_corrected_PseudoUniform_key-prob=';
path_end = '_word_evaluation_index.txt';
freq_table = zeros(5, 19);
col = 1;

for var = 0.05:0.05:0.95
    
    path_var = num2str(var);
    path = strcat(path_begin, path_var);
    path = strcat(path, path_end);
    
    freq_table = import_errors_data(path, freq_table, col);
    
    col = col + 1;
    
end

linspace = (