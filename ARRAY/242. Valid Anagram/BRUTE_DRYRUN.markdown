## Input

- `str1 = "aba"`
- `str2 = "baa"`

```
str1vec = ['a', 'b', 'a']
str2vec = ['b', 'a', 'a']
```

#### Iteration i=0 (str1vec[0] = 'a')

- Inner loop checks str2vec for 'a'
  - j=0: str2vec[0]='b' ≠ 'a' ❌ → continue
  - j=1: str2vec[1]='a' = 'a' ✅ → match found!
  - Mark str2vec[1] = '#'
  - matched = true, break
- str2vec = ['b', '#', 'a']

#### Iteration i=1 (str1vec[1] = 'b')

- Inner loop checks str2vec for 'b'
  - j=0: str2vec[0]='b' = 'b' ✅ → match found!
  - Mark str2vec[0] = '#'
  - matched = true, break
- str2vec = ['#', '#', 'a']

#### Iteration i=2 (str1vec[2] = 'a')

- Inner loop checks str2vec for 'a'
  - j=0: str2vec[0]='#' ≠ 'a' ❌ → continue
  - j=1: str2vec[1]='#' ≠ 'a' ❌ → continue
  - j=2: str2vec[2]='a' = 'a' ✅ → match found!
  - Mark str2vec[2] = '#'
  - matched = true, break
- str2vec = ['#', '#', '#']

### Step 3: Final Result

- All characters from str1 found matches in str2
- Output: **"Anagram is available"**

## Conclusion

✅ The program correctly identifies that "aba" and "baa" are anagrams.
