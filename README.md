# Leprechaun Catcher Python Code #
A python script to operate a leprechaun catcher using an ST VL6180X time-of-flight ranging sensor, and an RC servo on Raspberry Pi.

Check out the project page on Hackaday.io ([https://hackaday.io/project/10072-leprechaun-catcher](https://hackaday.io/project/10072-leprechaun-catcher))

* Make sure you have i2c enabled and python-rpi.gpio installed on your raspberry pi.
* Copy my ST VL6180X library ([https://bitbucket.org/310weber/st_vl6180x](https://bitbucket.org/310weber/st_vl6180x)) into ./lib/ folder


Written by Arnie Weber.  BSD license, all text above and below must be included in any redistribution

Copyright (c) 2015 Arnie Weber.  All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. * Neither the name of the nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.