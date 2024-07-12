# Sum-compress

Encrypt and Decrypt with Sum-Compress

## Mechanisms

### Sum-compress

Compression

1. Get a keys set whose any two combinations are unique
2. Make original data to four bits array
3. Loop three pairs of data, called A, B, C
4. Record sequence data (comseq=A==B abseq=A<B)
5. If A==B, B++
6. Pass A, B, C through keys
7. Record S=A+B+C, Z=A+B-C

Decompression

1. Loop two pairs of data, called S, Z
2. Get C=(S-Z)/2, A+B=S-C
3. Get A,B from combination of A+B
4. To know the order of A and B, refer to abseq
5. Adjust B by referring to comseq
6. Get original A,B,C by passing through keys

### Encryption

Encryption

1. Compress data
2. Get indicies from data
3. Add indicies with increasing offset
4. Get data with keys, indicies

Decryption

1. Get indicies from data
2. Subtract indicies with increasing offset
3. Get data with keys, indicies
4. Decompress data

## Example
