CSCI6230-HW03
^^^^^^^^^^^^^

Homework 3 Programming a
========================

This program implements Blum-Goldwasser Probabilistic Encryption Algorithm with parameters
p=499, q=547, a=-57, b=52, X0 =159201 and message m=10011100000100001100.

Code Path
---------

[Programming-a](Programming-a)

Key Generation (Alice)
----------------------
Alice
* chooses a Blum integer :math:`n` such that :math:`n=p \cdot q` and :math:`p \equiv 3~mod~4, q \equiv 3~mod~4`.
* computes two integers :math:`a` and :math:`b` using Euler-Extended Algorithm such that :math:`ap + bq = 1`

public key is :math:`n`
private keys are :math:`p,q,a,b`

In this homework,

.. math::

	n = 159201, p = 499, q = 547, a = -57, b = 52

Encryption (Bob)
----------------
Bob chooses a random number :math:`x_0 \in QR_n`.
Compute

.. math::
    k = \lfloor log n \rfloor\\
    h = \lfloor log k \rfloor

The message is divided into :math:`t` blocks such that each block is of :math:`h` bits.

In this homework, :math:`k=18, h=4, t=5`

Then follow the encryption rule of BG, we will have the ciphertext:
:code:`[50, 0, 44, 46, 52, 40632]`.

:code:`50, 0, 44, 46, 52` are :math:`c_1, c_2, c_3, c_4, c_5`

:code:`40632` is :math:`X_{t+1}`.


Decryption (Alice)
------------------

.. math::
  &d_1 = [(p+1)/4]^{t+1} ~mod~p-1\\
  &d_2 = [(q+1)/4]^{t+1} ~mod~q-1\\\\
  &u = X_{t+1}^d_1 ~mod~p \\
  &v = X_{t+1}^d_2 ~mod~q\\
  &X_0 = vap + ubq~mod~N

Follow the above steps to compute :math:`X_0`, we then can decode the ciphertext and get
:code:`10011100000100001100`

In the code, I don't use the given a and b. Instead, I use

.. math::
	a = p^{-1}~mod~q\\
  b = q^{-1}~mod~p.

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
