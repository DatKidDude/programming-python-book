import pickle, glob

for filename in glob.glob("*.pkl"):
    with open(filename, "rb") as recfile:
        record = pickle.load(recfile)
        print(filename, "=>\n", record)
    # recfile = open(filename, "rb")
    # record = pickle.load(recfile)
    # print(filename, "=>\n", record)
    # recfile.close()


suefile = open("sue.pkl", "rb")
print(pickle.load(suefile)["name"])
suefile.close()