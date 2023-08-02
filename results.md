# Speed Evaluation
## Key Encapsulation Schemes
| scheme | implementation | key generation [cycles] | encapsulation [cycles] | decapsulation [cycles] |
| ------ | -------------- | ----------------------- | ---------------------- | ---------------------- |
| kyber1024 (21 executions) | clean | AVG: 1,688,246 <br /> MIN: 1,685,804 <br /> MAX: 1,700,453 | AVG: 2,061,820 <br /> MIN: 2,059,388 <br /> MAX: 2,074,049 | AVG: 2,179,696 <br /> MIN: 2,177,264 <br /> MAX: 2,191,925 |
| kyber1024 (21 executions) | m4fspeed | AVG: 1,195,804 <br /> MIN: 1,194,357 <br /> MAX: 1,209,296 | AVG: 1,400,558 <br /> MIN: 1,399,094 <br /> MAX: 1,414,045 | AVG: 1,286,778 <br /> MIN: 1,285,313 <br /> MAX: 1,300,265 |
| kyber1024 (21 executions) | m4fstack | AVG: 1,199,138 <br /> MIN: 1,196,927 <br /> MAX: 1,212,065 | AVG: 1,409,256 <br /> MIN: 1,407,045 <br /> MAX: 1,422,185 | AVG: 1,296,232 <br /> MIN: 1,294,020 <br /> MAX: 1,309,160 |
| kyber1024-90s (21 executions) | clean | AVG: 3,133,196 <br /> MIN: 3,132,530 <br /> MAX: 3,133,693 | AVG: 3,398,891 <br /> MIN: 3,398,258 <br /> MAX: 3,399,408 | AVG: 3,622,071 <br /> MIN: 3,621,438 <br /> MAX: 3,622,588 |
| kyber1024-90s (21 executions) | m4fspeed | AVG: 1,040,419 <br /> MIN: 1,032,699 <br /> MAX: 1,042,835 | AVG: 1,139,439 <br /> MIN: 1,131,732 <br /> MAX: 1,141,885 | AVG: 1,130,968 <br /> MIN: 1,123,261 <br /> MAX: 1,133,414 |
| kyber1024-90s (21 executions) | m4fstack | AVG: 1,047,044 <br /> MIN: 1,042,619 <br /> MAX: 1,052,226 | AVG: 1,151,389 <br /> MIN: 1,146,986 <br /> MAX: 1,156,358 | AVG: 1,143,699 <br /> MIN: 1,139,296 <br /> MAX: 1,148,669 |
| kyber512 (22 executions) | clean | AVG: 650,919 <br /> MIN: 650,558 <br /> MAX: 651,511 | AVG: 862,945 <br /> MIN: 862,595 <br /> MAX: 863,548 | AVG: 946,386 <br /> MIN: 946,036 <br /> MAX: 946,989 |
| kyber512 (22 executions) | m4fspeed | AVG: 463,400 <br /> MIN: 462,296 <br /> MAX: 476,738 | AVG: 565,418 <br /> MIN: 564,335 <br /> MAX: 578,539 | AVG: 507,213 <br /> MIN: 506,130 <br /> MAX: 520,333 |
| kyber512 (22 executions) | m4fstack | AVG: 462,254 <br /> MIN: 461,795 <br /> MAX: 462,852 | AVG: 566,478 <br /> MIN: 566,019 <br /> MAX: 567,075 | AVG: 508,327 <br /> MIN: 507,868 <br /> MAX: 508,924 |
| kyber512-90s (21 executions) | clean | AVG: 982,075 <br /> MIN: 981,588 <br /> MAX: 982,391 | AVG: 1,147,251 <br /> MIN: 1,146,775 <br /> MAX: 1,147,578 | AVG: 1,287,273 <br /> MIN: 1,286,797 <br /> MAX: 1,287,600 |
| kyber512-90s (21 executions) | m4fspeed | AVG: 394,095 <br /> MIN: 390,223 <br /> MAX: 394,754 | AVG: 449,318 <br /> MIN: 445,455 <br /> MAX: 449,936 | AVG: 447,692 <br /> MIN: 443,829 <br /> MAX: 448,310 |
| kyber512-90s (21 executions) | m4fstack | AVG: 394,749 <br /> MIN: 394,402 <br /> MAX: 395,074 | AVG: 452,138 <br /> MIN: 451,792 <br /> MAX: 452,486 | AVG: 450,573 <br /> MIN: 450,226 <br /> MAX: 450,920 |
| kyber768 (21 executions) | clean | AVG: 1,079,451 <br /> MIN: 1,079,060 <br /> MAX: 1,079,816 | AVG: 1,384,659 <br /> MIN: 1,384,292 <br /> MAX: 1,385,047 | AVG: 1,485,118 <br /> MIN: 1,484,751 <br /> MAX: 1,485,506 |
| kyber768 (21 executions) | m4fspeed | AVG: 752,131 <br /> MIN: 750,248 <br /> MAX: 765,268 | AVG: 919,029 <br /> MIN: 917,173 <br /> MAX: 932,157 | AVG: 832,667 <br /> MIN: 830,811 <br /> MAX: 845,797 |
| kyber768 (21 executions) | m4fstack | AVG: 752,518 <br /> MIN: 751,512 <br /> MAX: 765,846 | AVG: 923,208 <br /> MIN: 922,202 <br /> MAX: 936,535 | AVG: 837,313 <br /> MIN: 836,308 <br /> MAX: 850,640 |
| kyber768-90s (21 executions) | clean | AVG: 1,884,927 <br /> MIN: 1,884,498 <br /> MAX: 1,885,327 | AVG: 2,106,701 <br /> MIN: 2,106,272 <br /> MAX: 2,107,100 | AVG: 2,288,105 <br /> MIN: 2,287,676 <br /> MAX: 2,288,504 |
| kyber768-90s (21 executions) | m4fspeed | AVG: 656,619 <br /> MIN: 652,615 <br /> MAX: 657,811 | AVG: 740,131 <br /> MIN: 736,118 <br /> MAX: 741,327 | AVG: 734,711 <br /> MIN: 730,698 <br /> MAX: 735,907 |
| kyber768-90s (21 executions) | m4fstack | AVG: 659,103 <br /> MIN: 645,752 <br /> MAX: 660,567 | AVG: 746,389 <br /> MIN: 733,035 <br /> MAX: 747,856 | AVG: 741,442 <br /> MIN: 728,087 <br /> MAX: 742,908 |
## Signature Schemes
| scheme | implementation | key generation [cycles] | sign [cycles] | verify [cycles] |
| ------ | -------------- | ----------------------- | ------------- | --------------- |
| dilithium2 (18 executions) | clean | AVG: 2,115,413 <br /> MIN: 2,073,336 <br /> MAX: 2,140,998 | AVG: 8,337,988 <br /> MIN: 3,492,900 <br /> MAX: 17,077,964 | AVG: 2,271,780 <br /> MIN: 2,271,483 <br /> MAX: 2,272,195 |
| dilithium2 (18 executions) | m4f | AVG: 1,709,572 <br /> MIN: 1,688,304 <br /> MAX: 1,742,791 | AVG: 3,421,752 <br /> MIN: 2,112,259 <br /> MAX: 6,986,416 | AVG: 1,683,998 <br /> MIN: 1,683,458 <br /> MAX: 1,684,341 |
| dilithium2aes (5 executions) | clean | AVG: 5,429,252 <br /> MIN: 5,397,464 <br /> MAX: 5,468,391 | AVG: 10,830,989 <br /> MIN: 6,769,051 <br /> MAX: 18,102,895 | AVG: 5,096,324 <br /> MIN: 5,064,249 <br /> MAX: 5,135,539 |
| dilithium3 (5 executions) | clean | AVG: 3,662,345 <br /> MIN: 3,661,657 <br /> MAX: 3,662,821 | AVG: 13,924,251 <br /> MIN: 7,430,041 <br /> MAX: 20,742,764 | AVG: 3,762,232 <br /> MIN: 3,762,052 <br /> MAX: 3,762,345 |
| dilithium3 (5 executions) | m4f | AVG: 3,026,450 <br /> MIN: 3,025,954 <br /> MAX: 3,027,180 | AVG: 6,425,848 <br /> MIN: 3,439,912 <br /> MAX: 9,466,811 | AVG: 2,879,572 <br /> MIN: 2,879,505 <br /> MAX: 2,879,684 |
| dilithium3aes (5 executions) | clean | AVG: 9,759,024 <br /> MIN: 9,716,185 <br /> MAX: 9,805,261 | AVG: 26,331,534 <br /> MIN: 11,457,577 <br /> MAX: 43,929,252 | AVG: 9,060,551 <br /> MIN: 9,017,589 <br /> MAX: 9,106,685 |
| dilithium5 (5 executions) | clean | AVG: 6,135,466 <br /> MIN: 6,121,834 <br /> MAX: 6,149,019 | AVG: 12,374,764 <br /> MIN: 8,587,017 <br /> MAX: 15,683,480 | AVG: 6,327,876 <br /> MIN: 6,327,587 <br /> MAX: 6,328,131 |
| dilithium5 (5 executions) | m4f | AVG: 5,155,956 <br /> MIN: 5,136,883 <br /> MAX: 5,177,662 | AVG: 7,457,219 <br /> MIN: 5,767,849 <br /> MAX: 10,794,816 | AVG: 5,022,350 <br /> MIN: 5,022,240 <br /> MAX: 5,022,487 |
| falcon-1024 (2 executions) | clean | AVG: 530,920,887 <br /> MIN: 523,774,463 <br /> MAX: 538,067,311 | AVG: 137,427,761 <br /> MIN: 137,386,217 <br /> MAX: 137,469,306 | AVG: 1,636,737 <br /> MIN: 1,636,335 <br /> MAX: 1,637,139 |
| falcon-1024 (2 executions) | m4-ct | AVG: 355,656,491 <br /> MIN: 314,612,070 <br /> MAX: 396,700,912 | AVG: 87,473,642 <br /> MIN: 87,401,571 <br /> MAX: 87,545,713 | AVG: 1,023,430 <br /> MIN: 1,023,299 <br /> MAX: 1,023,562 |
| falcon-1024 (2 executions) | opt-ct | AVG: 321,762,187 <br /> MIN: 314,615,308 <br /> MAX: 328,909,067 | AVG: 87,523,935 <br /> MIN: 87,509,173 <br /> MAX: 87,538,698 | AVG: 1,024,798 <br /> MIN: 1,024,414 <br /> MAX: 1,025,183 |
| falcon-1024 (2 executions) | opt-leaktime | AVG: 311,441,344 <br /> MIN: 258,667,421 <br /> MAX: 364,215,267 | AVG: 78,450,941 <br /> MIN: 78,266,235 <br /> MAX: 78,635,648 | AVG: 1,016,726 <br /> MIN: 1,008,626 <br /> MAX: 1,024,827 |
| falcon-512 (7 executions) | clean | AVG: 228,564,297 <br /> MIN: 164,919,652 <br /> MAX: 411,598,962 | AVG: 62,748,251 <br /> MIN: 62,605,076 <br /> MAX: 62,864,784 | AVG: 820,612 <br /> MIN: 820,375 <br /> MAX: 820,920 |
| falcon-512 (7 executions) | m4-ct | AVG: 180,461,589 <br /> MIN: 116,624,528 <br /> MAX: 320,936,719 | AVG: 40,092,772 <br /> MIN: 39,947,375 <br /> MAX: 40,232,572 | AVG: 488,029 <br /> MIN: 484,992 <br /> MAX: 500,834 |
| falcon-512 (7 executions) | opt-ct | AVG: 209,220,179 <br /> MIN: 116,624,528 <br /> MAX: 355,851,711 | AVG: 40,087,743 <br /> MIN: 40,038,118 <br /> MAX: 40,119,944 | AVG: 497,850 <br /> MIN: 485,992 <br /> MAX: 500,398 |
| falcon-512 (7 executions) | opt-leaktime | AVG: 105,013,637 <br /> MIN: 95,092,729 <br /> MAX: 132,290,633 | AVG: 36,614,303 <br /> MIN: 36,436,888 <br /> MAX: 36,885,345 | AVG: 495,760 <br /> MIN: 485,725 <br /> MAX: 500,507 |
| falcon-512-tree (10 executions) | m4-ct | AVG: 147,562,852 <br /> MIN: 122,768,510 <br /> MAX: 205,077,718 | AVG: 18,223,219 <br /> MIN: 18,109,213 <br /> MAX: 18,331,322 | AVG: 496,174 <br /> MIN: 485,784 <br /> MAX: 501,669 |
| falcon-512-tree (10 executions) | opt-ct | AVG: 185,440,687 <br /> MIN: 142,951,886 <br /> MAX: 243,555,818 | AVG: 18,239,218 <br /> MIN: 18,097,193 <br /> MAX: 18,357,344 | AVG: 492,183 <br /> MIN: 485,727 <br /> MAX: 501,891 |
| falcon-512-tree (10 executions) | opt-leaktime | AVG: 216,719,519 <br /> MIN: 111,764,241 <br /> MAX: 361,463,581 | AVG: 19,916,516 <br /> MIN: 19,722,789 <br /> MAX: 20,148,110 | AVG: 493,140 <br /> MIN: 484,381 <br /> MAX: 502,501 |
# Memory Evaluation
## Key Encapsulation Schemes
| Scheme | Implementation | Key Generation [bytes] | Encapsulation [bytes] | Decapsulation [bytes] |
| ------ | -------------- | ---------------------- | --------------------- | --------------------- |
| bikel1 | m4f | 44,068 | 32,116 | 91,368 |
| bikel1 | opt | 35,928 | 25,876 | 78,556 |
| bikel3 | m4f | 85,828 | 62,852 | 161,804 |
| bikel3 | opt | 69,632 | 50,564 | 155,376 |
| hqc-rmrs-128 | clean | 48,936 | 64,412 | 71,148 |
| hqc-rmrs-192 | clean | 96,828 | 128,348 | 141,900 |
| hqc-rmrs-256 | clean | 154,228 | 204,820 | 226,540 |
| kyber1024 | clean | 15,076 | 18,748 | 20,324 |
| kyber1024 | m4fspeed | 6,376 | 7,472 | 7,488 |
| kyber1024 | m4fstack | 3,272 | 3,344 | 3,368 |
| kyber1024-90s | clean | 15,340 | 19,020 | 20,596 |
| kyber1024-90s | m4fspeed | 7,124 | 8,220 | 8,236 |
| kyber1024-90s | m4fstack | 4,028 | 4,100 | 4,124 |
| kyber512 | clean | 6,108 | 8,772 | 9,548 |
| kyber512 | m4fspeed | 4,304 | 5,408 | 5,416 |
| kyber512 | m4fstack | 2,232 | 2,320 | 2,336 |
| kyber512-90s | clean | 6,548 | 9,212 | 9,988 |
| kyber512-90s | m4fspeed | 5,052 | 6,156 | 6,164 |
| kyber512-90s | m4fstack | 2,988 | 3,076 | 3,092 |
| kyber768 | clean | 10,204 | 13,372 | 14,468 |
| kyber768 | m4fspeed | 5,328 | 6,440 | 6,456 |
| kyber768 | m4fstack | 2,768 | 2,840 | 2,856 |
| kyber768-90s | clean | 10,760 | 13,820 | 14,916 |
| kyber768-90s | m4fspeed | 6,084 | 7,196 | 7,212 |
| kyber768-90s | m4fstack | 3,516 | 3,588 | 3,604 |
## Signature Schemes
| Scheme | Implementation | Key Generation [bytes] | Sign [bytes] | Verify [bytes] |
| ------ | -------------- | ---------------------- | ------------ | -------------- |
| dilithium2 | clean | 38,392 | 52,016 | 36,304 |
| dilithium2 | m4f | 38,384 | 49,464 | 36,296 |
| dilithium2aes | clean | 39,748 | 53,372 | 37,660 |
| dilithium3 | clean | 60,920 | 79,664 | 57,700 |
| dilithium3 | m4f | 60,912 | 68,912 | 57,800 |
| dilithium3aes | clean | 62,276 | 81,020 | 59,164 |
| dilithium5 | clean | 97,784 | 122,672 | 92,880 |
| dilithium5 | m4f | 97,776 | 116,016 | 92,872 |
| falcon-1024 | clean | 36,304 | 82,420 | 8,796 |
| falcon-1024 | m4-ct | 1,472 | 2,560 | 388 |
| falcon-1024 | opt-ct | 1,488 | 2,560 | 388 |
| falcon-1024 | opt-leaktime | 1,480 | 2,656 | 388 |
| falcon-1024-tree | opt-ct | 1,416 | 2,920 | 388 |
| falcon-1024-tree | opt-leaktime | 1,400 | 2,936 | 388 |
| falcon-512 | clean | 18,360 | 42,396 | 4,700 |
| falcon-512 | m4-ct | 1,488 | 2,472 | 388 |
| falcon-512 | opt-ct | 1,488 | 2,472 | 388 |
| falcon-512 | opt-leaktime | 1,440 | 2,672 | 388 |
| falcon-512-tree | m4-ct | 1,480 | 2,768 | 388 |
| falcon-512-tree | opt-ct | 1,480 | 2,768 | 388 |
| falcon-512-tree | opt-leaktime | 1,488 | 2,896 | 388 |
| sphincs-haraka-128f-robust | clean | 3,620 | 3,712 | 4,172 |
| sphincs-haraka-128s-simple | clean | 3,856 | 3,896 | 3,468 |
| sphincs-haraka-192f-robust | clean | 5,064 | 5,104 | 5,396 |
| sphincs-haraka-256f-robust | clean | 7,028 | 7,104 | 7,004 |
| sphincs-haraka-256f-simple | clean | 7,020 | 7,016 | 6,996 |
| sphincs-haraka-256s-simple | clean | 7,400 | 7,240 | 6,588 |
| sphincs-sha256-128f-simple | clean | 2,104 | 2,168 | 2,656 |
| sphincs-sha256-192s-robust | clean | 4,103 | 3,992 | 3,376 |
| sphincs-sha256-256f-robust | clean | 5,792 | 5,760 | 5,656 |
| sphincs-sha256-256f-simple | clean | 5,512 | 5,480 | 5,488 |
| sphincs-shake256-128f-robust | clean | 2,012 | 2,176 | 2,556 |
| sphincs-shake256-128s-robust | clean | 2,336 | 2,288 | 1,860 |
| sphincs-shake256-192f-simple | clean | 3,436 | 3,576 | 3,788 |
| sphincs-shake256-192s-robust | clean | 3,748 | 3,736 | 3,124 |
| sphincs-shake256-192s-simple | clean | 3,856 | 3,736 | 3,232 |
| sphincs-shake256-256s-robust | clean | 5,816 | 5,648 | 5,104 |
| sphincs-shake256-256s-simple | clean | 5,816 | 5,648 | 4,996 |
# Hashing Evaluation
## Key Encapsulation Schemes
| Scheme | Implementation | Key Generation [%] | Encapsulation [%] | Decapsulation [%] |
| ------ | -------------- | ------------------ | ----------------- | ----------------- |
| kyber1024 | clean | 56.5% | 56.1% | 45.0% |
| kyber1024 | m4fspeed | 79.5% | 82.4% | 76.1% |
| kyber1024 | m4fstack | 79.3% | 82.0% | 75.6% |
| kyber1024-90s | clean | 75.2% | 72.3% | 66.0% |
| kyber1024-90s | m4fspeed | 70.9% | 73.2% | 67.8% |
| kyber1024-90s | m4fstack | 70.5% | 72.6% | 67.2% |
| kyber512 | clean | 56.8% | 54.1% | 39.3% |
| kyber512 | m4fspeed | 79.7% | 82.5% | 73.2% |
| kyber512 | m4fstack | 79.8% | 82.2% | 73.0% |
| kyber512-90s | clean | 70.4% | 64.7% | 54.8% |
| kyber512-90s | m4fspeed | 72.4% | 74.6% | 66.5% |
| kyber512-90s | m4fstack | 72.3% | 74.2% | 66.2% |
| kyber768 | clean | 55.0% | 54.6% | 41.8% |
| kyber768 | m4fspeed | 78.9% | 82.2% | 74.5% |
| kyber768 | m4fstack | 78.8% | 81.8% | 74.1% |
| kyber768-90s | clean | 73.0% | 69.2% | 61.4% |
| kyber768-90s | m4fspeed | 70.9% | 73.5% | 66.9% |
| kyber768-90s | m4fstack | 70.6% | 72.9% | 66.3% |
## Signature Schemes
| Scheme | Implementation | Key Generation [%] | Sign [%] | Verify [%] |
| ------ | -------------- | ------------------ | -------- | ---------- |
| dilithium2 | clean | 67.0% | 37.4% | 59.7% |
| dilithium2 | m4f | 83.1% | 64.9% | 80.4% |
| dilithium2aes | clean | 2.7% | 3.2% | 5.1% |
| dilithium3 | clean | 70.4% | 39.6% | 63.3% |
| dilithium3 | m4f | 85.1% | 63.9% | 82.6% |
| dilithium3aes | clean | 2.2% | 2.3% | 3.6% |
| dilithium5 | clean | 72.4% | 42.4% | 67.3% |
| dilithium5 | m4f | 86.2% | 70.8% | 84.7% |
| falcon-1024 | clean | 9.6% | 0.4% | 27.0% |
| falcon-1024 | m4-ct | 12.9% | 0.5% | 35.4% |
| falcon-1024 | opt-ct | 20.8% | 0.5% | 35.5% |
| falcon-1024 | opt-leaktime | 5.6% | 0.5% | 35.5% |
| falcon-512 | clean | 17.5% | 0.4% | 29.4% |
| falcon-512 | m4-ct | 15.1% | 0.5% | 36.7% |
| falcon-512 | opt-ct | 15.4% | 0.5% | 36.5% |
| falcon-512 | opt-leaktime | 19.6% | 0.6% | 36.5% |
| falcon-512-tree | m4-ct | 11.0% | 1.2% | 37.1% |
| falcon-512-tree | opt-ct | 13.9% | 1.2% | 36.8% |
| falcon-512-tree | opt-leaktime | 14.4% | 1.1% | 36.8% |
# Size Evaluation
## Key Encapsulation Schemes
| Scheme | Implementation | .text [bytes] | .data [bytes] | .bss [bytes] | Total [bytes] |
| ------ | -------------- | ------------- | ------------- | ------------ | ------------- |
| kyber1024 | clean | 6,076 | 0 | 0 | 6,076 |
| kyber1024 | m4fspeed | 16,452 | 0 | 0 | 16,452 |
| kyber1024 | m4fstack | 13,708 | 0 | 0 | 13,708 |
| kyber1024-90s | clean | 6,460 | 0 | 0 | 6,460 |
| kyber1024-90s | m4fspeed | 16,936 | 0 | 0 | 16,936 |
| kyber1024-90s | m4fstack | 13,984 | 0 | 0 | 13,984 |
| kyber512 | clean | 4,888 | 0 | 0 | 4,888 |
| kyber512 | m4fspeed | 15,336 | 0 | 0 | 15,336 |
| kyber512 | m4fstack | 12,824 | 0 | 0 | 12,824 |
| kyber512-90s | clean | 5,136 | 0 | 0 | 5,136 |
| kyber512-90s | m4fspeed | 15,820 | 0 | 0 | 15,820 |
| kyber512-90s | m4fstack | 13,088 | 0 | 0 | 13,088 |
| kyber768 | clean | 4,904 | 0 | 0 | 4,904 |
| kyber768 | m4fspeed | 15,528 | 0 | 0 | 15,528 |
| kyber768 | m4fstack | 12,824 | 0 | 0 | 12,824 |
| kyber768-90s | clean | 5,168 | 0 | 0 | 5,168 |
| kyber768-90s | m4fspeed | 16,020 | 0 | 0 | 16,020 |
| kyber768-90s | m4fstack | 13,088 | 0 | 0 | 13,088 |
## Signature Schemes
| Scheme | Implementation | .text [bytes] | .data [bytes] | .bss [bytes] | Total [bytes] |
| ------ | -------------- | ------------- | ------------- | ------------ | ------------- |
| dilithium2 | clean | 7,852 | 0 | 0 | 7,852 |
| dilithium2 | m4f | 18,428 | 0 | 0 | 18,428 |
| dilithium2aes | clean | 14,674 | 0 | 0 | 14,674 |
| dilithium3 | clean | 7,372 | 0 | 0 | 7,372 |
| dilithium3 | m4f | 19,904 | 0 | 0 | 19,904 |
| dilithium3aes | clean | 14,186 | 0 | 0 | 14,186 |
| dilithium5 | clean | 7,652 | 0 | 0 | 7,652 |
| dilithium5 | m4f | 18,220 | 0 | 0 | 18,220 |
| falcon-1024 | clean | 80,785 | 0 | 0 | 80,785 |
| falcon-1024 | m4-ct | 81,073 | 0 | 79,872 | 160,945 |
| falcon-1024 | opt-ct | 81,073 | 0 | 79,872 | 160,945 |
| falcon-1024 | opt-leaktime | 74,293 | 0 | 79,872 | 154,165 |
| falcon-512 | clean | 80,753 | 0 | 0 | 80,753 |
| falcon-512 | m4-ct | 81,073 | 0 | 39,936 | 121,009 |
| falcon-512 | opt-ct | 81,073 | 0 | 39,936 | 121,009 |
| falcon-512 | opt-leaktime | 74,293 | 0 | 39,936 | 114,229 |
| falcon-512-tree | m4-ct | 80,813 | 0 | 27,648 | 108,461 |
| falcon-512-tree | opt-ct | 80,813 | 0 | 27,648 | 108,461 |
| falcon-512-tree | opt-leaktime | 74,033 | 0 | 27,648 | 101,681 |
