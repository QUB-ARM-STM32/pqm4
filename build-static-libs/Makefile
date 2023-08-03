all: clean
	make -f ./kyber.mk SCHEME_NAME=kyber512 TYPE=m4fspeed -s
	make -f ./kyber.mk SCHEME_NAME=kyber512 TYPE=m4fstack -s
	make -f ./kyber.mk SCHEME_NAME=kyber768 TYPE=m4fspeed -s
	make -f ./kyber.mk SCHEME_NAME=kyber768 TYPE=m4fstack -s
	make -f ./kyber.mk SCHEME_NAME=kyber1024 TYPE=m4fspeed -s
	make -f ./kyber.mk SCHEME_NAME=kyber1024 TYPE=m4fstack -s
	make -f ./kyber.mk SCHEME_NAME=kyber512-90s TYPE=m4fspeed -s
	make -f ./kyber.mk SCHEME_NAME=kyber512-90s TYPE=m4fstack -s
	make -f ./kyber.mk SCHEME_NAME=kyber768-90s TYPE=m4fspeed -s
	make -f ./kyber.mk SCHEME_NAME=kyber768-90s TYPE=m4fstack -s
	make -f ./kyber.mk SCHEME_NAME=kyber1024-90s TYPE=m4fspeed -s
	make -f ./kyber.mk SCHEME_NAME=kyber1024-90s TYPE=m4fstack -s
	
	make -f ./dilithium.mk SCHEME_NAME=dilithium2
	make -f ./dilithium.mk SCHEME_NAME=dilithium3
	make -f ./dilithium.mk SCHEME_NAME=dilithium5

clean:
	rm -f *.o *.a
	rm -fr ./libs