SCHEME_NAME ?= dilithium2
TYPE ?= m4f

SRC_FILES := $(wildcard ../mupq/common/*.c) $(wildcard ../crypto_sign/$(SCHEME_NAME)/$(TYPE)/*.c) $(wildcard ../crypto_sign/$(SCHEME_NAME)/$(TYPE)/*.S) \
$(wildcard ../crypto_sign/$(SCHEME_NAME)/$(TYPE)/*.s) $(wildcard ../common/*.c) $(wildcard ../common/*.S) $(wildcard ../common/*.s)
SRC_FILES := $(filter-out ../common/hal-mps2.c, $(SRC_FILES))
SRC_FILES := $(filter-out ../common/hal-opencm3.c, $(SRC_FILES))
SRC_FILES := $(filter-out ../common/test.c, $(SRC_FILES))
SRC_FILES := $(filter-out ../common/aestest.c, $(SRC_FILES))
SRC_FILES := $(filter-out ../common/mps2/*, $(SRC_FILES))
SRC_FILES := $(filter-out ../common/randombytes.c, $(SRC_FILES))

INC_FILES := ../common/ ../mupq/common/ ../crypto_kem/$(SCHEME_NAME)/$(TYPE)/
CC := arm-none-eabi-gcc

MPU := -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb

LIB_NAME := lib$(SCHEME_NAME)_$(TYPE).a

all: build
	mkdir -p ./libs
	ar -rc ./libs/$(LIB_NAME) *.o
	ranlib ./libs/$(LIB_NAME)
	rm -f *.o
	

build: clean
	if [ -d "../crypto_sign/$(SCHEME_NAME)/$(TYPE)" ]; then \
		echo "Building $(SCHEME_NAME)_$(TYPE)"; \
		$(CC) -c $(SRC_FILES) -I./common/ -I../mupq/common/ -I../crypto_sign/$(SCHEME_NAME)/$(TYPE)/ $(MPU); \
	else \
		echo "Invalid scheme name $(SCHEME_NAME) or type $(TYPE)"; \
		exit 1; \
	fi

clean:
	rm -f *.o *.a