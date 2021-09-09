from englisttohindi.englisttohindi import EngtoHindi
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

stopwords_file = open('stop_words.txt', 'w') 
hindi_output = open('hindi_output.txt', 'w', encoding="utf-8")

input_lines = []
stop = []

stopwords_file.writelines("Words\n")
with open('english_input.txt') as f:
    input_lines = f.readlines()
    
    for line in input_lines:

        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(line)

        filtered_sentence = [
            w for w in word_tokens if not w.lower() in stop_words]

        filtered_sentence = []

        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
            else:
                stop.append(w)
        stopwords_file.writelines(" ".join(filtered_sentence))
        stopwords_file.writelines("\n")
        multi_lines = line.split(".")
        print(multi_lines)
        for single_sen in multi_lines:
            if single_sen == '' or single_sen == '\n':
                continue
            # print(single_sen+'\n')
            
            res = EngtoHindi(single_sen)
            print(res.convert)
            hindi_output.writelines(res.convert)
            hindi_output.writelines("| ")
        hindi_output.writelines("\n")
            

    stopwords_file.writelines("\nStop-Words\n")
    stopwords_file.writelines(", ".join(stop))