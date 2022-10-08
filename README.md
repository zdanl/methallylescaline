methallylescaline
================

* methallylescaline is playing with bits and strings.
* it is pure security by obscurity unless you find a good RNG / entropy source
* it is a polymorphic encryption library
* it has a benchmarking and profiling library
* you can compile it to web assembly

* methallylescaline is a framework that supports polymorphic crypto,
  test it, benchmark it and use it in numerous environments including
  webassembly. this is meant for binary

* there are three basic crypto libraries shipped: 

    - *dihydrobenzofuran* is used for strings only. it is a horrible drug, and
      you should never use it. it is dangerous. you can compare it to rot13
      on anabolic steroids and 1,3-dimethylamylamine. it can shift ASCII codes
      of Unicode from 0 - 127 and adding 32 (or flipping the sixth bit) will 
      play with uppercase to lowercase. it will go to hex and base64, and perform
      the same operation again. decoding is simple if you know the algorithm.
      methallylescaline allows you to easily write analouges and homolouges of 
      dihydrobenzofuran so they have to break your crypto again.

    - *phenylethylamin* is meant for block ciphers in general. it operates on
      bits with XOR ^ and bitwise complement ~. this is actually quite strong
      for text messages and files, or anything binary.

    - *tryptamin* is meant for stream ciphers. it operates on bytes by basic 
      arithmetic operations. this is weak. there is not enough knowledge about
      block ciphers yet.

    - *isopropylphenidate* is a null encryption. it does precisely nothing and
      is used for testing. this corresponds to the potency of isopropyl- in
      binding to neural receptors and producing exactly zero prefrontal cortex
      stimulation.

