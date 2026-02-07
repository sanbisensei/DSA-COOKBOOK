**jaja shikhlam**

_brute force diye leetcode e sumbit dawa jacche na coz onek boro array hoile onek time lagbe coz amra 2ta loop use korsilam jar karone time complexity o(n^2) hoyeche_

_we used unordered_set stl._

> > suppose vector[1,2,1,3,5]

- eikhane duplicate value insert kora jay but ignore kore, so ami ja korsi sheita hocche:
  - unordered set banaisi jeitar name disi `seen`
  - FOREACH LOOP use korsi jetay vector er value gulo re nisi then oida diye check korsi seen er ache kina --  
    (`seen.count(i)`) eita always amake 0 return korbe coz `seen(1) = 0` kenona amra faka unordered set banaisilam.  
    Jehetu if statement e ekhon 0 eshe geche so eita false return korbe and pore `seen.insert(i)` which is the first value that in this example i = 1.
  - in 2nd iteration same shit  
    `seen.count(2)` which will give false  
    then insert 2. Etokkhon e `seen` e amar `{1,2}` chole ashche.
  - ebar 3rd iteration e `seen.count(1)` eibar true coz 1 exists in `seen`. So true return korbe.

**Time Complexity:** O(n)
