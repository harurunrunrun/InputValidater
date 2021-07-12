# InputValidater

Validate the input in Python.

- ## Caution
  - I am not responsible for any damage you may suffer from using this code.
  - I have tested it, but it may contain bugs.
  - It is very slow because it is reading one character at a time (So you may excute in PyPy3).

- ## How to use

    If you run python scripts, you have to excute it with a command like following.

    `py hoge.py < hoge.txt`

    (`hoge.py` is script file, `hoge.txt` is input file)

  - ### initialization
      
      If you use at online judege, you have to paste `InputValidater class` on your code.

      If you use at local, you can do `import InputValidater`.(InputValidater.py must be in the same folder that contains your script.)

      You do following ones. More than onece is undefined.

      `inf=InputValidater()`

  - ### read integer
      In the following, `lower` represents the lower limit and `upper` represents the upper limit, which you may or may not set. The default is `None`.

      - read one integer
      
        `inf.readInt(lower,upper)`
      
      - read integers as list
        
        `inf.readIntegers(length,lower,upper)`
        
        length means list length.
      
  - ### read float
      - read one float
        
        `inf.readFloat(lower,upper)`

      - read floats as list
        
        `inf.readFloats(length,lower,upper)`

  - ### read string
      - read one string (No character limit)
        
        `inf.readStr_All()`
      
      - read one string (lowercase letter)

        `inf.readStr_lowercase()`

      - read one string (uppercase letter)

        `inf.readStr_uppercase()`
      
      - read one string (alphabets)

        `inf.readStr_alphabets()`
      
      - read one string (Integer)

        `inf.readStr_Integer()`

      - read one string (limited)
      
        Add the ones in chr_list to the limit.

        `inf.set_CharList(chr_list)`

        The input will be based on the restrictions added above.

        `inf.readStr()`

      - read strings as list

        Provide input based on the `func` function

        `inf.readStrings(length,func)`
        
        example:
          
          `inf.readStrings(length,inf.readStr_All)`
  
  - ### other
      - read one space

        `inf.readSpace()`
      
      - read one End of line
        
        `inf.readEoln()`

      - read end of file
        
        `inf.readEof()`
        
