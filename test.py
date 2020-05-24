import pickle
# with open('modbus_pkl_10','rb') as f:
#     data = pickle.load(f)
# for i in range(len(data)):
#     print(data[i])

with open('seqgan-master/data/save/generated_sentences.txt','rb') as f:
    generate_data = pickle.load(f)

for i in range(len(generate_data)):
    print(bytes(generate_data[i]))