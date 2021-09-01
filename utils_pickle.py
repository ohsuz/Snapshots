import pickle


def save_pickle(save_path, data):
    file = open(save_path, "wb")
    pickle.dump(data, file)
    file.close()
    return None


def get_pickle(pickle_path):
    f = open(pickle_path, "rb")
    data = pickle.load(f)
    f.close()
    return data
