class dictionary(object):
    def __init__(self):
        self.dict_keys=[]
        self.dict_values=[]
    def set_value(self,v,k):
        try:
            self.dict_values[self.dict_keys.index(v)]=k
        except:
            self.dict_keys.append(v) ; self.dict_values.append(k)
    def get_value(self,v):
        try:
            return self.dict_values[self.dict_keys.index(v)]
        except:
            raise KeyError
    def del_value(self,v):
        try:
            self.dict_values.pop(self.dict_keys.index(v))
            self.dict_keys.remove(v)
        except:
            raise KeyError