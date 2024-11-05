from initdata import bob, sue, tom
import pickle

for (key, record) in [("bob", bob), ("tom", tom), ("sue", sue)]:
    print(f"Key: {key}\nRecord: {record}")
    recfile = open(key + ".pkl", "wb")
    pickle.dump(record, recfile)
    recfile.close()