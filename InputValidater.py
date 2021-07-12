class InputValidater:
  def __init__(self):
    self._char_set=set()
    self._space=[32,10]
    _input_file=open(0)
    self._input_data=list(_input_file.read())
    self._input_data_uni=[]
    for data in self._input_data:
      self._input_data_uni.append(ord(data))
    self._length=len(self._input_data)
    self._index=0
    _input_file.close()
    return
  
  def readSpace(self):
    if self._input_data_uni[self._index]!=32:
      raise ValueError(f"{self._input_data[self._index]} is not space.")
    self._index+=1
    return
  
  def readEoln(self):
    if self._input_data_uni[self._index]!=10:
      raise ValueError(f"{self._input_data[self._index]} is not Eoln.")
    self._index+=1
    return

  def readEof(self):
    if self._index!=self._length:
      raise ValueError(f"It is not Eof.")
    return

  def readInt(self,lower=None,upper=None):
    res_list=[]
    if self._input_data_uni[self._index]==45:
      res_list.append("-")
      self._index+=1
    while self._input_data_uni[self._index] not in self._space:
      if self._index==self._length:
        raise Exception("There is No data.")
      if 57<self._input_data_uni[self._index] or self._input_data_uni[self._index]<48:
        raise ValueError(f"{self._input_data[self._index]} is not int.")
      res_list.append(self._input_data[self._index])
      self._index+=1
    res_int=int("".join(res_list))
    if lower!=None and lower>res_int:
      raise ValueError(f"{res_int} is less than {lower}.")
    if upper!=None and upper<res_int:
      raise ValueError(f"{res_int} is greater than {upper}.")
    return res_int

  def readFloat(self,lower=None,upper=None):
    res_list=[]
    _cnt=0
    if self._input_data_uni[self._index]==45:
      res_list.append("-")
      self._index+=1
    while self._input_data_uni[self._index] not in self._space:
      if self._index==self._length:
        raise Exception("There is No data.")
      if (57<self._input_data_uni[self._index] or self._input_data_uni[self._index]<48) and self._input_data_uni[self._index]!=46:
        raise ValueError(f"{self._input_data[self._index]} is not int or floating point.")
      if self._input_data_uni[self._index]==46:
        _cnt+=1
        if _cnt>1:
          raise Exception(f"Floating points are 2.")
      res_list.append(self._input_data[self._index])
      self._index+=1
    res_float=float("".join(res_list))
    if lower!=None and lower>res_float:
      raise ValueError(f"{res_int} is less than {lower}.")
    if upper!=None and upper<res_float:
      raise ValueError(f"{res_int} is greater than {upper}.")
    return res_float
  
  def readIntegers(self,lg,lower=None,upper=None):
    res_list=[]
    for _i in range(lg):
      res_list.append(self.readInt(lower,upper))
      if _i!=lg-1:
        self.readSpace()
    return res_list
  
  def readFloats(self,lg,lower=None,upper=None):
    res_list=[]
    for _i in range(lg):
      res_list.append(self.readFloat(lower,upper))
      if _i!=lg-1:
        self.readSpace()
    return res_list

  def readStr_All(self):
    res_list=[]
    while self._input_data_uni[self._index] not in self._space:
      if self._index==self._length:
        raise Exception("There is No data.")
      res_list.append(self._input_data[self._index])
      self._index+=1
    res_str="".join(res_list)
    return res_str

  def readStr(self):
    res_list=[]
    while self._input_data_uni[self._index] not in self._space:
      if self._index==self._length:
        raise Exception("There is No data.")
      if self._input_data_uni[self._index] not in self._char_set:
        raise ValueError(f"{self._input_data[self._index]} is not in char_set.")
      res_list.append(self._input_data[self._index])
      self._index+=1
    res_str="".join(res_list)
    return res_str
  
  def readStr_lowercase(self):
    res_list=[]
    while self._input_data_uni[self._index] not in self._space:
      if self._index==self._length:
        raise Exception("There is No data.")
      if 122<self._input_data_uni[self._index] or self._input_data_uni[self._index]<97:
        raise ValueError(f"{self._input_data[self._index]} is not lowercase.")
      res_list.append(self._input_data[self._index])
      self._index+=1
    res_str="".join(res_list)
    return res_str

  def readStr_uppercase(self):
    res_list=[]
    while self._input_data_uni[self._index] not in self._space:
      if self._index==self._length:
        raise Exception("There is No data.")
      if 90<self._input_data_uni[self._index] or self._input_data_uni[self._index]<65:
        raise ValueError(f"{self._input_data[self._index]} is not uppercase.")
      res_list.append(self._input_data[self._index])
      self._index+=1
    res_str="".join(res_list)
    return res_str

  def readStr_alphabets(self):
    res_list=[]
    while self._input_data_uni[self._index] not in self._space:
      if self._index==self._length:
        raise Exception("There is No data.")
      if (90<self._input_data_uni[self._index] or self._input_data_uni[self._index]<65) and (122<self._input_data_uni[self._index] or self._input_data_uni[self._index]<97):
        raise ValueError(f"{self._input_data[self._index]} is not uppercase.")
      res_list.append(self._input_data[self._index])
      self._index+=1
    res_str="".join(res_list)
    return res_str
  
  def readStr_Integer(self):
    res_list=[]
    while self._input_data_uni[self._index] not in self._space:
      if self._index==self._length:
        raise Exception("There is No data.")
      if 57<self._input_data_uni[self._index] or self._input_data_uni[self._index]<48:
        raise ValueError(f"{self._input_data[self._index]} is not uppercase.")
      res_list.append(self._input_data[self._index])
      self._index+=1
    res_str="".join(res_list)
    return res_str

  def readStrings(self,lg,func):
    res_list=[]
    for _i in range(lg):
      res_list.append(func())
      if _i!=lg-1:
        self.readSpace()
    return res_list

  def set_CharList(self,chr_list):
    for char in chr_list:
      if len(str(char))!=1:
        raise Exception(f"char's length must be 1.")
      self._char_set.add(ord(str(char)))
    return

