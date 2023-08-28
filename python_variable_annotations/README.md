# Python Type Annotations and Validation

This repository focuses on the use of type annotations in Python 3, understanding duck typing, and validating code with tools like `mypy`.

## What I've Learned:

- **Type Annotations in Python 3:**
  - I've gained an understanding of how to annotate variables and functions in Python 3 to explicitly specify the expected type of data they should handle.

- **Function Signatures & Variable Types:**
  - I've learned to use type annotations to clearly define the types of arguments a function should accept and the type of data it should return. This enhances code readability and provides clearer documentation.

- **Duck Typing:**
  - I've become familiar with the concept of "duck typing", which is a feature of dynamically-typed languages like Python. It emphasizes an object's behavior over its class or type, meaning that the methods and properties an object possesses are more important than its actual type.

- **Validating Code with Mypy:**
  - I've acquired skills in using `mypy`, a static type checker for Python. This tool helps detect potential type inconsistencies in the code, thus enhancing code quality by catching type errors before runtime.

## Tasks

### 0. Basic annotations - add

- **Filename:** `0-add.py`

- **Description:**
  Write a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float.

---

### 1. Basic annotations - concat

- **Filename:** `1-concat.py`

- **Description:**
  Write a type-annotated function `concat` that takes a string `str1` and a string `str2` as arguments and returns a concatenated string.

---

### 2. Basic annotations - floor

- **Filename:** `2-floor.py`

- **Description:**
  Write a type-annotated function `floor` which takes a float `n` as an argument and returns the floor of the float.

---

### 3. Basic annotations - to string

- **Filename:** `3-to_str.py`

- **Description:**
  Write a type-annotated function `to_str` that takes a float `n` as an argument and returns the string representation of the float.

---

### 4. Define variables

- **Filename:** `4-define_variables.py`

- **Description:**
  Define and annotate the following variables with the specified values:
  - `a`, an integer with a value of 1
  - `pi`, a float with a value of 3.14
  - `i_understand_annotations`, a boolean with a value of True
  - `school`, a string with a value of “Holberton”

---

### 5. Complex types - list of floats

- **Filename:** `5-sum_list.py`

- **Description:**
  Write a type-annotated function `sum_list` which takes a list `input_list` of floats as an argument and returns their sum as a float.

---

### 6. Complex types - mixed list

- **Filename:** `6-sum_mixed_list.py`

- **Description:**
  Write a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float.

---

### 7. Complex types - string and int/float to tuple

- **Filename:** `7-to_kv.py`

- **Description:**
  Write a type-annotated function `to_kv` that takes a string `k` and an int OR float `v` as arguments and returns a tuple. The first element of the tuple is the string `k`. The second element is the square of the int/float `v` and should be annotated as a float.

---

### 8. Complex types - functions

- **Filename:** `8-make_multiplier.py`

- **Description:**
  Write a type-annotated function `make_multiplier` that takes a float `multiplier` as argument and returns a function that multiplies a float by `multiplier`.

---

### 9. Let's duck type an iterable object

- **Filename:** `9-element_length.py`

- **Description:**
  Annotate the below function’s parameters and return values with the appropriate types. The function is defined as:

  ```python
  def element_length(lst):
      return [(i, len(i)) for i in lst]
