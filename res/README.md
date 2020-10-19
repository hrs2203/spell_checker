# Detailed Explanation

## Check Spelling

[Detailed Explanation](./SpellCheckerS2018064.pdf)

```bash
(proj_env) $ python3 manage.py run

Enter your string: simr adr peopel
```

<table>
    <tr>
        <th>Word</th><th>isCorrect</th><th>possibleWord</th><th>suggestList</th>
    </tr>
    <tr>
        <td>simr</td><td>False</td><td>six</td><td>['six', 'sri', 'air', 'sit', 'sirs', 'sir'] </td>
    </tr>
    <tr>
        <td>adr</td><td>False</td><td>and</td><td>['and', 'or', 'do', 'r', 'mr', 'di', 'pair', 'air', 'de', 'adds', 'd', 'aim', 'da', 'ur', 'sir', 'dr', 'hair', 'add']</td>
    </tr>
    <tr>
        <td>peopel</td><td>False</td><td>people</td><td>['people']</td>
    </tr>
</table>
<br>

## Train on New dataset

[Detailed Explanation](./SpellCheckerS2018064.pdf)

create a new file in `/src/data/train_data_set/fileName.txt`
of any name of your choice and exectute the command

```bash
(proj_env) $ python3 manage.py train
```

## Add new word to dataset

[Detailed Explanation](./SpellCheckerS2018064.pdf)


```bas

(proj_env) $ python3 manage.py addWord

Enter word seprated by space (eg. some,people,are)
-> simple james
simple added to data/search_data/si.txt
james added to data/search_data/j.txt
```