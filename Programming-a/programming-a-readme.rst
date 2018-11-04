Homework 3 Programming a
========================

This program implements Blum-Goldwasser Probabilistic Encryption Algorithm with parameters
p=499, q=547, a=-57, b=52, X0 =159201 and message m=10011100000100001100.

Code Path
---------

[Programming-a](Programming-a)

Encryption
----------

Ciphertext is
:code:`[50, 0, 44, 46, 52, 40632]`

Decryption
----------

Decrypt Ciphertext and get
:code:`10011100000100001100`

In the code, I don't use the given a and b. Instead, I use a = p^-1 mod q and b = q^-1 mod p.

Code Description
----------------

* *BG_demo.py* is the main program. Run it using *Python 3*.
* *Blum_Goldwessar_Class.py* defines class BG which is used for both encryption and decryption.
* *Number_Package.py* contains useful functions related to number manipulation such as multiplicative inverse, exponential with modulo.

How to run
----------

:code:`python3 BG_demo.py`

and the expected output is

.. code-block:: bash

  Ciphertext is
  [50, 0, 44, 46, 52, 40632]
  Decryption result
  10011100000100001100
  Decryption success
