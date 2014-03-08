This project suppose to be library for one of extension of Json.

Author is yassu on gitHub.

---

* Define Data Structure
* Append Data Structure
* Using comment 

---

## Define Data Struncture

Data Structure of Yson is String, Number, Bool, List and Object.
But we will find to how to append new Data Structure.

### String

Regrex of String is `"[^"]"`.
Note that this is not extension of Json.
For example, "123\"456" can not be parsed as String Data Structure.

### Number

Regrex of Number is `(+|-)?[0-9]+(\.[0-9]*)?`.
Note that this is not extension of Json.
For example, 123e4 can not be parsed as Number Data Structure.

### Bool

Regrex of Bool is `(True|False)`.

### None

Regrex of None is `(None|null)`.

### List

Regrex of Number is `\[(obj,)*\]`, where obj is other data structure.
Note that this format is extension of Json.
For example, `[True,[1,2,3],]` is parsed as `[True,[1,2,3]]` for python.

### Object

Regrex of Object is `\{(key_obj,*:value_obj,)*\}`, where `key_obj` or `value_obj` is other data structure.
Note that this format is extension of Json.
For example, 

    {
        1: [1,2,3],
    }

is parsed as `{1:[1,2,3]}`.

## Using Comment

Comment is very useful however this is not defined in Json.

In Yson, Comment is defined by user.

Comment is regrex.

How to write is `yson.load(f, reg)`.
